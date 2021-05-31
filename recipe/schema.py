import graphene
from graphql import GraphQLError

from ingredient.models import Ingredient
from recipe.mutations import CreateRecipe
from tag.models import Category, Tag
from user.models import User
from utensil.models import Utensil
from django.db.models import Q

from .models import Recipe
from .type import DifficultyFilter, LanguageFilter, LicenseFilter, RecipeType


class SearchFilterInput(graphene.InputObjectType):
    string = graphene.String(required=True)


class RecipeFilterInput(graphene.InputObjectType):
    language = LanguageFilter(required=False)
    difficulty = DifficultyFilter(required=False)
    license = LicenseFilter(required=False)
    rating = graphene.Int(required=False)
    duration = graphene.Int(required=False)
    author = graphene.String(required=False)
    tags = graphene.List(graphene.String, required=False)
    category = graphene.String(required=False)
    ingredients = graphene.List(graphene.String, required=False)
    utensils = graphene.List(graphene.String, required=False)


class Query(graphene.ObjectType):

    all_recipes = graphene.List(RecipeType, filter=RecipeFilterInput(required=False))
    recipe = graphene.Field(RecipeType, id=graphene.String(required=True))
    search_recipes = graphene.List(RecipeType, filter=SearchFilterInput(required=True))

    def resolve_all_recipes(self, info, filter=None, **kwargs):
        def get_filter(filter):

            # Initialize Dict for standard filters and empty Queryset for chained filters # noqa E501
            filter_params = {}
            filter_set = Recipe.objects.none()
            if filter.get('language'):
                filter_params['language'] = filter['language']
            if filter.get('difficulty'):
                filter_params['difficulty'] = filter['difficulty']
            if filter.get('license'):
                filter_params['license'] = filter['license']
            if filter.get('rating'):
                filter_params['rating__gte'] = filter['rating']
            if filter.get('duration'):
                filter_params['duration__lte'] = filter['duration']

            # Foreign Key filters
            if filter.get('author'):
                try:
                    user = User.objects.get(pk=filter.get('author'))
                    filter_params['author'] = user
                except User.DoesNotExist:
                    raise GraphQLError('User matching query does not exist.')
            if filter.get('category'):
                try:
                    category = Category.objects.get(pk=filter.get('category'))
                    filter_params['category'] = category
                except Category.DoesNotExist:
                    raise GraphQLError('Category matching query does not exist.')

            # M2M with AND-chained filters
            if filter.get('tags'):
                try:
                    ids = filter.get('tags')
                    # Initial Queryset consists of first tag-id
                    filter_set = Recipe.objects.filter(tags=ids[0])
                    # Filter Queryset with second query if multiple recipies still in question # noqa E501
                    if len(filter_set) > 1:
                        for id in ids[1:]:
                            if len(filter_set) > 1:
                                filter_set = filter_set.filter(tags=id)
                            else:
                                break
                except Tag.DoesNotExist:
                    raise GraphQLError('Tag matching query does not exist.')
            if filter.get('ingredients'):
                try:
                    ids = filter.get('ingredients')
                    filter_set = Recipe.objects.filter(ingredients=ids[0])
                    if len(filter_set) > 1:
                        for id in ids[1:]:
                            if len(filter_set) > 1:
                                filter_set = filter_set.filter(ingredients=id)
                            else:
                                break
                except Ingredient.DoesNotExist:
                    raise GraphQLError('Ingredient matching query does not exist.')
            if filter.get('utensils'):
                try:
                    ids = filter.get('utensils')
                    filter_set = Recipe.objects.filter(utensils=ids[0])
                    if len(filter_set) > 1:
                        for id in ids[1:]:
                            if len(filter_set) > 1:
                                filter_set = filter_set.filter(utensils=id)
                            else:
                                break
                except Utensil.DoesNotExist:
                    raise GraphQLError('Utensil matching query does not exist.')

            if filter_params:
                return filter_params
            else:
                return filter_set

        filter = get_filter(filter) if filter else {}

        # If get_filter returns a dictionary, then apply standard filtering and return results # noqa E501
        if isinstance(filter, dict):
            return Recipe.objects.filter(**filter)
        # If get_filter returns a Queryset, then filtering is already complete.
        # Remove duplicates with .distinct() and return results
        else:
            return filter.distinct()

    def resolve_recipe(self, info, id):
        return Recipe.objects.get(pk=id)

    def resolve_search_recipes(self, info, filter=SearchFilterInput(required=True)):
        filter = filter['string'].split()
        recipes = Recipe.objects.none()
        for term in filter:
            recipes = recipes | Recipe.objects.filter(
                Q(name__icontains=term)
                | Q(description__icontains=term)
                | Q(duration__icontains=term)
                | Q(tags__name__icontains=term)
                | Q(category__name__icontains=term)
            )
        return recipes.distinct()


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
