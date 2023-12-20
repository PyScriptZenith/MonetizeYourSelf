from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

NULLABLE = {"null": True, "blank": True}
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email", **NULLABLE)
    phone = models.CharField(unique=True, max_length=35, verbose_name="номер телефона")
    city = models.CharField(max_length=70, verbose_name="город", **NULLABLE)
    nick_name = models.CharField(max_length=50, verbose_name='ник', **NULLABLE)


    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []


    def __str__(self):
        return (
            f"{self.phone}: {self.email}"
        )

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"




