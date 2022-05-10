import graphene

from .models import User
from .type import UserType
from graphql_auth import mutations
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required
from django.core.mail import EmailMessage
from django.core import serializers
from django.db import connection

class CreateUserFromAuth(graphene.Mutation):
    
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password =  graphene.String(required=True)
        id_facebook = graphene.String()
        is_follow_newsletter =  graphene.String()
    
    isUserAlreadyCreated = graphene.Boolean()
    errors = graphene.String()

    def mutate(root, info, email, username, password, id_facebook, is_follow_newsletter):
      try:
          # SI email existe déjà dans les users --> dire que l'email existe déjà
          if User.objects.filter(id_facebook=id_facebook).exists():
              return CreateUserFromAuth(isUserAlreadyCreated=True)
          if User.objects.filter(email=email).exists():
             return CreateUserFromAuth(errors="L’e-mail est déjà attribué à un compte.")
          
          if User.objects.filter(username=username).exists():
             return CreateUserFromAuth(errors="Le nom d'utilisateur est déjà attribué à un compte.")
              
          else:
              currentUserCreateByAuth = User(email = email, username = username, password = password, id_facebook = id_facebook, photo_url = "https://graph.facebook.com/{0}/picture".format(id_facebook))
              currentUserCreateByAuth.set_password(password)
              currentUserCreateByAuth.save()
              cursor = connection.cursor()
              cursor.execute("UPDATE graphql_auth_userstatus SET verified = True WHERE user_id = '{0}'".format(currentUserCreateByAuth.id))
              return CreateUserFromAuth(isUserAlreadyCreated=False)
              
      except Exception as e:
          raise Exception(e)
          print(e)


class UpdateImageAccount(graphene.Mutation):

    class Arguments:
        imageProfile = Upload(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(root, info, imageProfile):
      try:
          user = info.context.user
          userImage = User.objects.get(id=user.id)
          userImage.image_profile=imageProfile[0]
          userImage.save()
          return UpdateImageAccount(success=True)

      except Exception as e:
          print(e)
          return UpdateImageAccount(success=False)


class EmailWelcomeNewUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(root, info, email):
      try:
          message = EmailMessage(
              to=[email]
          )
          message.merge_global_data = {
              'EMAIL_TO': email,
          }
          message.template_id = "3350964"  # Mailjet numeric template id
          message.send()

          return EmailWelcomeNewUser(success=True)

      except Exception as e:
          print(e)
          return EmailWelcomeNewUser(success=False)
      
class EmailSharedWithFriend(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(root, info, email):
      try:
          message = EmailMessage(
              to=[email]
          )
          message.template_id = "3625816"  # Mailjet numeric template id
          message.send()

          return EmailSharedWithFriend(success=True)

      except Exception as e:
          print(e)
          return EmailSharedWithFriend(success=False)      


class EmailAskQuestionStarterPage(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        question = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(root, info, email, question):
      try:
          message = EmailMessage(
          from_email="hello@greenitcommunity.com",
          to=["hello@greenitcommunity.com"],
          subject="Une personne à posé une question sur la page starter page",  # subject doesn't support on-the-fly merge fields
            # Use [[var:FIELD]] to for on-the-fly merge into plaintext or html body:
          body="Email: [[var:email]]: \nQuestion: [[var:question]]"

          )

          message.merge_global_data = {
                'email': email,
                'question': question,
          }
          message.send()

          return EmailAskQuestionStarterPage(success=True)

      except Exception as e:
          print(e)
          return EmailAskQuestionStarterPage(success=False)      
      
class EmailProfilPage(graphene.Mutation):
    class Arguments:
        question = graphene.String(required=True)

    success = graphene.Boolean()
    
    @login_required
    def mutate(root, info, question):
      try:
          userEmail = info.context.user.email
          print(userEmail)
          print(question)
          message = EmailMessage(
          from_email="hello@greenitcommunity.com",
          to=["hello@greenitcommunity.com"],
          subject="CREATEUR profil page --> Une personne à posé une question",  # subject doesn't support on-the-fly merge fields
            # Use [[var:FIELD]] to for on-the-fly merge into plaintext or html body:
          body="Email: [[var:email]]: \nQuestion: [[var:question]]"
          )

          message.merge_global_data = {
                'email': userEmail,
                'question': question,
          }
          message.send()

          return EmailProfilPage(success=True)

      except Exception as e:
          print(e)
          return EmailProfilPage(success=False)            
      
class EmailHeadband(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(root, info, email):
      try:
          message = EmailMessage(
          from_email="hello@greenitcommunity.com",
          to=["hello@greenitcommunity.com"],
          subject="Pré-commande BOX",  # subject doesn't support on-the-fly merge fields
            # Use [[var:FIELD]] to for on-the-fly merge into plaintext or html body:
          body="Email: [[var:email]]"

          )

          message.merge_global_data = {
                'email': email,
          }
          message.send()

          return EmailHeadband(success=True)

      except Exception as e:
          print(e)
          return EmailHeadband(success=False)         