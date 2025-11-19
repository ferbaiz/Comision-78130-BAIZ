from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()

# ======================
# CATEGORÍAS
# ======================
class Categoria(models.Model):
    RUBROS = [
        ('congelados', 'Congelados'),
        ('limpieza', 'Limpieza'),
        ('fiambreria', 'Fiambrería'),
        ('panificacion', 'Panificación'),
    ]

    nombre = models.CharField(max_length=120, choices=RUBROS, unique=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        # Devuelve siempre el label amigable
        return dict(self.RUBROS).get(self.nombre, self.nombre)


# ======================
# PROVEEDOR
# ======================
class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    contacto = models.CharField(max_length=150, blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre


# ======================
# CLIENTE
# ======================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    registrado = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# ======================
# PRODUCTO  (MODELO PRINCIPAL DE LA CONSIGNA)
# ======================
class Producto(models.Model):
    codigo = models.PositiveIntegerField(unique=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        related_name='productos'
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='productos'
    )
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


# ======================
# PAGE (POST / BLOG)
# ======================
class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages/', blank=True, null=True)
    publicado = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
