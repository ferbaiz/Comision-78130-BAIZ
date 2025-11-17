from django.contrib import admin
from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ("emisor", "receptor", "contenido_resumen", "fecha")
    list_filter = ("fecha", "emisor")
    search_fields = ("emisor__username", "receptor__username", "contenido")

    def contenido_resumen(self, obj):
        return obj.contenido[:40] + "..." if len(obj.contenido) > 40 else obj.contenido

    contenido_resumen.short_description = "Mensaje"
