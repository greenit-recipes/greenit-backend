from decouple import config
import graphene
import stripe

# env = environ.Env()
# environ.Env.read_env()

stripe.api_key = config('STRIPE_SECRET_KEY')

BASE_URL = f'{config("PROTOCOL")}://{config("DOMAIN_NAME")}'
PRICE_ID = config("PRICE_ID")


# Creates a new checkout session and yields a checkout url
class CreateCheckoutSession(graphene.Mutation):
    class Arguments:
        data = graphene.String()

    # Todo (zack): Create custom object type for response with error handling
    redirect_url = graphene.String()

    # Todo (zack): Impose a rate limit on the API
    def mutate(root, info, data):
        try:

            # Todo (zack) store session parameters in a secure place (env or db)
            checkout_session = stripe.checkout.Session.create(
                customer_creation='always',
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': PRICE_ID,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                # Todo (zack): Assess whether is it safe to expose client ids directly otherwise we will use temp tokens
                success_url=BASE_URL + '/commande-box?step=Confirmation',
                cancel_url=BASE_URL + '/commande-box',
                locale='fr',
                allow_promotion_codes=True,
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
            # stripe.Customer.delete(new_customer.id)
            print('There was an error creating the session', e)
            return CreateCheckoutSession(redirect_url=str(e))


# Get Customer Details By id
class Query(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_checkout_session = CreateCheckoutSession.Field()
