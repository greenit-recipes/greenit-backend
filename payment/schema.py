import environ
import graphene
import stripe

env = environ.Env()
environ.Env.read_env()

stripe.api_key = env('STRIPE_SECRET_KEY')

BASE_URL = f'{env("PROTOCOL")}://{env("DOMAIN_NAME")}'



class CreateCheckoutSession(graphene.Mutation):
    class Arguments:
        data = graphene.String()

    #Todo (zack): Create custom object type for response with error handling
    redirect_url = graphene.String()

    def mutate(root, info, data):
        try:
            #Todo (zack) store session parameters in a secure place (env or db)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1KxsowDUYQtfMdf1QI7OvksR',
                        'quantity': 1
                    },
                ],
                mode='payment',
                success_url=BASE_URL + '/pages/payment_success',
                cancel_url=BASE_URL + '/pages/payment_cancel',
            )
            return CreateCheckoutSession(redirect_url=checkout_session.url)
        except Exception as e:
            print('There was an error creating the session', e)
            return CreateCheckoutSession(redirect_url=str(e))


class Mutation(graphene.ObjectType):
    create_checkout_session = CreateCheckoutSession.Field()
