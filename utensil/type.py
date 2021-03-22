from graphene_django import DjangoObjectType

from .models import Utensil


class UtensilType(DjangoObjectType):
    class Meta:
        model = Utensil
        fields = ('id', 'name', 'description', 'image', 'tags')
