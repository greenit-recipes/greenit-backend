import graphene

from .models import Category, Tag, Category_Ingredient
from .type import CategoryType, TagType, Category_IngredientType


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

class Category_IngredientInput(graphene.InputObjectType):
    name = graphene.String()


class CreateCategory_Ingredient(graphene.Mutation):
    class Arguments:
        data = Category_IngredientInput(required=True)

    category_ingredient = graphene.Field(Category_IngredientType)

    def mutate(root, info, data):
        category_ingredient = Category_Ingredient.objects.create(name=data.name)

        return CreateCategory_Ingredient(category_ingredient=category_ingredient)
