import graphene
from graphene_django import DjangoObjectType

from .models import Utensil


class UtensilType(DjangoObjectType):
    class Meta:
        model = Utensil


class Query(graphene.ObjectType):
    utensils = graphene.List(UtensilType)

    def resolve_utensils(self, info, **kwargs):
        return Utensil.objects.all()
