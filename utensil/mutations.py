import graphene

from .models import Utensil
from .type import UtensilType

class UtensilInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()


class CreateUtensil(graphene.Mutation):
    class Arguments:
        data = UtensilInput(required=True)

    Output = UtensilType

    def mutate(root, info, data):
        return Utensil.objects.create(name=data.name, description=data.description)
