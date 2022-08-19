import graphene
from graphql_jwt.decorators import login_required

from .models import Ingredient, IngredientAtHomeUser, IngredientShoppingListUser
from .type import IngredientType


class CreateIngredientInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    # image =


class IngredientIdsInput(graphene.InputObjectType):
    additions = graphene.List(graphene.String)
    deletions = graphene.List(graphene.String)


class CreateIngredient(graphene.Mutation):
    class Arguments:
        data = CreateIngredientInput(required=True)

    ingredient = graphene.Field(IngredientType)

    def mutate(root, info, data):
        ingredient = Ingredient.objects.create(
            name=data.name, description=data.description
        )

        return CreateIngredient(ingredient=ingredient)


class CreateOrDeleteIngredientShoppingList(graphene.Mutation):
    class Arguments:
        ingredientShoppingList = IngredientIdsInput(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(root, info, ingredientShoppingList):
        user = info.context.user
        try:
            if len(ingredientShoppingList.additions) == 1:
                if IngredientShoppingListUser.objects.filter(user_id=user.id,
                                                             ingredient_id=ingredientShoppingList.additions[
                                                                 0]).exists():
                    IngredientShoppingListUser.objects.filter(user_id=user.id,
                                                              ingredient_id=ingredientShoppingList.additions[
                                                                  0]).delete()
                else:
                    IngredientShoppingListUser.objects.create(
                        ingredient_id=ingredientShoppingList.additions[0], user_id=user.id
                    )
            else:
                if len(ingredientShoppingList.deletions) != 0:
                    if len(ingredientShoppingList.deletions) != 0:
                        IngredientShoppingListUser.objects.filter(ingredient__id__in=ingredientShoppingList.deletions,
                                                                  user_id=user.id).delete()

                if len(ingredientShoppingList.additions) != 0:
                    IngredientShoppingListUser.objects.bulk_create(list(
                        IngredientShoppingListUser(ingredient_id=ingredientShoppingList.additions[i], user_id=user.id)
                        for i
                        in
                        range(len(ingredientShoppingList.additions))))

            return CreateOrDeleteIngredientShoppingList(success=True)
        except Exception as e:
            print(e)
            return CreateOrDeleteIngredientShoppingList(success=False)


class CreateOrDeleteIngredientAtHomeUser(graphene.Mutation):
    class Arguments:
        ingredientAtHome = IngredientIdsInput(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(root, info, ingredientAtHome):

        user = info.context.user
        print(ingredientAtHome.additions)
        try:
            if len(ingredientAtHome.additions) == 1:
                if IngredientAtHomeUser.objects.filter(user_id=user.id,
                                                       ingredient_id=ingredientAtHome.additions[0]).exists():
                    IngredientAtHomeUser.objects.filter(user_id=user.id,
                                                        ingredient_id=ingredientAtHome.additions[0]).delete()
                else:
                    IngredientAtHomeUser.objects.create(
                        ingredient_id=ingredientAtHome.additions[0], user_id=user.id
                    )
            else:
                # Todo : Add checks to ids (existant & not found) cases
                if len(ingredientAtHome.deletions) != 0:
                    IngredientAtHomeUser.objects.filter(ingredient__id__in=ingredientAtHome.deletions,
                                                        user_id=user.id).delete()

                if len(ingredientAtHome.additions) != 0:
                    print(ingredientAtHome.additions)
                    IngredientAtHomeUser.objects.bulk_create(list(
                        IngredientAtHomeUser(ingredient_id=ingredientAtHome.additions[i], user_id=user.id) for i
                        in
                        range(len(ingredientAtHome.additions))))

            return CreateOrDeleteIngredientAtHomeUser(success=True)
        except Exception as e:
            print(e)
            return CreateOrDeleteIngredientAtHomeUser(success=False)
