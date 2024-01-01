from django.contrib import admin

from monetizeyourself.models import Post


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "header",
        "text",
        "image",
        "is_free",
        "published_date",
    )
