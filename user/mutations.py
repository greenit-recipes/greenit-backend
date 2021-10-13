import graphene
from .models import User
from .type import UserType


class UserInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String(required=True)
    location = graphene.String()
    dob = graphene.Date()
    password = graphene.String(required=True)
    # image_profile


class CreateUser(graphene.Mutation):
    class Arguments:
        data = UserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, data):
        user = CustomUserobjects.create(
            name=data.name,
            email=data.email,
            location=data.location,
            dob=data.dob,
            password=data.password,
        )

        return CreateUser(user=user)
