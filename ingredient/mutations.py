import graphene

from .models import Ingredient
from .type import IngredientType


class CreateIngredientInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    # image =


class CreateIngredient(graphene.Mutation):
    class Arguments:
        data = CreateIngredientInput(required=True)

    ingredient = graphene.Field(IngredientType)

    def mutate(root, info, data):
        ingredient = Ingredient.objects.create(
            name=data.name, description=data.description
        )

        return CreateIngredient(ingredient=ingredient)
