from django import forms
from .models import Page, Producto, Proveedor, Cliente

# ==========================
# FORMULARIO DE PAGE (BLOG)
# ==========================

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["titulo", "subtitulo", "contenido", "imagen"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


# ================================
# FORMULARIO DE PRODUCTO
# ================================

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["categoria", "nombre", "descripcion", "proveedor", "imagen", "precio", "stock"]
        widgets = {
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "proveedor": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Agrega clase bootstrap a todos
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        # Asegura que las categorías existan
        self.fields["categoria"].empty_label = "Seleccionar categoría"



# ================================
# FORMULARIO DE PROVEEDOR
# ================================

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "contacto", "telefono", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


# ================================
# FORMULARIO DE CLIENTE
# ================================

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "email", "telefono", "saldo"]
        widgets = {
            'telefono': forms.TextInput(attrs={'placeholder': 'Ej: 03442-123456'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
