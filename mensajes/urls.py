from django.urls import path
from . import views

app_name = "mensajes"

urlpatterns = [
    path("", views.bandeja_entrada, name="bandeja"),
    path("nuevo/", views.mensaje_nuevo, name="nuevo"),
    path("<int:pk>/", views.mensaje_detalle, name="detalle"),
]
