import graphene
from graphene_django import DjangoObjectType

from tag.type import TagType

from .models import Ingredient, IngredientAmount


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description', 'image', 'tags')


class IngredientAmountType(DjangoObjectType):
    id = graphene.UUID(required=True)
    name = graphene.String(required=True)
    description = graphene.String(required=True)
    image = graphene.String(required=True)
    tags = graphene.List(TagType, required=True, default_value=[])

    def resolve_name(parent, info):
        return parent.ingredient.name

    def resolve_image(parent, info):
        return parent.ingredient.image

    def resolve_description(parent, info):
        return parent.ingredient.description

    def resolve_tags(parent, info):
        return parent.ingredient.tags.all()

    def resolve_id(parent, info):
        return parent.ingredient.id

    class Meta:
        model = IngredientAmount
        fields = ('id', 'name', 'description', 'image', 'tags', 'amount')
