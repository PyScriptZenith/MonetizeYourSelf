# Generated by Django 4.2.4 on 2024-01-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("header", models.CharField(max_length=100, verbose_name="заголовок")),
                ("text", models.TextField(verbose_name="текст")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "is_free",
                    models.BooleanField(default=True, verbose_name="бесплатная"),
                ),
                (
                    "published_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата публикации"
                    ),
                ),
            ],
            options={
                "verbose_name": "публикация",
                "verbose_name_plural": "публикации",
            },
        ),
    ]
