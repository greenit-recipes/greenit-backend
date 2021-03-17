import graphene
from graphene import ObjectType, relay

from ingredient.mutations import CreateIngredient

from .models import Ingredient
from .type import IngredientType


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    ingredient = graphene.Field(IngredientType, id=graphene.String(required=True))

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_ingredient(self, info, id):
        try:
            return Ingredient.objects.get(pk=id)
        except:
            raise Exception('Ingredient does not exist!')


class Mutation(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field()
