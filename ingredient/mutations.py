import graphene

from .models import Ingredient
from .type import IngredientType


class IngredientTagInput(graphene.InputObjectType):
    name = graphene.String(required=True)

class CreateIngredientInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    # image =
    tags = graphene.List(IngredientTagInput, required=True)

class CreateIngredient(graphene.Mutation):
    class Arguments:
        data = CreateIngredientInput(required=True)

    Output = IngredientType

    def mutate(root, info, data):
        return Ingredient.objects.create(name=data.name, description=data.description)
