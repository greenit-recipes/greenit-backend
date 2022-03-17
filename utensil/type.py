import graphene

from graphene_django import DjangoObjectType
from tag.type import TagType

from .models import Utensil, UtensilAmount


class UtensilType(DjangoObjectType):
    class Meta:
        model = Utensil
        fields = ('id', 'name', 'description', 'image', 'tags', 'amount')


class UtensilAmountType(DjangoObjectType):
    id = graphene.UUID(required=True)
    name = graphene.String()
    description = graphene.String()
    image = graphene.String()
    tags = graphene.List(TagType, default_value=[])
    amount = graphene.String()

    def resolve_name(parent, info):
        return parent.utensil.name
    
    def resolve_alternative(parent, info):
        return parent.utensil.alternative

    def resolve_description(parent, info):
        return parent.utensil.description
    
    def resolve_image(parent, info):
        return parent.utensil.image

    def resolve_tags(parent, info):
        return parent.utensil.tags.all()

    def resolve_id(parent, info):
        return parent.utensil.id

    class Meta:
        model = UtensilAmount
        fields = ('id', 'name', 'description', 'image', 'tags', 'amount')