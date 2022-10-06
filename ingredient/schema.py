import graphene
from graphql import GraphQLError

from ingredient.mutations import CreateIngredient, CreateOrDeleteIngredientShoppingList, \
    CreateOrDeleteIngredientAtHomeUser
from tag.models import Category_Ingredient, Tag
from graphene.types.generic import GenericScalar


from .models import Ingredient
from .type import IngredientType


class IngredientFilterInput(graphene.InputObjectType):
    tag = graphene.String(required=False)
    category_ingredient = graphene.List(graphene.String, required=False)
    is_for_market = graphene.Boolean(required=False)
    name = graphene.String(required=False)


class Query(graphene.ObjectType):
    ingredients_for_market = graphene.List(
        IngredientType, filter=IngredientFilterInput(required=False))
    all_ingredients = graphene.List(
        IngredientType, filter=IngredientFilterInput(required=False))
    ingredient = graphene.Field(IngredientType, id=graphene.String(required=False))
  

    def resolve_all_ingredients(self, info, filter=None, **kwargs):
        def get_filter(filter):
            filter_params = {}
            if filter.get('tag'):
                try:
                    tag = Tag.objects.get(pk=filter.get('tag'))
                    filter_params['tags'] = tag
                except Tag.DoesNotExist:
                    raise GraphQLError('Tag matching query does not exist.')
            if filter.get('category_ingredient'):
                try:
                    filter_params['category_ingredient__name__unaccent__in'] = filter['category_ingredient']
                except Category_Ingredient.DoesNotExist:
                    raise GraphQLError(
                        'Category_ingredient matching query does not exist.')
            if filter.get('is_for_market') != None:
                filter_params['is_for_market'] = filter.get('is_for_market') #to do: catch the error possible
            if filter.get('name'):
                try:
                    filter_params['name'] = filter['name']
                except Category_Ingredient.DoesNotExist:
                    raise GraphQLError(
                        'name matching query does not exist.')
            return filter_params

        filter = get_filter(filter) if filter else {}

        return Ingredient.objects.filter(**filter)

    def resolve_ingredient(self, info, id=None):
        if(id):
            return Ingredient.objects.get(pk=id)
        return


class Mutation(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field()
    create_or_delete_ingredient_shopping_list = CreateOrDeleteIngredientShoppingList.Field()
    create_or_delete_ingredient_at_home_user = CreateOrDeleteIngredientAtHomeUser.Field()
