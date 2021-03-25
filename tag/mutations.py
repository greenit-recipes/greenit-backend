import graphene

from .models import Category, Tag
from .type import CategoryType, TagType


class TagInput(graphene.InputObjectType):
    name = graphene.String()


class CreateTag(graphene.Mutation):
    class Arguments:
        data = TagInput(required=True)

    tag = graphene.Field(TagType)

    def mutate(root, info, data):
        tag = Tag.objects.create(name=data.name)

        return CreateTag(tag=tag)


class CategoryInput(graphene.InputObjectType):
    name = graphene.String()


class CreateCategory(graphene.Mutation):
    class Arguments:
        data = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    def mutate(root, info, data):
        category = Category.objects.create(name=data.name)

        return CreateCategory(category=category)
