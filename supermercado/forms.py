from django import forms
from .models import Page, Producto, Proveedor, Cliente, Categoria


# =====================================================================
# FORM PAGE (BLOG)
# =====================================================================

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["titulo", "subtitulo", "contenido", "imagen"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


# =====================================================================
# FORM PRODUCTO
# =====================================================================

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "codigo",
            "categoria",
            "nombre",
            "descripcion",
            "proveedor",
            "imagen",
            "precio",
            "stock",
        ]

        widgets = {
            "codigo": forms.NumberInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "proveedor": forms.Select(attrs={"class": "form-select"}),

            # IMPORTANTE: no usar Input para imagen, sino ClearableFileInput
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),

            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
        }


# =====================================================================
# FORM PROVEEDOR
# =====================================================================

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "contacto", "telefono", "email"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "contacto": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


# =====================================================================
# FORM CLIENTE
# =====================================================================

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "email", "telefono", "saldo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: 03442-123456"
            }),
            "saldo": forms.NumberInput(attrs={"class": "form-control"}),
        }


# =====================================================================
# FORM CATEGORÍA
# =====================================================================

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]

        widgets = {
            # nombre es select porque usa choices=RUBROS
            "nombre": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }
