from django.urls import path

from monetizeyourself.apps import MonetizeyourselfConfig
from monetizeyourself.views import PostCreateView, PostDetailView, PostUpdateView, PostListView

app_name = MonetizeyourselfConfig.name


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    # path('', IndexView.as_view(), name='index'),
    # path('', index, name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update')
    ]