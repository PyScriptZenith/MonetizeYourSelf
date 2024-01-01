from django.test import SimpleTestCase
from django.urls import resolve, reverse

from payment.views import PaymentCreateView, SuccessView, CancelView


class TestPaymentUrls(SimpleTestCase):
    def test_payment_create(self):
        url = reverse("payment:payment_create")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PaymentCreateView)

    def test_payment_success(self):
        url = reverse("payment:success")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, SuccessView)

    def test_payment_cancel(self):
        url = reverse("payment:cancel")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CancelView)
