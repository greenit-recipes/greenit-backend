import graphene
import ingredient.schema

class Query(ingredient.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
