import stripe
import requests
from django.conf import settings

stripe.api_key = "sk_test_51OAXHdSFVg6LGnstWx1rKbLogFAh5PQI2VMhFuk9pIa5dr8urI2Ee838SmgFvdqdqW7roUbIVus4ha2A84uHo5pB00Lw6o6Xqp"

# product = stripe.Product.create(
#   name="Basic Dashboard",
#   default_price_data={
#     "unit_amount": 1000,
#     "currency": "usd",
#   },
#   expand=["default_price"],
# )
#
#
# print(product['id'])
#
# my_price = stripe.Price.create(
#             product=product['id'],
#             unit_amount=1000,
#             currency="usd",
#
#         )
#
# print('##########################')
#
# print(my_price['id'])
#
# print('##########################')
#
# print(my_price)


import stripe


checkout_session_id = 'cs_test_a128oRIwB6MRzt5fdESK54z2ZCNVsqyAXfEI9ddFV6ZzTI7bW26HUUeJeD'

checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

print('Payment Status:', checkout_session.payment_status)