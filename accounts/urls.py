from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    # Login con vista de Django + template propio
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login"
    ),

    # Logout usando vista personalizada (correcto)
    path("logout/", views.logout_view, name="logout"),

    # Registro
    path("signup/", views.signup, name="signup"),

    # Perfil del usuario
    path("profile/", views.profile, name="profile"),

    # Editar perfil
    path("profile/edit/", views.profile_edit, name="profile_edit"),

    # Cambiar contraseña
    path("profile/password/", views.change_password, name="change_password"),
]
