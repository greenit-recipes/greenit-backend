import graphene
from graphene_django import DjangoObjectType


from tag.type import TagType

from .models import Ingredient, IngredientAmount


class IngredientType(DjangoObjectType):

    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'description',
            'image',
            'image_optional2',
            'image_optional3',
            'tags',
            'category_ingredient',
            'alternative',
            'information_market',
            'indication',
            'precaution',
            'contenance',
            'rating',
            'price',
            'producer',
            'is_for_market',
            'is_supermarket',
            'is_online',
            'is_productor'
        )


class IngredientAmountType(DjangoObjectType):
    id = graphene.UUID(required=True)
    name = graphene.String()
    description = graphene.String()
    image = graphene.String()
    image_optional2 = graphene.String()
    image_optional3 = graphene.String()
    tags = graphene.List(TagType, default_value=[])
    alternative = graphene.String()
    information_market = graphene.String()
    indication = graphene.String()
    precaution = graphene.String()
    contenance = graphene.String()
    rating = graphene.String()
    price = graphene.String()
    producer = graphene.String()
    amount = graphene.String()
    is_for_market = graphene.Boolean()
    is_supermarket = graphene.Boolean()
    is_online = graphene.Boolean()
    is_productor = graphene.Boolean()

    def resolve_name(parent, info):
        return parent.ingredient.name

    def resolve_alternative(parent, info):
        return parent.ingredient.alternative

    def resolve_information_market(parent, info):
        return parent.ingredient.information_market

    def resolve_indication(parent, info):
        return parent.ingredient.indication

    def resolve_precaution(parent, info):
        return parent.ingredient.precaution

    def resolve_contenance(parent, info):
        return parent.ingredient.contenance

    def resolve_rating(parent, info):
        return parent.ingredient.rating

    def resolve_price(parent, info):
        return parent.ingredient.price

    def resolve_producer(parent, info):
        return parent.ingredient.producer

    def resolve_is_for_market(parent, info):
        return parent.ingredient.is_for_market

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

    def resolve_image_optional2(parent, info):
        return parent.ingredient.image_optional2

    def resolve_image_optional3(parent, info):
        return parent.ingredient.image_optional3

    def resolve_tags(parent, info):
        return parent.ingredient.tags.all()

    def resolve_category_ingredient(parent, info):
        return parent.ingredient.category_ingredient

    def resolve_id(parent, info):
        return parent.ingredient.id

    class Meta:
        model = IngredientAmount
        fields = (
            'id',
            'name',
            'description',
            'image',
            'image_optional2',
            'image_optional3',
            'tags',
            'alternative',
            'information_market',
            'indication',
            'precaution',
            'contenance',
            'rating',
            'price',
            'producer',
            'is_for_market',
            'is_supermarket',
            'is_online',
            'is_productor'
        )


class IngredientShoppingListUserType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'description',
            'image',
            'image_optional2',
            'image_optional3',
            'tags',
            'alternative',
            'price',
            'producer',
            'information_market',
            'is_for_market',
            'is_supermarket',
            'is_online',
            'is_productor'
        )


class IngredientAtHomeUserType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'description',
            'image',
            'image_optional2',
            'image_optional3',
            'tags',
            'alternative',
            'price',
            'producer',
            'information_market',
            'is_for_market',
            'is_supermarket',
            'is_online',
            'is_productor'
        )
