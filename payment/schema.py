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

    # Todo (zack): Create custom object type for response with error handling
    redirect_url = graphene.String()

    def mutate(root, info, data):
        try:
            # Todo (zack) store session parameters in a secure place (env or db)
            checkout_session = stripe.checkout.Session.create(
                customer_creation='always',
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1KxsowDUYQtfMdf1QI7OvksR',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=BASE_URL + '/pages/payment_success',
                cancel_url=BASE_URL + '/pages/payment_cancel',
                locale='fr',
                # Shipping details
                phone_number_collection={
                    'enabled': True,
                },
                shipping_address_collection={
                    'allowed_countries': ['FR'],
                },
                shipping_options=[
                    {
                        'shipping_rate_data': {
                            'type': 'fixed_amount',
                            'fixed_amount': {
                                'amount': 500,
                                'currency': 'eur',
                            },
                            'display_name': 'Greenit super delivery',
                            # Delivers in exactly 1 business day
                            'delivery_estimate': {
                                'minimum': {
                                    'unit': 'business_day',
                                    'value': 5,
                                },
                                'maximum': {
                                    'unit': 'business_day',
                                    'value': 7,
                                },
                            }
                        }
                    }
                ]
            )
            return CreateCheckoutSession(redirect_url=checkout_session.url)
        except Exception as e:
            # Todo (zack) investigate whether stripe session errors are safe
            # to be relayed directly to the web app
            print('There was an error creating the session', e)
            return CreateCheckoutSession(redirect_url=str(e))


class Mutation(graphene.ObjectType):
    create_checkout_session = CreateCheckoutSession.Field()
