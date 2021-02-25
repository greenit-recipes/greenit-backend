import graphene
from graphene_django import DjangoObjectType

from .models import Ingredient


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description', 'image')


class Query(graphene.ObjectType):
    ingredients = graphene.List(IngredientType)

    def resolve_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()
