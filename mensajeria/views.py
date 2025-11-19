from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Mensaje
from .forms import MensajeForm


# ===============================
# BANDEJA DE ENTRADA
# ===============================
@login_required
def bandeja(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha')
    return render(request, "mensajeria/bandeja.html", {
        "mensajes": mensajes
    })


# ===============================
# MENSAJES ENVIADOS
# ===============================
@login_required
def enviados(request):
    mensajes = Mensaje.objects.filter(remitente=request.user).order_by('-fecha')
    return render(request, "mensajeria/enviados.html", {
        "mensajes": mensajes
    })


# ===============================
# DETALLE DE MENSAJE
# ===============================
@login_required
def mensaje_detalle(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)

    # Seguridad: solo remitente o destinatario
    if mensaje.destinatario != request.user and mensaje.remitente != request.user:
        return redirect("mensajeria:bandeja")

    return render(request, "mensajeria/detalle.html", {
        "mensaje": mensaje
    })


# ===============================
# MARCAR COMO LEÍDO
# ===============================
@login_required
def marcar_leido(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk, destinatario=request.user)
    mensaje.leido = True
    mensaje.save()
    return redirect("mensajeria:detalle", pk=pk)


# ===============================
# NUEVO MENSAJE
# ===============================
@login_required
def mensaje_nuevo(request):
    para = request.GET.get("para")  # Para pre-seleccionar destinatario
    
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.remitente = request.user
            nuevo.save()
            return redirect("mensajeria:bandeja")
    else:
        initial = {}

        # Autocompletar destinatario si viene desde “Responder”
        if para:
            try:
                usuario_destino = User.objects.get(username=para)
                initial["destinatario"] = usuario_destino
            except User.DoesNotExist:
                pass

        form = MensajeForm(initial=initial)

    return render(request, "mensajeria/nuevo.html", {
        "form": form
    })
