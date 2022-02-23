import graphene

from .models import User
from .type import UserType
from graphql_auth import mutations
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required
from django.core.mail import EmailMessage


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field()  # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class CreateUser(AuthMutation):
    pass


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
          print(email)
          print(question)
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