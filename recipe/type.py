import graphene
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType

from ingredient.type import IngredientAmountType

from .models import Recipe

# Imports language choices from .models to prevent code duplication
LanguageFilter = graphene.Enum.from_enum(Recipe.LanguageChoice)
DifficultyFilter = graphene.Enum.from_enum(Recipe.DifficultyChoice)


class RecipeType(DjangoObjectType):
    instructions = GenericScalar()

    def resolve_ingredients(parent, info):
        return parent.ingredients.through.objects.filter(recipe__id=parent.id)

    ingredients = graphene.List(
        graphene.NonNull(IngredientAmountType), required=True, default_value=[]
    )

    class Meta:
        interfaces = (graphene.relay.Node,)
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
            'author',
            'image',
            'tags',
            'category',
            'utensils',
            'instructions',
            'url_id',
            'video_url',
            'expiry',
            'notes_from_author'
        )


class RecipeConnection(graphene.relay.Connection):
    class Meta:
        node = RecipeType
