import graphene
from graphql_jwt.decorators import login_required

from .models import Ingredient, IngredientAtHomeUser, IngredientShoppingListUser
from .type import IngredientType


class CreateIngredientInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    # image =

class CreateIngredient(graphene.Mutation):
    class Arguments:
        data = CreateIngredientInput(required=True)

    ingredient = graphene.Field(IngredientType)

    def mutate(root, info, data):
        ingredient = Ingredient.objects.create(
            name=data.name, description=data.description
        )

        return CreateIngredient(ingredient=ingredient)



class CreateIngredientShoppingList(graphene.Mutation):
    class Arguments:
        ingredientId = graphene.String(required=True)

    success = graphene.Boolean()
    
    @login_required
    def mutate(root, info, ingredientId):
        user = info.context.user
        try:
            if IngredientShoppingListUser.objects.filter(user_id=user.id, ingredient_id=ingredientId).exists():
                IngredientShoppingListUser.objects.filter(user_id=user.id, ingredient_id=ingredientId).delete()
            else:
                IngredientShoppingListUser.objects.create(
                    ingredient_id=ingredientId, user_id=user.id
                )

            return CreateIngredientShoppingList(success= True)
        except Exception as e:
            print(e)
            return CreateIngredientShoppingList(success= False)      

class CreateIngredientAtHomeUser(graphene.Mutation):
    class Arguments:
        ingredientId = graphene.String(required=True)

    success = graphene.Boolean()
    
    @login_required
    def mutate(root, info, ingredientId):
        user = info.context.user
        try:
            if IngredientAtHomeUser.objects.filter(user_id=user.id, ingredient_id=ingredientId).exists():
                IngredientAtHomeUser.objects.filter(user_id=user.id, ingredient_id=ingredientId).delete()
            else:
                IngredientAtHomeUser.objects.create(
                    ingredient_id=ingredientId, user_id=user.id
                )

            return CreateIngredientAtHomeUser(success= True)
        except Exception as e:
            print(e)
            return CreateIngredientAtHomeUser(success= False)      
