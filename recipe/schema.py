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


class Query(graphene.ObjectType):
    recipes = graphene.List(RecipeType)

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()
