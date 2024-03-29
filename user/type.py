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
            'is_follow_newsletter',
            'is_active',
            'urls_social_media',
            'biographie',
            'is_creator_profil',
            'date_joined',
            'urls_social_media',
            'photo_url',
            'username',
        )
