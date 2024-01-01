from django.test import TestCase, Client
from django.urls import reverse

from payment.models import Payment
from users.models import User


class TestPaymentViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            email="test@test.com", phone=89139130505, city="Moscow", nick_name="Max77"
        )
        self.client.force_login(self.user)
        self.create_url = reverse("payment:payment_create")
        self.payment_1 = Payment.objects.create(
            user=self.user,
            amount=1055.221,
            is_confirmed=False,
            stripe_session_id="test12345",
        )

    def test_payment_create(self):
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Payment.objects.all().count(), 2)
