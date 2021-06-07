import graphene
from django.db.models import Count, Q
from graphene.types.generic import GenericScalar
from graphql import GraphQLError

from ingredient.models import Ingredient
from recipe.mutations import CreateRecipe
from tag.models import Category, Tag
from user.models import User
from utensil.models import Utensil

from .models import Recipe
from .type import DifficultyFilter, LanguageFilter, RecipeConnection, RecipeType


class RecipeFilterInput(graphene.InputObjectType):
    language = LanguageFilter(required=False)
    difficulty = DifficultyFilter(required=False)
    rating = graphene.Int(required=False)
    duration = graphene.Int(required=False)
    author = graphene.String(required=False)
    tags = graphene.List(graphene.String, required=False)
    category = graphene.String(required=False)
    ingredients = graphene.List(graphene.String, required=False)
    utensils = graphene.List(graphene.String, required=False)
    search = graphene.String(required=False)
    is_featured = graphene.Boolean(required=False)

class Query(graphene.ObjectType):
    all_recipes = graphene.relay.ConnectionField(
        RecipeConnection, filter=RecipeFilterInput(required=False)
    )
    recipe = graphene.Field(RecipeType, id=graphene.String(required=True))
    filter = graphene.Field(GenericScalar)

    def resolve_all_recipes(self, info, filter=None, **kwargs):
        def get_filter(filter):
            filter_params = {}
            if filter.get('language'):
                filter_params['language'] = filter['language']
            if filter.get('difficulty'):
                filter_params['difficulty'] = filter['difficulty']
            if filter.get('rating'):
                filter_params['rating__gte'] = filter['rating']
            if filter.get('duration'):
                filter_params['duration__lte'] = filter['duration']
            if filter.get('is_featured'):
                filter_params['is_featured'] = filter['is_featured']
            if filter.get('tags'):
                filter_params['tags__name__unaccent__in'] = filter['tags']
            if filter.get('author'):
                try:
                    filter_params['author'] = User.objects.get(pk=filter.get('author'))
                except User.DoesNotExist:
                    raise GraphQLError('User matching query does not exist.')
            if filter.get('category'):
                try:
                    filter_params['category'] = Category.objects.get(
                        name=filter.get('category')
                    )
                except Category.DoesNotExist:
                    raise GraphQLError('Category matching query does not exist.')

            return filter_params

        filter_query = get_filter(filter) if filter else {}
        if filter and filter.get('tags'):
            recipes = (
                Recipe.objects.filter(**filter_query)
                .annotate(num_tags=Count('tags'))
                .filter(num_tags=len(filter.get('tags')))
            )
        else:
            recipes = Recipe.objects.filter(**filter_query)

        if filter and filter.get('search'):
            terms = filter.get('search').split()
            for term in terms:
                recipes = recipes.filter(
                    Q(name__unaccent__icontains=term)
                    | Q(description__unaccent__icontains=term)
                    | Q(tags__name__unaccent__icontains=term)
                    | Q(category__name__unaccent__icontains=term)
                )
        return recipes.distinct()

    def resolve_recipe(self, info, id):
        return Recipe.objects.get(url_id=id)


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
