import graphene
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


class Query(graphene.ObjectType):
    all_tags = graphene.List(TagType)
    tag = graphene.Field(TagType, id=graphene.String(required=True))
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.String(required=True))

    def resolve_tag(self, info, id):
        try:
            return Tag.objects.get(pk=id)
        except:
            raise Exception('Tag does not exist!')

    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_category(self, info, id):
        try:
            return Category.objects.get(pk=id)
        except:
            raise Exception('Category does not exist!')

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
