import graphene
from graphene_django import DjangoObjectType

from recipe.mutations import CreateRecipe
from tag.models import Category, Tag
from tag.schema import CategoryType, TagType
from user.models import User
from user.schema import UserType
from ingredient.models import Ingredient
from ingredient.schema import IngredientType

from .models import Recipe
from .type import RecipeType

# Imports language choices from .models to prevent code duplication
LanguageFilter = graphene.Enum.from_enum(Recipe.LanguageChoice)
DifficultyFilter = graphene.Enum.from_enum(Recipe.DifficultyChoice)
LicenseFilter = graphene.Enum.from_enum(Recipe.LicenseChoice)



class RecipeFilterInput(graphene.InputObjectType):
    language = LanguageFilter(required=False)
    difficulty = DifficultyFilter(required=False)
    license = LicenseFilter(required=False)
    rating = graphene.Int(required=False)
    duration = graphene.Int(required=False)
    author = graphene.String(required=False)
    tag = graphene.String(required=False)
    category = graphene.String(required=False)
    ingredient = graphene.String(required=False)


class Query(graphene.ObjectType):

    all_recipes = graphene.List(RecipeType, filter=RecipeFilterInput(required=False))
    recipe = graphene.Field(RecipeType, id=graphene.String(required=True))

    def resolve_all_recipes(self, info, filter=None, **kwargs):
        def get_filter(filter):
            filter_params = {}
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
            if filter.get('author'):
                try:
                    user = User.objects.get(pk=filter.get('author'))
                    filter_params['author'] = user
                except User.DoesNotExist:
                    raise Exception('User does not exist!')
            if filter.get('tag'):
                try:
                    tag = Tag.objects.get(pk=filter.get('tag'))
                    filter_params['tags'] = tag
                except Tag.DoesNotExist:
                    raise Exception('Tag does not exist!')
            if filter.get('category'):
                try:
                    category = Category.objects.get(pk=filter.get('category'))
                    filter_params['category'] = category
                except Category.DoesNotExist:
                    raise Exception('Category does not exist!')
            if filter.get('ingredient'):
                try:
                    ingredient = Ingredient.objects.get(pk=filter.get('ingredient'))
                    filter_params['ingredients'] = ingredient
                except Ingredient.DoesNotExist:
                    raise Exception('Ingredient does not exist!')

            return filter_params

        filter = get_filter(filter) if filter else {}

        return Recipe.objects.filter(**filter)

    def resolve_recipe(self, info, id):
        try:
            return Recipe.objects.get(pk=id)
        except:
            raise Exception('Recipe does not exist!')


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
