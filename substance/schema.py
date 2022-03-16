import graphene
from graphql import GraphQLError


from .models import Substance
from .type import SubstanceType

class Query(graphene.ObjectType):
    all_substance = graphene.List(SubstanceType)
    tag = graphene.Field(SubstanceType, id=graphene.String(required=True))

    def resolve_substance(self, info, id):
        return Substance.objects.get(pk=id)

    def resolve_all_substances(self, info, **kwargs):
        return Substance.objects.all()

class Mutation(graphene.ObjectType):
    pass 