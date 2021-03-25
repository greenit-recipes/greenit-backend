import graphene
from graphene_django import DjangoObjectType

from .models import Recipe

# Imports language choices from .models to prevent code duplication
LanguageFilter = graphene.Enum.from_enum(Recipe.LanguageChoice)
DifficultyFilter = graphene.Enum.from_enum(Recipe.DifficultyChoice)
LicenseFilter = graphene.Enum.from_enum(Recipe.LicenseChoice)


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
