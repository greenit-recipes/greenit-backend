from graphene_django import DjangoObjectType

from .models import Category, Tag, Category_Ingredient


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')

class Category_IngredientType(DjangoObjectType):
    class Meta:
        model = Category_Ingredient
        fields = ('id', 'name')
