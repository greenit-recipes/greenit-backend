import graphene

from .models import Utensil
from .type import UtensilType

class UtensilTagInput(graphene.InputObjectType):
    name = graphene.String(required=True)

class CreateUtensilInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    # image =
    tags = graphene.List(UtensilTagInput, required=True)

class CreateUtensil(graphene.Mutation):
    class Arguments:
        data = CreateUtensilInput(required=True)

    Output = UtensilType

    def mutate(root, info, data):
        return Utensil.objects.create(name=data.name, description=data.description)
