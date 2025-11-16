from django.db import models
from django.conf import settings

class Mensaje(models.Model):
    remitente = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='recibidos', on_delete=models.CASCADE)
    asunto = models.CharField(max_length=200)
    cuerpo = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asunto} - {self.remitente} -> {self.destinatario}"
