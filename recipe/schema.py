import graphene
from graphene_django import DjangoObjectType

from user.models import User
from user.schema import UserType

from .models import Recipe


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'description',
            'video_url',
            'language',
            'difficulty',
            'rating',
            'duration',
            'license',
            'author',
            'image',
            'tags',
            'category',
            'ingredients',
            'utensils',
        )


# Instead of adding the enums here, find out how to import them from Recipe
class LanguageFilter(graphene.Enum):
    GERMAN = 'de'
    ENGLISH = 'en'


class RecipeFilterInput(graphene.InputObjectType):
    language = LanguageFilter(required=False)
    rating = graphene.Int(required=False)
    duration = graphene.Int(required=False)


class Query(graphene.ObjectType):

    all_recipes = graphene.List(RecipeType, filter=RecipeFilterInput(required=False))
    recipe = graphene.Field(RecipeType, id=graphene.String(required=True))

    def resolve_all_recipes(self, info, filter=None, **kwargs):
        def get_filter(filter):
            filter_params = {}
            if filter.get('language'):
                filter_params['language'] = filter['language']
            if filter.get('rating'):
                filter_params['rating__gte'] = filter['rating']
            if filter.get('duration'):
                filter_params['duration__lte'] = filter['duration']
            return filter_params

        filter = get_filter(filter) if filter else {}

        return Recipe.objects.filter(**filter)

    def resolve_recipe(self, info, id):
        try:
            return Recipe.objects.get(pk=id)
        except:
            raise Exception('Recipe does not exist!')
