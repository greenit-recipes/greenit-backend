import graphene
from graphql import GraphQLError

from tag.mutations import CreateCategory, CreateTag, CreateCategory_Ingredient

from .models import Category, Tag, Category_Ingredient
from .type import CategoryType, TagType, Category_IngredientType


class Query(graphene.ObjectType):
    all_tags = graphene.List(TagType)
    tag = graphene.Field(TagType, id=graphene.String(required=True))
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.String(required=True))
    all_categories_ingredient = graphene.List(Category_IngredientType)
    category_ingredient = graphene.Field(Category_IngredientType, id=graphene.String(required=True))

    def resolve_tag(self, info, id):
        return Tag.objects.get(pk=id)

    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_category(self, info, id):
        return Category.objects.get(pk=id)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    
    def resolve_category_ingredient(self, info, id):
        return Category_Ingredient.objects.get(pk=id)

    def resolve_all_categories_ingredient(self, info, **kwargs):
        return Category_Ingredient.objects.all()


class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()
    create_category = CreateCategory.Field()
    create_category_ingredient = CreateCategory_Ingredient.Field()
