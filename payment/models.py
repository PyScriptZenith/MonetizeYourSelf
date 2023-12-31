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
    stripe_session_id = models.TextField(verbose_name='id платежной сессии', **NULLABLE)

    def __str__(self):
        return (
            f"Пользователь -  {self.user},\n"
            f"Сумма оплаты - {self.amount} \n"
            f"Оплата подтверждена - {self.is_confirmed} \n"
            f"id сессии stripe {self.stripe_session_id} \n"
        )

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

        ordering = ("date",)



