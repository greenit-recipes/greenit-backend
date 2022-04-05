import graphene

from ingredient.models import Ingredient
from tag.models import Category, Tag
from utensil.models import Utensil
from django.core.mail import EmailMultiAlternatives

from utils.validator import file_size_image, file_size_video
from utils.file import getFilePathForUpload
from .models import Made, Recipe
from .type import DifficultyFilter, LanguageFilter, RecipeType
from smtplib import SMTPException
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.utils.html import strip_tags
from graphql_jwt.decorators import login_required
import boto3
from botocore.exceptions import NoCredentialsError
import os
import io
from graphene_file_upload.scalars import Upload
from django.core import serializers

from django.conf import settings
from django.core.mail import EmailMessage
import asyncio

async def upload_to_aws(local_file, s3_file, username):
    s3 = boto3.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    try:
        await s3.upload_fileobj(local_file.file, os.getenv('AWS_STORAGE_BUCKET_NAME'), settings.PUBLIC_MEDIA_LOCATION + "/" + getFilePathForUpload(username, 'recipe', s3_file), ExtraArgs={'ACL':'public-read'})
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except Exception as e:
        print("e", e)
        return False

class RecipeInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    text_associate = graphene.String()
    video_url = graphene.String()
    video = graphene.String()
    image = graphene.String()
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
        recipe = Recipe.objects.get(id=recipeId)
        user = info.context.user
        try:
            if recipe.likes.filter(id=user.id).exists():
                recipe.likes.remove(user)
            else:
                recipe.likes.add(user)

            return AddOrRemoveLikeRecipe(success= True)
        except Exception as e:
            print(e)
            return AddOrRemoveLikeRecipe(success= False)
        
class AddOrRemoveMadeRecipe(graphene.Mutation):
    class Arguments:
        recipeId = graphene.String(required=True)

    success = graphene.Boolean()
    
    @login_required
    def mutate(root, info, recipeId):
        user = info.context.user
        made = Made.objects.filter(user_id=user.id, recipe_id=recipeId)
        try:
            if made.exists():
               Made.objects.get(user_id=user.id, recipe_id=recipeId).delete()
            else:
               Made.objects.create(
                   amount=1,
                   recipe_id= recipeId,
                   user_id= user.id
               )

            return AddOrRemoveMadeRecipe(success= True)
        except Exception as e:
            print(e)
            return AddOrRemoveMadeRecipe(success= False)        

class AddViewRecipe(graphene.Mutation):
    class Arguments:
        recipeId = graphene.String(required=True)

    success = graphene.Boolean()
    
    def mutate(root, info, recipeId):
        recipe = Recipe.objects.get(id=recipeId)
        try:
            recipe.nbr_view += 1
            recipe.save()
            return AddViewRecipe(success=True)
        except Exception as e:
            print(e)
            return AddViewRecipe(success=False)        

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
        image = Upload(required=False)
        #video = Upload(required=False)
        tags = graphene.List(graphene.String, required=True)
        ingredients = graphene.List(graphene.String, required=True)
        utensils = graphene.List(graphene.String, required=True)
        notes_from_author = graphene.String(required=False)
        category = graphene.List(graphene.String, required=True)
        difficulty = DifficultyFilter(required=True)
        textAssociate = graphene.String(required=False)
        videoUrl = graphene.String(required=False)

    success = graphene.Boolean()

    @login_required
    def mutate(root, info, **kwargs):
        image = ""
        #video = ""
        if len(kwargs['image']) > 0:
            file_size_image(kwargs['image'][0])
            upload_to_aws(kwargs['image'][0], kwargs['image'][0].name, kwargs['userUsername'])
            image = os.getenv('AWS_URL_NAME') + getFilePathForUpload(kwargs['userUsername'], 'recipe', kwargs['image'][0].name)
            
        #if len(kwargs['video']) > 0:
        #    file_size_video(kwargs['video'][0])
        #    upload_to_aws(kwargs['video'][0], kwargs['video'][0].name, kwargs['userUsername'])  
        #    video = os.getenv('AWS_URL_NAME') + getFilePathForUpload(kwargs['userUsername'], 'recipe', kwargs['video'][0].name)        
        d = {
            'name': kwargs['name'],
            'userEmail': kwargs['userEmail'],
            'userUsername': kwargs['userUsername'],
            'userId': kwargs['userId'],
            'image': image,
            #'video': video,
            'description': kwargs['description'],
            'instructions': kwargs['instructions'],
            'videoUrl': kwargs['videoUrl'],
            'expiry': kwargs['expiry'],
            'duration': kwargs['duration'],
            'tags': kwargs['tags'],
            'ingredients': kwargs['ingredients'],
            'utensils': kwargs['utensils'],
            'notes_from_author': kwargs['notes_from_author'],
            'category': kwargs['category'],
            'difficulty': kwargs['difficulty'],
            'textAssociate': kwargs['textAssociate']
        }
        html_content = get_template('email/create_recette.html').render(
            d
        )
        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(
            "Création de recette", "", from_email="hello@greenitcommunity.com", to=["hello@greenitcommunity.com"])
        msg.attach_alternative(html_content, "text/html")
        try:
            msg.send()
            return SendEmailRecipe(success=True)
        except Exception as e:
            print('There was an error sending an email: ', e)
            return SendEmailRecipe(success=False)

class EmailLinkSharedRecipe(graphene.Mutation):
    class Arguments:
        link = graphene.String(required=True)

    success = graphene.Boolean()
    
    def mutate(root, info, link):
      user = getattr(info.context, 'user', '-')
      try:
          emailUser = getattr(user, 'email', '-')  or "-"
          message = EmailMessage(
          from_email = "hello@greenitcommunity.com",
          to=["hello@greenitcommunity.com"],
          subject="Lien d'une recette à récupérer de: " + emailUser,
          body="Email: [[var:email]]: \nLien: [[var:link]]")

          message.merge_global_data = {
                'email': emailUser,
                'link': link,
          }
          message.send()

          return EmailLinkSharedRecipe(success=True)

      except Exception as e:
          print(e)
          return EmailLinkSharedRecipe(success=False)      