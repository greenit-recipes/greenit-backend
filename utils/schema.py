import graphene
import requests
from django.conf import settings
from django.core.mail import send_mail


class SendMessageInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()
    message = graphene.String()
    token = graphene.String()


class SendMessage(graphene.Mutation):
    class Arguments:
        data = SendMessageInput(required=True)

    ok = graphene.Boolean()
    message = graphene.String(required=False)

    def mutate(root, info, data):
        r = requests.post(
            f'https://hcaptcha.com/siteverify',
            data={
                "response": data['token'],
                "secret": settings.CAPTCHA_SECRET_KEY,
            },
        )
        if r.json()['success']:
            try:
                send_mail(
                    f'New Message from {data["name"]}',
                    data['message'],
                    data['email'],
                    ['hellogreenit@gmail.com', data['email']],
                    fail_silently=False,
                )
                return SendMessage(ok=True)
            except:
                # log here
                return SendMessage(ok=False, message="Internal Error")
        return SendMessage(ok=False, message="Invalid Captcha")


class Mutation(graphene.ObjectType):
    send_message = SendMessage.Field()
