import graphene
from graphene_django import DjangoObjectType

from .models import Utensil


class UtensilType(DjangoObjectType):
    class Meta:
        model = Utensil
        fields = ('id', 'name', 'description', 'image', 'tags')


class Query(graphene.ObjectType):
    utensils = graphene.List(UtensilType)

    def resolve_utensils(self, info, **kwargs):
        return Utensil.objects.all()
