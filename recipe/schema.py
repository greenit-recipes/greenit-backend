from typing import List

import graphene
from django.db.models import Count, Q
from graphene.types.generic import GenericScalar
from graphql import GraphQLError
from ingredient.models import Ingredient
from tag.models import Category, Tag
from user.models import User
from utensil.models import Utensil
from ingredient.models import IngredientAmount

from recipe.mutations import (AddOrRemoveFavoriteRecipe, AddOrRemoveLikeRecipe,
                              CreateRecipe, SendEmailRecipe)

from .models import Recipe
from .type import (DifficultyFilter, LanguageFilter, RecipeConnection,
                   RecipeType)
from django.core import serializers


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

class Query(graphene.ObjectType):
    all_recipes = graphene.relay.ConnectionField(
        RecipeConnection, filter=RecipeFilterInput(required=False)
    )
    recipe = graphene.Field(RecipeType, id = graphene.String(required=False, default_value=None), userId = graphene.String(required=False, default_value=None))
    filter = graphene.Field(GenericScalar)

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
            if filter.get('author'):
                try:
                    filter_params['author'] = User.objects.get(pk=filter.get('author'))
                except User.DoesNotExist:
                    raise GraphQLError('User matching query does not exist.')
            if filter.get('number_of_ingredients'):
                filter_params['num_ingredient__in'] = filter['number_of_ingredients']
            return filter_params

        filter_query = get_filter(filter) if filter else {}
        recipes = Recipe.objects.annotate(num_ingredient=Count('ingredientamount')).filter(**filter_query).order_by('-created_at')


        if filter and filter.get('search'):
            terms = filter.get('search').split()
            for term in terms:
                recipes = recipes.filter(
                    Q(name__unaccent__icontains=term)
                )
        return recipes.distinct()

    def resolve_recipe(self, info, id=None, userId=None):
        if (id):
            return Recipe.objects.get(id=id)
        if (userId):
            return Recipe.objects.get(author_id=userId)
        return


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    send_email_recipe = SendEmailRecipe.Field()
    add_or_remove_like_recipe = AddOrRemoveLikeRecipe.Field()
    add_or_remove_favorite_recipe = AddOrRemoveFavoriteRecipe.Field()
