from django.test import SimpleTestCase
from django.urls import resolve, reverse
from monetizeyourself.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    PayedPostListView


class TestPostUrls(SimpleTestCase):

    def test_post_list(self):
        url = reverse('monetizeyourself:post_list')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PostListView)

    def test_post_payed_list(self):
        url = reverse('monetizeyourself:post_payed_list')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PayedPostListView)

    def test_post_detail(self):
        url = reverse('monetizeyourself:post_detail', args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PostDetailView)

    def test_post_create(self):
        url = reverse('monetizeyourself:post_create')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PostCreateView)

    def test_post_update(self):
        url = reverse('monetizeyourself:post_update', args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PostUpdateView)

    def test_post_delete(self):
        url = reverse('monetizeyourself:post_delete', args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PostDeleteView)
