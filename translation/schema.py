import graphene
from graphql import GraphQLError

from translation.mutations import CreateTranslation

from .models import Translation
from .type import TranslationType


class Query(graphene.ObjectType):
    all_translations = graphene.List(TranslationType)
    translation = graphene.Field(TranslationType, id=graphene.String(required=True))

    def resolve_all_translations(self, info, **kwargs):
        return Translation.objects.all()

    def resolve_translation(self, info, id):
        return Translation.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_translation = CreateTranslation.Field()
