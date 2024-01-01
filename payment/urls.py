from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentIndex, PaymentCreateView, SuccessView, CancelView

app_name = PaymentConfig.name


urlpatterns = [
    path("", PaymentIndex.as_view(), name="payment"),
    path("create_payment/", PaymentCreateView.as_view(), name="payment_create"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
]
