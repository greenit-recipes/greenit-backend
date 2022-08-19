import graphene
from graphene_django import DjangoObjectType

from tag.type import TagType

from .models import Ingredient, IngredientAmount


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = (
        'id', 'name', 'description', 'image', 'tags', 'alternative', 'is_supermarket', 'is_online', 'is_productor')


class IngredientAmountType(DjangoObjectType):
    id = graphene.UUID(required=True)
    name = graphene.String()
    description = graphene.String()
    image = graphene.String()
    tags = graphene.List(TagType, default_value=[])
    alternative = graphene.String()
    amount = graphene.String()
    is_supermarket = graphene.Boolean()
    is_online = graphene.Boolean()
    is_productor = graphene.Boolean()

    def resolve_name(parent, info):
        return parent.ingredient.name

    def resolve_alternative(parent, info):
        return parent.ingredient.alternative

    def resolve_is_supermarket(parent, info):
        return parent.ingredient.is_supermarket

    def resolve_is_online(parent, info):
        return parent.ingredient.is_online

    def resolve_is_productor(parent, info):
        return parent.ingredient.is_productor

    def resolve_description(parent, info):
        return parent.ingredient.description

    def resolve_image(parent, info):
        return parent.ingredient.image

    def resolve_tags(parent, info):
        return parent.ingredient.tags.all()

    def resolve_id(parent, info):
        return parent.ingredient.id

    class Meta:
        model = IngredientAmount
        fields = ('id', 'name', 'description', 'image', 'tags', 'amount', 'alternative', 'is_supermarket', 'is_online',
                  'is_productor')


class IngredientShoppingListUserType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description', 'image')


class IngredientAtHomeUserType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description', 'image')
