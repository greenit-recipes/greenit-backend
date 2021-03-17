import graphene
from graphene_django import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'name',
            'image_profile',
            'location',
            'auto_pay',
            'is_staff',
            'is_active',
            'date_joined',
            'dob',
            'liked_recipes',
            'done_recipes',
            'recipes',
        )


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

        return User.objects.filter(**filter)

    def resolve_user(self, info, id):
        try:
            return User.objects.get(pk=id)
        except:
            raise Exception('User does not exist!')
