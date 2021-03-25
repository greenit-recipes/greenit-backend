import graphene

from tag.mutations import CreateCategory, CreateTag

from .models import Category, Tag
from .type import CategoryType, TagType


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


class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()
    create_category = CreateCategory.Field()
