import graphene

from .models import Category, Tag
from .type import CategoryType, TagType

class TagInput(graphene.InputObjectType):
    name = graphene.String()


class CreateTag(graphene.Mutation):
    class Arguments:
        data = TagInput(required=True)

    Output = TagType

    def mutate(root, info, data):
        return Tag.objects.create(name=data.name)

class CategoryInput(graphene.InputObjectType):
    name = graphene.String()


class CreateCategory(graphene.Mutation):
    class Arguments:
        data = CategoryInput(required=True)

    Output = CategoryType

    def mutate(root, info, data):
        return Category.objects.create(name=data.name)
