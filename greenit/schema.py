import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

import ingredient.schema
import recipe.schema
import tag.schema
import translation.schema
import user.schema
import utensil.schema
import utils.schema


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Query(
    ingredient.schema.Query,
    recipe.schema.Query,
    tag.schema.Query,
    translation.schema.Query,
    user.schema.Query,
    utensil.schema.Query,
    UserQuery,
    MeQuery,
    graphene.ObjectType,
):
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(
    ingredient.schema.Mutation,
    recipe.schema.Mutation,
    tag.schema.Mutation,
    translation.schema.Mutation,
    user.schema.Mutation,
    utensil.schema.Mutation,
    utils.schema.Mutation,
    AuthMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
