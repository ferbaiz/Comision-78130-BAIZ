from django.urls import path
from . import views

app_name = "mensajeria"

urlpatterns = [
    # Bandeja de entrada
    path("", views.bandeja, name="bandeja"),

    # Mensajes enviados
    path("enviados/", views.enviados, name="enviados"),

    # Crear nuevo mensaje
    path("nuevo/", views.mensaje_nuevo, name="nuevo"),

    # Detalle del mensaje
    path("detalle/<int:pk>/", views.mensaje_detalle, name="detalle"),

    # Marcar mensaje como leído
    path("detalle/<int:pk>/leido/", views.marcar_leido, name="marcar_leido"),
]
