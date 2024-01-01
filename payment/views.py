import stripe
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View
from payment.models import Payment
from django.conf import settings


class PaymentIndex(TemplateView):

    """Страница приобретения подписки"""

    template_name = "payment/payment.html"


class SuccessView(TemplateView):

    """Успешная оплата"""

    template_name = "payment/success.html"


class CancelView(TemplateView):

    """Оплата не произведена"""

    template_name = "payment/cancel.html"


stripe.api_key = settings.STRIPE_API_KEY


class PaymentCreateView(View):
    def post(self, request, *args, **kwargs):
        # Создаем подписку как объект платежа Stripe

        product = stripe.Product.create(
            # Данные для отображения на странице оплаты
            name="Бессрочная подписка MonetizeYourSelf",
            default_price_data={
                "unit_amount": 1000000,
                "currency": "rub",
            },
            expand=["default_price"],
        )

        # Формируем цену подписки

        my_price = stripe.Price.create(
            product=product["id"],
            unit_amount=1000000,
            currency="rub",
        )

        # Создаем сессию оплаты подписки

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": my_price["id"],
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="http://127.0.0.1:8000/payment/success/",
            cancel_url="http://127.0.0.1:8000/payment/cancel/",
        )

        checkout_session_id = checkout_session["id"]

        user_data = self.request.user

        # Записываем данные об оплате в БД

        Payment.objects.create(user=user_data, stripe_session_id=checkout_session_id)

        # Перенаправляем пользователя на страницу со статусом платежа

        return redirect(checkout_session.url, code=303)
