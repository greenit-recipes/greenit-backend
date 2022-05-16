import graphene
from graphql_auth.schema import UserQuery, MeQuery

from graphql_auth import mutations

from user.mutations import EmailWelcomeNewUser, UpdateImageAccount, CreateUserFromAuth, EmailSharedWithFriend, EmailAskQuestionStarterPage, EmailProfilPage, EmailGreenitFullXp, EmailHeadband, HasPurchasedBeginnerBox


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()
    
    # update image account
    update_image_account = UpdateImageAccount.Field()
    
    # email
    email_welcome_new_user = EmailWelcomeNewUser.Field()
    email_shared_with_friend = EmailSharedWithFriend.Field()
    email_ask_question_starte_page = EmailAskQuestionStarterPage.Field()
    email_profil_page = EmailProfilPage.Field()
    email_headband = EmailHeadband.Field()
    email_greenit_full_xp = EmailGreenitFullXp.Field()

    # Box Full Xp
    has_purchased_beginner_box = HasPurchasedBeginnerBox.Field()
    
    #auth
    create_user_from_auth = CreateUserFromAuth.Field()

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
   pass
