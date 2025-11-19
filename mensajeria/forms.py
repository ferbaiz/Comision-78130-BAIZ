from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ["destinatario", "asunto", "contenido"]
        widgets = {
            "destinatario": forms.Select(attrs={"class": "form-select"}),
            "asunto": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
