import graphene
import stripe

# This is your test secret API key.
stripe.api_key = 'sk_test_51KxoqiDUYQtfMdf1lZB4QgF9hcTro5xQ5Sp4ZblTy9aMYY3idkXCtDfh4ryqsOMrxK61TZY9zAPY1AeHv0hx6AbP00BF6qbT0a'

YOUR_DOMAIN = 'http://localhost:3000'



class CreateCheckoutSession(graphene.Mutation):
    class Arguments:
        data = graphene.String()

    redirect_url = graphene.String()

    def mutate(root, info, data):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1KxpA8DUYQtfMdf16b44BTOR',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/pages/payment_success',
                cancel_url=YOUR_DOMAIN + '/pages/payment_cancel',
            )
            return CreateCheckoutSession(redirect_url=checkout_session.url)
        except Exception as e:
            print('There was an error creating the session', e)
            return CreateCheckoutSession(redirect_url=str(e))


class Mutation(graphene.ObjectType):
    create_checkout_session = CreateCheckoutSession.Field()
