from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# ======= SIGNUP =======
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu cuenta fue creada exitosamente. Ya podés iniciar sesión.")
            return redirect("accounts:login")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


# ======= PERFIL (solo usuarios logueados) =======
@login_required
def profile(request):
    return render(request, "accounts/profile.html")


# ======= EDITAR PERFIL (opcional, se puede ampliar luego) =======
@login_required
def profile_edit(request):
    messages.info(request, "Edición de perfil en desarrollo.")
    return redirect("accounts:profile")
