import stripe
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.views import View
from payment.forms import PaymentForm
from payment.models import Payment
from django.conf import settings
from django.http import JsonResponse

# Create your views here.

class PaymentIndex(TemplateView):
    template_name = 'payment/payment.html'


class SuccessView(TemplateView):
    template_name = 'payment/success.html'

class CancelView(TemplateView):
    template_name = 'payment/cancel.html'


stripe.api_key = settings.STRIPE_API_KEY
class PaymentCreateView(View):

    CHECK_PAY = None
    def post(self, request, *args, **kwargs):

        product = stripe.Product.create(
            name="Бессрочная подписка MonetizeYourSelf",
            default_price_data={
                "unit_amount": 1000000,
                "currency": "rub",

            },
            expand=["default_price"],
        )

        my_price = stripe.Price.create(
            product=product['id'],
            unit_amount=1000000,
            currency="rub",

        )

        YOUR_DOMAIN = 'http://127.0.0.1:8000/'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': my_price['id'],
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/payment/success/',
            cancel_url='http://127.0.0.1:8000/payment/cancel/',
        )



        checkout_session_id = checkout_session["id"]

        user_data = self.request.user

        print(user_data.id)
        print(user_data.pk)

        Payment.objects.create(user=user_data,
                               stripe_session_id=checkout_session_id)



        return redirect(checkout_session.url, code=303)

