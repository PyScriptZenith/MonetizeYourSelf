from django import forms

from monetizeyourself.forms import StyleMixin
from payment.models import Payment


class PaymentForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
