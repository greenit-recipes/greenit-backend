# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_51KxoqiDUYQtfMdf1lZB4QgF9hcTro5xQ5Sp4ZblTy9aMYY3idkXCtDfh4ryqsOMrxK61TZY9zAPY1AeHv0hx6AbP00BF6qbT0a"

price = stripe.Price.create(
  currency="euro",
  unit_amount=20,
  product_data={"name": "Greenit FullXP Box"},
)

print(str(price))