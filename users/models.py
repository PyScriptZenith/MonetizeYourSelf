from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

NULLABLE = {"null": True, "blank": True}



# Валидация номера телефона

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Введите действительный номер телефона."
)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email", **NULLABLE)
    phone = models.CharField(
        unique=True,
        max_length=35,
        verbose_name="номер телефона",
        validators=[phone_validator]
    )
    city = models.CharField(max_length=70, verbose_name="город", **NULLABLE)
    nick_name = models.CharField(max_length=50, verbose_name="ник", **NULLABLE)


    # Основное поле при регистрации - номер телефона

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.phone}: {self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
