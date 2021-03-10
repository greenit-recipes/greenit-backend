from graphene_django import DjangoObjectType

from .models import Ingredient


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description', 'image', 'tags')
