import graphene
from graphene_django import DjangoObjectType

from .models import Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class Query(graphene.ObjectType):
    tags = graphene.List(TagType)

    def resolve_tags(self, info, **kwargs):
        return Tag.objects.all()
