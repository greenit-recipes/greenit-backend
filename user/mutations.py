import graphene

from .models import User
from .type import UserType


class UserInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()
    location = graphene.String()
    dob = graphene.Date()
    # image_profile


class CreateUser(graphene.Mutation):
    class Arguments:
        data = UserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, data):
        user = User.objects.create(
            name=data.name, email=data.email, location=data.location, dob=data.dob
        )

        return CreateUser(user=user)
