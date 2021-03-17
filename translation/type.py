from graphene_django import DjangoObjectType

from .models import Translation


class TranslationType(DjangoObjectType):
    class Meta:
        model = Translation
        fields = ('id', 'language', 'author', 'is_approved')
