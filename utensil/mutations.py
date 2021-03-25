import graphene

from .models import Utensil
from .type import UtensilType


class CreateUtensilInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    # image =


class CreateUtensil(graphene.Mutation):
    class Arguments:
        data = CreateUtensilInput(required=True)

    utensil = graphene.Field(UtensilType)

    def mutate(root, info, data):
        utensil = Utensil.objects.create(name=data.name, description=data.description)

        return CreateUtensil(utensil=utensil)
