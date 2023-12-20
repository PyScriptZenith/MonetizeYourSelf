from django.db import models

from monetizeyourself.models import NULLABLE
from users.models import User


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE
    )
    date = models.DateField(verbose_name="дата оплаты", **NULLABLE)
    amount = models.FloatField(verbose_name="сумма оплаты", **NULLABLE)
    is_confirmed = models.BooleanField(
        default=False, verbose_name="подтверждение оплаты"
    )

    def __str__(self):
        return (
            f"{self.user}, {self.amount}: {self.is_confirmed}"
        )

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

        ordering = ("date",)


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь",
        related_name='subsription', **NULLABLE
    )
    is_subscribed = models.BooleanField(default=False, verbose_name='наличие подписки')

    def __str__(self):
        return f"{self.user} : {self.is_subscribed}"

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"

