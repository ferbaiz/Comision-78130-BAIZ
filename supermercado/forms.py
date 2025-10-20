from django import forms
from supermercado.models import Rubro, Proveedor, Cliente

class RubroForm(forms.ModelForm):
    class Meta:
        model = Rubro
        fields = ['nombre', 'descripcion']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono', 'email']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'saldo']