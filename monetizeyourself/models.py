from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец публикации', **NULLABLE)
    header = models.CharField(max_length=100, verbose_name='заголовок', **NULLABLE)
    text = models.TextField(verbose_name='текст', **NULLABLE)
    image = models.ImageField(
        upload_to="images/", verbose_name="изображение", **NULLABLE
    )
    is_free = models.BooleanField(default=True, verbose_name='бесплатная', **NULLABLE)
    published_date = models.DateField(verbose_name='дата публикации', **NULLABLE)

    def __str__(self):
        return (
            f"{self.owner}, {self.header}: {self.is_free}"
        )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "публикации"




