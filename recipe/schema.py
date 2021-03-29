import graphene

from ingredient.models import Ingredient
from recipe.mutations import CreateRecipe
from tag.models import Category, Tag
from user.models import User

from .models import Recipe
from .type import DifficultyFilter, LanguageFilter, LicenseFilter, RecipeType


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

    def resolve_all_recipes(self, info, filter=None, **kwargs):
        def get_filter(filter):

            # Initialize Dict for standard filters and empty Queryset for chained filters
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
                    raise Exception('User does not exist!')
            if filter.get('category'):
                try:
                    category = Category.objects.get(pk=filter.get('category'))
                    filter_params['category'] = category
                except Category.DoesNotExist:
                    raise Exception('Category does not exist!')

            # M2M with AND-chained filters
            if filter.get('tags'):
                try:
                    # Initial Queryset consists of first tag-id
                    id = filter.get('tags')
                    filter_set = Recipe.objects.filter(tags=id[0])
                    # Intersecting results between initial Queryset and any additional Querysets
                    for id in filter.get('tags'):
                        filter_set = filter_set.intersection(
                            filter_set, Recipe.objects.filter(tags=id)
                        )
                except Tag.DoesNotExist:
                    raise Exception('Tag does not exist!')
            if filter.get('ingredients'):
                try:
                    id = filter.get('ingredients')
                    filter_set = Recipe.objects.filter(ingredients=id[0])
                    for id in filter.get('ingredients'):
                        filter_set = filter_set.intersection(
                            filter_set, Recipe.objects.filter(ingredients=id)
                        )
                except Ingredient.DoesNotExist:
                    raise Exception('Ingredient does not exist!')
            if filter.get('utensil'):
                try:
                    utensil = Utensil.objects.get(pk=filter.get('utensil'))
                    filter_params['utensils'] = utensil
                except Utensil.DoesNotExist:
                    raise Exception('Utensil does not exist!')

            if filter_params:
                return filter_params
            else:
                return filter_set

        filter = get_filter(filter) if filter else {}

        # If get_filter returns a dictionary, then apply standard filtering and return results
        if isinstance(filter, dict):
            return Recipe.objects.filter(**filter)
        # If get_filter returns a Queryset, then filtering is already complete.
        # Remove duplicates with .distinct() and return results
        else:
            return filter.distinct()

    def resolve_recipe(self, info, id):
        try:
            return Recipe.objects.get(pk=id)
        except:
            raise Exception('Recipe does not exist!')


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
