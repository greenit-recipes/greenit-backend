import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

import ingredient.schema
import recipe.schema
import tag.schema
import translation.schema
import user.schema
import utensil.schema
import utils.schema
import substance.schema
import newsletter.schema
import comment.schema
from graphql_auth.schema import UserQuery, MeQuery


class Query(
    ingredient.schema.Query,
    recipe.schema.Query,
    substance.schema.Query,
    tag.schema.Query,
    translation.schema.Query,
    user.schema.Query,
    utensil.schema.Query,
    comment.schema.Query,
    graphene.ObjectType,
):
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(
    ingredient.schema.Mutation,
    recipe.schema.Mutation,
    tag.schema.Mutation,
    substance.schema.Mutation,
    translation.schema.Mutation,
    user.schema.Mutation,
    utensil.schema.Mutation,
    newsletter.schema.Mutation,
    comment.schema.Mutation,
    utils.schema.Mutation,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
