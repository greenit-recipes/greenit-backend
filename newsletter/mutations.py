import graphene

from .models import NewsLetter

class NewsletterInput(graphene.InputObjectType):
    email = graphene.String()

class CreateNewsletter(graphene.Mutation):
    class Arguments:
        data = NewsletterInput(required=True)

    success = graphene.Boolean()

    def mutate(root, info, data):
        try:
            NewsLetter.objects.create(email=data.email)
            return CreateNewsletter(success=True)
        except Exception as e:
            print('There was an error by adding email to newsletter: ', e)
            return CreateNewsletter(success=False)