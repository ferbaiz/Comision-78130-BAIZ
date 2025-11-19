from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import SignUpForm, ProfileEditForm


# =====================================================
# LOGIN
# =====================================================
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect("supermercado:home")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


# =====================================================
# LOGOUT
# =====================================================
def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect("accounts:login")


# =====================================================
# SIGNUP / REGISTRO
# =====================================================
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente. Ya puedes iniciar sesión.")
            return redirect("accounts:login")
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})


# =====================================================
# PERFIL
# =====================================================
@login_required
def profile(request):
    return render(request, "accounts/profile.html")


# =====================================================
# EDITAR PERFIL
# =====================================================
@login_required
def profile_edit(request):
    user = request.user

    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("accounts:profile")
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = ProfileEditForm(instance=user)

    return render(request, "accounts/profile_edit.html", {"form": form})


# =====================================================
# CAMBIO DE CONTRASEÑA
# =====================================================
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Contraseña actualizada correctamente.")
            return redirect("accounts:profile")
        else:
            messages.error(request, "Corrige los errores.")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "accounts/change_password.html", {"form": form})
