import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from monetizeyourself.models import Post
import json

from payment.models import Payment
from users.models import User


class TestPostViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('monetizeyourself:post_list')
        self.payed_list_url = reverse('monetizeyourself:post_payed_list')
        self.detail_url = reverse('monetizeyourself:post_detail', args=[1])
        self.delete_url = reverse('monetizeyourself:post_delete', args=[1])
        self.create_url = reverse('monetizeyourself:post_create')

        image_path = 'monetizeyourself/tests/test_image.jpg'
        with open(image_path, 'rb') as image_file:
            image = SimpleUploadedFile(image_path, image_file.read(), content_type='image/jpeg')

        self.user = User.objects.create(
            email='user@user.com',
            phone='000001111111',
            city='Spb',
            nick_name='Opa',
            password='testpass'
        )
        self.payed_post = Post.objects.create(
            owner=self.user,
            header='payable_header',
            text='pay,pay,pay',
            image=image,
            is_free=False,
            published_date=datetime.date.today()
        )

        self.payment = Payment.objects.create(
            user=self.user,
            date=datetime.date.today(),
            amount=10000,
            is_confirmed=True,
            stripe_session_id='cs_test_a128oRIwB6MRzt5fdESK54z2ZCNVsqyAXfEI9ddFV6ZzTI7bW26HUUeJeD'
        )
        self.client.force_login(self.user)

    def test_post_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monetizeyourself/post_list.html')

    def test_post_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monetizeyourself/post_detail.html')

    def test_post_delete(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)

    def test_post_create(self):
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.all().count(), 2)
        self.assertEqual(self.payed_post.header, 'payable_header')

    def test_payed_post_list(self):
        response = self.client.get(self.payed_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monetizeyourself/payed_post_list.html')









