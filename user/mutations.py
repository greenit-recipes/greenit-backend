import graphene

from .models import User
from .type import UserType

class UserInput(graphene.InputObjectType):
    name = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        data = UserInput(required=True)

    Output = UserType

    def mutate(root, info, data):
        return User.objects.create(name=data.name)
