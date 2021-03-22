import graphene

from .models import Recipe
from .type import RecipeType


class RecipeInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    video_url = graphene.String()
    duration = graphene.Int()


class CreateRecipe(graphene.Mutation):
    class Arguments:
        data = RecipeInput(required=True)

    Output = RecipeType

    def mutate(root, info, data):
        return Recipe.objects.create(
            name=data.name,
            description=data.description,
            video_url=data.video_url,
            duration=data.duration,
        )
