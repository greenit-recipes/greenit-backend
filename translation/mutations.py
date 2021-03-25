import graphene

from .models import Translation
from .type import TranslationType


class TranslationInput(graphene.InputObjectType):
    is_approved = graphene.Boolean()


class CreateTranslation(graphene.Mutation):
    class Arguments:
        data = TranslationInput(required=True)

    translation = graphene.Field(TranslationType)

    def mutate(root, info, data):
        translation = Translation.objects.create(is_approved=data.is_approved)

        return CreateTranslation(translation=translation)
