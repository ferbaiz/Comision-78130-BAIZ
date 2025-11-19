from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # App principal Supermercado
    path("", include("supermercado.urls")),

    # Sistema de Mensajería (la app correcta es MENSAJERIA)
    path("mensajeria/", include("mensajeria.urls")),

    # App de Usuarios
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

# Archivos MEDIA en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
