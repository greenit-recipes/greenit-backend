import graphene
from graphene_django import DjangoObjectType

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


class Query(graphene.ObjectType):
    all_recipes = graphene.List(RecipeType, filter=RecipeFilterInput(required=False))
    recipe = graphene.Field(RecipeType, id=graphene.String(required=True))

    def resolve_all_recipes(self, info, filter=None, **kwargs):
        def get_filter(filter):
            filter = {}
            if filter.get('language'):
                filter['language'] = filter['language']
            if filter.get('rating'):
                filter['rating__gte'] = filter['rating']
            return filter

        filter = get_filter(filter) if filter else {}
        return Recipe.objects.filter(**filter)

    def resolve_recipe(self, info, id):
        try:
            return Recipe.objects.get(pk=id)
        except:
            raise Exception('Invalid UUID. Recipe does not exist!')
