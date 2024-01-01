from django.contrib import admin

from payment.models import Payment


# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date",
        "amount",
        "is_confirmed",
        "stripe_session_id",
    )
