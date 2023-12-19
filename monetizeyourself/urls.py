from django.urls import path

from monetizeyourself.apps import MonetizeyourselfConfig
from monetizeyourself.views import IndexView

app_name = MonetizeyourselfConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index')
    ]