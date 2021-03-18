import graphene
from graphene_django import DjangoObjectType

from recipe.mutations import CreateRecipe
from user.models import User
from user.schema import UserType

from .models import Recipe
from .type import RecipeType

#Imports language choices from .models to prevent code duplication
language_choices = Recipe.LanguageChoice._member_map_
#Dynamic class
LanguageFilter = type(
    'LanguageFilter',
    (graphene.Enum,),
    {str(k): str(v) for k, v in language_choices.items()},
)

difficulty_choices = Recipe.DifficultyChoice._member_map_
DifficultyFilter = type(
    'DifficultyFilter',
    (graphene.Enum,),
    {str(k): str(v) for k, v in difficulty_choices.items()},
)

license_choices = Recipe.LicenseChoice._member_map_
LicenseFilter = type(
    'LicenseFilter',
    (graphene.Enum,),
    {str(k): str(v) for k, v in license_choices.items()},
)





class RecipeFilterInput(graphene.InputObjectType):
    language = LanguageFilter(required=False)
    difficulty = DifficultyFilter(required=False)
    license = LicenseFilter(required=False)
    rating = graphene.Int(required=False)
    duration = graphene.Int(required=False)
    author = graphene.String(required=False)


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
