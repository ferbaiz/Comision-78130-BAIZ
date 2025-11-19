from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Producto, Proveedor, Cliente, Page


# ======================
# ADMIN - CATEGORÍA
# ======================
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('nombre',)


# ======================
# ADMIN - PROVEEDOR
# ======================
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'telefono', 'email')
    search_fields = ('nombre', 'email')
    list_filter = ('nombre', 'email')


# ======================
# ADMIN - CLIENTE
# ======================
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'saldo')
    search_fields = ('nombre', 'email')
    list_filter = ('saldo', 'email')


# ======================
# ADMIN - PRODUCTO
# ======================
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'proveedor', 'precio', 'stock', 'creado', 'imagen_tag')
    list_filter = ('categoria', 'proveedor', 'creado')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('creado',)

    # Mostrar imagen pequeña
    def imagen_tag(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:4px;" />', obj.imagen.url)
        return "-"
    imagen_tag.short_description = "Imagen"


# ======================
# ADMIN - PAGE
# ======================
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'publicado', 'autor')
    search_fields = ('titulo', 'subtitulo')
    list_filter = ('publicado', 'autor')
    readonly_fields = ('publicado',)
    ordering = ('-publicado',)
