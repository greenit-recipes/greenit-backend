import graphene
from graphene_django import DjangoObjectType

from .models import Recipe


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe


class Query(graphene.ObjectType):
    recipes = graphene.List(RecipeType)

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()
