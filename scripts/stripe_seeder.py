import environ
import stripe

env = environ.Env()
environ.Env.read_env()
stripe.api_key = env('STRIPE_SECRET_KEY')

# Create a new product
price = stripe.Price.create(
    currency="eur",
    unit_amount=2000,  # Amount in cents
    product_data={"name": "Greenit FullXP Box"},
)

print(str(price))
