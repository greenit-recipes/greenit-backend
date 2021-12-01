import graphene

from newsletter.mutations import CreateNewsletter

class Mutation(graphene.ObjectType):
    create_newsletter = CreateNewsletter.Field()
