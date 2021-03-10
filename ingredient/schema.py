import graphene
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Ingredient


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description', 'image', 'tags')


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['iexact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
    ingredient = relay.Node.Field(IngredientNode)
