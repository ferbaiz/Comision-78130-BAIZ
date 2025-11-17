from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm


@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(
        receptor=request.user
    ).order_by('-fecha')
    return render(request, "mensajes/bandeja.html", {"mensajes": mensajes})


@login_required
def mensaje_detalle(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if mensaje.receptor == request.user and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    return render(request, "mensajes/detalle.html", {"mensaje": mensaje})


@login_required
def mensaje_nuevo(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.emisor = request.user
            nuevo.save()
            messages.success(request, "Mensaje enviado correctamente.")
            return redirect("mensajes:bandeja")
    else:
        form = MensajeForm()

    return render(request, "mensajes/nuevo.html", {"form": form})
