import graphene

from .models import Ingredient
from .type import IngredientType


class IngredientInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()


class CreateIngredient(graphene.Mutation):
    class Arguments:
        data = IngredientInput(required=True)

    Output = IngredientType

    def mutate(root, info, data):
        return Ingredient.objects.create(name=data.name, description=data.description)
