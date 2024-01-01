from django.urls import path

from monetizeyourself.apps import MonetizeyourselfConfig
from monetizeyourself.views import (
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostListView,
    PostDeleteView,
    PayedPostListView,
)

app_name = MonetizeyourselfConfig.name


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("payed/", PayedPostListView.as_view(), name="post_payed_list"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
