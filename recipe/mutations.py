import graphene

from ingredient.models import Ingredient
from tag.models import Category, Tag
from utensil.models import Utensil
from django.core.mail import EmailMultiAlternatives
from .models import Recipe
from .type import DifficultyFilter, LanguageFilter, RecipeType
from smtplib import SMTPException
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.utils.html import strip_tags
from graphql_jwt.decorators import login_required


class RecipeInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    text_associate = graphene.String()
    video_url = graphene.String()
    duration = graphene.Int()
    tags = graphene.List(graphene.String)
    ingredients = graphene.List(graphene.String)
    utensils = graphene.List(graphene.String)
    expiry = graphene.String()
    notes_from_author = graphene.String()
    category = graphene.List(graphene.String)
    language = LanguageFilter()
    difficulty = DifficultyFilter()
    # instructions
    # image


class CreateRecipe(graphene.Mutation):
    class Arguments:
        data = RecipeInput(required=True)

    recipe = graphene.Field(RecipeType)

    @login_required
    def mutate(root, info, data):
        recipe = Recipe.objects.create(
            name=data.name,
            description=data.description,
            text_associate=data.text_associate,
            video_url=data.video_url,
            duration=data.duration,
            expiry=data.expiry,
            notes_from_author=data.notes_from_author,
            language=data.language,
            difficulty=data.difficulty,
        )
        recipe.tags.set([Tag.objects.get(pk=id) for id in data.tags])
        recipe.ingredients.set(
            [Ingredient.objects.get(pk=id) for id in data.ingredients]
        )
        recipe.utensils.set([Utensil.objects.get(pk=id)
                            for id in data.utensils])
        recipe.category.set([Category.objects.get(pk=data.category)])
        recipe.save()

        return CreateRecipe(recipe=recipe)

class AddOrRemoveLikeRecipe(graphene.Mutation):
    class Arguments:
        recipeId = graphene.String(required=True)

    success = graphene.Boolean()
    
    @login_required
    def mutate(root, info, recipeId):
        print('name -->', recipeId)
        recipe = Recipe.objects.get(id=recipeId)
        user = info.context.user
        try:
            if recipe.likes.filter(id=user.id).exists():
                print("Passe la")
                recipe.likes.remove(user)
            else:
                recipe.likes.add(user)

            return AddOrRemoveLikeRecipe(success= True)
        except Exception as e:
            print(e)
            return AddOrRemoveLikeRecipe(success= False)

class AddOrRemoveFavoriteRecipe(graphene.Mutation):
    class Arguments:
        recipeId = graphene.String(required=True)

    success = graphene.Boolean()
    
    @login_required
    def mutate(root, info, recipeId):
        recipe = Recipe.objects.get(id=recipeId)
        user = info.context.user
        try:
            if recipe.favorites.filter(id=user.id).exists():
                print("Passe la")
                recipe.favorites.remove(user)
            else:
                recipe.favorites.add(user)

            return AddOrRemoveFavoriteRecipe(success= True)
        except Exception as e:
            print(e)
            return AddOrRemoveFavoriteRecipe(success= False)

class SendEmailRecipe(graphene.Mutation):
    
    class Arguments:
        name = graphene.String(required=True)
        userEmail = graphene.String(required=True)
        instructions = graphene.List(graphene.String, required=True)
        expiry = graphene.String(required=True)
        userUsername = graphene.String(required=True)
        userId = graphene.String(required=True)
        description = graphene.String(required=True)
        duration = graphene.Int(required=True)
        tags = graphene.List(graphene.String, required=True)
        ingredients = graphene.List(graphene.String, required=True)
        utensils = graphene.List(graphene.String, required=True)
        notes_from_author = graphene.String(required=True)
        category = graphene.List(graphene.String, required=True)
        difficulty = DifficultyFilter(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(root, info, **kwarg):
        d = {
            'name': kwarg['name'],
            'userEmail': kwarg['userEmail'],
            'userUsername': kwarg['userUsername'],
            'userId': kwarg['userId'],
            'description': kwarg['description'],
            'instructions': kwarg['instructions'],
            'expiry': kwarg['expiry'],
            'duration': kwarg['duration'],
            'tags': kwarg['tags'],
            'ingredients': kwarg['ingredients'],
            'utensils': kwarg['utensils'],
            'notes_from_author': kwarg['notes_from_author'],
            'category': kwarg['category'],
            'difficulty': kwarg['difficulty']
        }
        html_content = get_template('email/create_recette.html').render(
            d
        )
        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(
            "Création de recette", "", from_email="hello@greenitcommunity.com", to=["compiegne92@gmail.com", "andrea.ribeiroo@hotmail.fr"])
        msg.attach_alternative(html_content, "text/html")
        try:
            print('good')
            msg.send()
            return SendEmailRecipe(success=True)
        except Exception as e:
            print('There was an error sending an email: ', e)
            return SendEmailRecipe(success=False)
