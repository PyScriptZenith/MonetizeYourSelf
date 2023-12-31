
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path("admin/", admin.site.urls),
               path("", include("monetizeyourself.urls", namespace="monetizeyourself")),
               path("users/", include("users.urls", namespace="users")),
               path("payment/", include("payment.urls", namespace="payment"))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)