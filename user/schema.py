import graphene
import graphql_jwt
from graphql import GraphQLError

#from user.mutations import CreateUser

from .models import User
from .type import UserType


class UserFilterInput(graphene.InputObjectType):
    name = graphene.String(required=False)


class Query(graphene.ObjectType):

    all_users = graphene.List(UserType, filter=UserFilterInput(required=False))
    user = graphene.Field(UserType, id=graphene.String(required=True))

    def resolve_all_users(self, info, filter=None, **kwargs):
        def get_filter(filter):
            filter_params = {}
            if filter.get('name'):
                filter_params['name'] = filter['name']
            return filter_params

        filter = get_filter(filter) if filter else {}

        return CustomUserobjects.filter(**filter)

    def resolve_user(self, info, id):
        return CustomUserobjects.get(pk=id)


class Mutation(graphene.ObjectType):
    pass
