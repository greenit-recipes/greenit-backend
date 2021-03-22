from graphene_django import DjangoObjectType

from .models import Category, Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')
