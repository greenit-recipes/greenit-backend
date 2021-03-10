import graphene
from graphene import ObjectType, relay

from ingredient.mutations import CreateIngredient

from .models import Ingredient
from .type import IngredientType


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()


class Mutation(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field()
