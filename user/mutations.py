import graphene

from .models import User
from .type import UserType
from graphql_auth import mutations


class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
       
class CreateUser(AuthMutation):
    pass
