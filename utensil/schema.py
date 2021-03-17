import graphene
from graphene_django import DjangoObjectType

from utensil.mutations import CreateUtensil

from .models import Utensil
from .type import UtensilType


class Query(graphene.ObjectType):
    all_utensils = graphene.List(UtensilType)
    utensils = graphene.Field(UtensilType, id=graphene.String(required=True))

    def resolve_all_utensils(self, info, **kwargs):
        return Utensil.objects.all()

    def resolve_utensil(self, info, id):
        try:
            return Utensil.objects.get(pk=id)
        except:
            raise Exception('Utensil does not exist!')


class Mutation(graphene.ObjectType):
    create_utensil = CreateUtensil.Field()
