from django.test import SimpleTestCase
from django.urls import resolve, reverse

from payment.views import PaymentCreateView, SuccessView, CancelView
from users.views import UserUpdateView, RegisterView, LogoutView


class TestUsersUrls(SimpleTestCase):

    def test_user_profile(self):
        url = reverse('users:profile', args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, UserUpdateView)

    def test_user_register(self):
        url = reverse('users:register')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, RegisterView)

    def test_user_logout(self):
        url = reverse('users:logout')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, LogoutView)

