import graphene

import ingredient.schema
import recipe.schema
import tag.schema
import translation.schema
import user.schema
import utensil.schema


class Query(
    ingredient.schema.Query,
    recipe.schema.Query,
    tag.schema.Query,
    translation.schema.Query,
    user.schema.Query,
    utensil.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    ingredient.schema.Mutation,
    recipe.schema.Mutation,
    tag.schema.Mutation,
    translation.schema.Mutation,
    user.schema.Mutation,
    utensil.schema.Mutation,
    ):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
