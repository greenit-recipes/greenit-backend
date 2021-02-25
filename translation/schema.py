import graphene
from graphene_django import DjangoObjectType

from .models import Translation


class TranslationType(DjangoObjectType):
    class Meta:
        model = Translation
        fields = ('id', 'language', 'author', 'is_approved')


class Query(graphene.ObjectType):
    translations = graphene.List(TranslationType)

    def resolve_translations(self, info, **kwargs):
        return Translation.objects.all()
