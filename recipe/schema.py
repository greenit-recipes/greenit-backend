import random
import unicodedata
from typing import List
import re
import graphene
from django.contrib.postgres.search import (SearchQuery, SearchRank,
                                            SearchVector)
from django.contrib.postgres.aggregates import StringAgg
from django.core import serializers
from django.db.models.functions import Lower
from django.db.models import Count, Q
from graphene.types.generic import GenericScalar
from graphql import GraphQLError
from ingredient.models import Ingredient, IngredientAmount
from tag.models import Category, Tag
from user.models import User
from utensil.models import Utensil

from recipe.mutations import (AddOrRemoveFavoriteRecipe, AddOrRemoveLikeRecipe,
                              AddOrRemoveMadeRecipe, AddViewRecipe,
                              CreateRecipe, EmailLinkSharedRecipe,
                              PlusOrLessMadeRecipe, SendEmailRecipe)

from .models import Recipe
from .type import (DifficultyFilter, LanguageFilter, RecipeConnection,
                   RecipeType, RecipeTypeAutoComplete)

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
   
class RecipeFilterInput(graphene.InputObjectType):
    language = LanguageFilter(required=False)
    difficulty = graphene.List(DifficultyFilter, required=False)
    rating = graphene.Int(required=False)
    duration = graphene.List(graphene.Int, required=False)
    author = graphene.String(required=False)
    tags = graphene.List(graphene.String, required=False)
    category = graphene.List(graphene.String, required=False)
    ingredients = graphene.List(graphene.String, required=False)
    number_of_ingredients = graphene.List(graphene.Int, required=False)
    utensils = graphene.List(graphene.String, required=False)
    search = graphene.String(required=False)
    is_display_home = graphene.Boolean(required=False)
    is_order_by_number_like = graphene.Boolean(required=False)
    is_random_list = graphene.Boolean(required=False)
    exclude_id = graphene.String(required=False)
    id = graphene.List(graphene.String, required=False)

class Query(graphene.ObjectType):
    all_recipes = graphene.relay.ConnectionField(
        RecipeConnection, filter=RecipeFilterInput(required=False)
    )
    all_recipes_seo = graphene.List(RecipeType)
    recipe = graphene.Field(RecipeType, id = graphene.String(required=False, default_value=None), urlId = graphene.String(required=True))
    filter = graphene.Field(GenericScalar)
    search_auto_complete_recipes = graphene.Field(RecipeTypeAutoComplete, search=graphene.String(required=False, default_value=None))

    def resolve_all_recipes(self, info, filter=None, **kwargs):
        def get_filter(filter):
            filter_params = {}
            if filter.get('language'):
                filter_params['language'] = filter['language']
            if filter.get('rating'):
                filter_params['rating__gte'] = filter['rating']
            if filter.get('category'):
                try:
                    filter_params['category__name__unaccent__in'] = filter['category']
                except Category.DoesNotExist:
                    raise GraphQLError('Category matching query does not exist.')
            if filter.get('duration'):
                for duration in filter['duration']:
                    filter_params['duration__lte'] = duration
            if filter.get('is_display_home'):
                filter_params['is_display_home'] = filter['is_display_home']
            if filter.get('tags'):
                filter_params['tags__name__unaccent__in'] = filter['tags']
            if filter.get('difficulty'):
                filter_params['difficulty__in'] = filter['difficulty']
            if filter.get('id'):
                filter_params['id__in'] = filter['id']
            if filter.get('author'):
                try:
                    filter_params['author'] = User.objects.get(pk=filter.get('author'))
                except User.DoesNotExist:
                    raise GraphQLError('User matching query does not exist.')
            if filter.get('number_of_ingredients'):
                filter_params['num_ingredient__in'] = filter['number_of_ingredients']
            return filter_params
        filter_query = get_filter(filter) if filter else {}
        recipes = Recipe.objects.all().annotate(likesNum=Count('likes', distinct=True))
        recipes = recipes.annotate(num_ingredient=Count('ingredientamount', distinct=True))
        recipes = recipes.filter(**filter_query)# recipes.filter(**filter_query).order_by('-likesNum' if filter and filter.get('is_order_by_number_like') else '-created_at')
        
        if filter and filter.get('is_order_by_number_like'):
            recipes = recipes.order_by('-likesNum')
            
        if filter and filter.get('exclude_id'):
            recipes = recipes.exclude(id=filter.get('exclude_id'))

        if filter and filter.get('search'):
            terms = strip_accents(re.sub('(\:|\&|\*)', '', filter.get('search'))).lower().split()
            phrase = ""
            totalLen = len(terms)
            for index, term in enumerate(terms):
                if len(terms) != 1 and index + 1 != totalLen:
                    phrase += str(term) + ":* & "
                else:
                    phrase += str(term) + ":*"
            search_vectors_recipes = SearchVector(StringAgg(Lower('name__unaccent'), delimiter=' '), StringAgg(Lower('ingredients__name__unaccent'), delimiter=' '))       
            search_query_reccipes = SearchQuery(phrase, search_type='raw')
            recipes = recipes.annotate(search=search_vectors_recipes, rank=SearchRank(search_vectors_recipes, search_query_reccipes)).filter(search=search_query_reccipes).order_by('-rank') 
        if filter and filter.get('is_random_list'):
            return random.sample(list(recipes), len(recipes)) 
        else:
            return recipes

    def resolve_all_recipes_seo(self, info):
        return Recipe.objects.all()
    
    def resolve_recipe(self, info, urlId=None, userId=None):
        if (urlId):
            return Recipe.objects.get(url_id=urlId)
        if (userId):
            return Recipe.objects.get(author_id=userId)
        return
    
    def resolve_search_auto_complete_recipes(self, info, search=None):
        if not (search):
            return
        terms = strip_accents(re.sub('(\:|\&|\*|\(|\)|\'|\<|\>)', '', search)).lower().split()
        phrase = ""
        totalLen = len(terms)
        for index, term in enumerate(terms):
            if len(terms) != 1 and index + 1 != totalLen:
                phrase += str(term) + ":* & "
            else:
                phrase += str(term) + ":*"
        search_vectors_recipes = SearchVector(Lower('name__unaccent'))      
        search_query_reccipes = SearchQuery(phrase, search_type='raw')
        recipes = Recipe.objects.annotate(search=search_vectors_recipes, rank=SearchRank(search_vectors_recipes, search_query_reccipes)).order_by('-rank').filter(search=search_query_reccipes)[:3]
        
        search_vectors_ingredients = SearchVector(Lower('name__unaccent'))       
        search_query_ingredients = SearchQuery(phrase, search_type='raw')
        ingredients = Ingredient.objects.annotate(search=search_vectors_ingredients, rank=SearchRank(search_vectors_ingredients, search_query_ingredients)).order_by('-rank').filter(search=search_query_ingredients)[:3]
        
        search_vectors_count = SearchVector(StringAgg(Lower('name__unaccent'), delimiter=' '), StringAgg(Lower('ingredients__name__unaccent'), delimiter=' '))       
        search_query_count = SearchQuery(phrase, search_type='raw')
        totalRecipes = Recipe.objects.annotate(search=search_vectors_count).filter(search=search_query_count).count()
        return RecipeTypeAutoComplete(recipes =recipes, ingredients= ingredients, totalRecipes=totalRecipes)


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    send_email_recipe = SendEmailRecipe.Field()
    email_link_shared_recipe = EmailLinkSharedRecipe.Field()
    add_or_remove_like_recipe = AddOrRemoveLikeRecipe.Field()
    add_or_remove_made_recipe = AddOrRemoveMadeRecipe.Field()
    add_view_recipe = AddViewRecipe.Field()
    plus_or_less_made_recipe = PlusOrLessMadeRecipe.Field()
    add_or_remove_favorite_recipe = AddOrRemoveFavoriteRecipe.Field()