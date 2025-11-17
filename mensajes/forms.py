from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ["receptor", "contenido"]
        widgets = {
            "contenido": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "receptor": forms.Select(attrs={"class": "form-select"}),
        }
