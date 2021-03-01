import graphene
from graphene_django import DjangoObjectType

from .models import Tag
from .models import Category


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class Query(graphene.ObjectType):
    tags = graphene.List(TagType)
    categories = graphene.List(CategoryType)

    def resolve_tags(self, info, **kwargs):
        return Tag.objects.all()
