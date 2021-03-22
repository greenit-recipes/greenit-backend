import graphene

from .models import Recipe
from .type import RecipeType


class RecipeInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()


class CreateRecipe(graphene.Mutation):
    class Arguments:
        data = RecipeInput(required=True)

    Output = RecipeType

    def mutate(root, info, data):
        return Recipe.objects.create(name=data.name, description=data.description)
