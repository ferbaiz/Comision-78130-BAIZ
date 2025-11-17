from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # App principal
    path("", include("supermercado.urls")),

    # Sistema de mensajes internos
    path("mensajes/", include("mensajes.urls")),

    # App de usuarios
    path("accounts/", include("accounts.urls")),

    # Login / Logout con plantillas personalizadas
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login"
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(next_page="/"),
        name="logout"
    ),
]

# Archivos media (solo en debug)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
