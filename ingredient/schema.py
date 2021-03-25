import graphene

from ingredient.mutations import CreateIngredient
from tag.models import Tag

from .models import Ingredient
from .type import IngredientType


class IngredientFilterInput(graphene.InputObjectType):
    tag = graphene.String(required=False)


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(
        IngredientType, filter=IngredientFilterInput(required=False)
    )
    ingredient = graphene.Field(IngredientType, id=graphene.String(required=True))

    def resolve_all_ingredients(self, info, filter=None, **kwargs):
        def get_filter(filter):
            filter_params = {}
            if filter.get('tag'):
                try:
                    tag = Tag.objects.get(pk=filter.get('tag'))
                    filter_params['tags'] = tag
                except Tag.DoesNotExist:
                    raise Exception('Tag does not exist!')
            return filter_params

        filter = get_filter(filter) if filter else {}

        return Ingredient.objects.filter(**filter)

    def resolve_ingredient(self, info, id):
        try:
            return Ingredient.objects.get(pk=id)
        except:
            raise Exception('Ingredient does not exist!')


class Mutation(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field()
