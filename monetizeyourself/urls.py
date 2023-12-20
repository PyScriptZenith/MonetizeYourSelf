from django.urls import path

from monetizeyourself.apps import MonetizeyourselfConfig
from monetizeyourself.views import IndexView, PostCreateView, PostDetailView

app_name = MonetizeyourselfConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create')
    ]