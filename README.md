# Comision-78130-BAIZ
# 🛒 Proyecto Final: Supermercado (Django)

Este proyecto es una aplicación web desarrollada en **Django 5**, como entrega final del curso de Python en CoderHouse.  
Simula la gestión básica de un supermercado, con administración de:

- Productos
- Categorías
- Proveedores
- Clientes
- Páginas tipo Blog (CMS sencillo)
- Usuarios registrados (sistema de login y perfil)
- (En desarrollo) Sistema interno de mensajes entre usuarios

---

## 🚀 Tecnologías utilizadas

- Python 3.13
- Django 5.2.7
- Bootstrap 5.3
- SQLite3
- Django CKEditor (para contenido enriquecido)
- Virtualenv

---

## 📂 Estructura del proyecto

proyecto_supermercado/
│
├── supermercado/ # App principal
│ ├── models.py # Modelos (Producto, Cliente, Proveedor, etc.)
│ ├── views.py # Vistas principales
│ ├── urls.py # Rutas principales
│ └── templates/
│ └── supermercado/ # Templates HTML
│
├── accounts/ # App de usuarios
│ ├── models.py # Perfil de usuario
│ ├── forms.py # Formularios propios
│ └── templates/accounts/ # Templates login, signup, perfil
│
├── mensajes/ (en desarrollo)
│
├── media/ # Archivos subidos por usuarios
├── static/ # CSS, imágenes y JS
└── templates/ # Base templates compartidos

---

## 🛎 Funcionalidades principales

### 🛍 Productos  
- CRUD completo  
- Imagen, precio, stock, descripción  
- Relación con categorías y proveedores  

### 🏷 Categorías  
- Rubros predefinidos  
- Validadas  
- Vistas de listado y edición  

### 🚚 Proveedores  
- Nombre, contacto, email, teléfono  
- CRUD completo  

### 👥 Clientes  
- Email único  
- Registro de saldo  
- CRUD completo  

### 📝 Pages (CMS)
- Título, subtítulo, contenido enriquecido  
- Imagen opcional  
- Editor CKEditor  

### 👤 Usuarios  
- Registro  
- Login  
- Logout  
- Perfil editable  

---

## 🧰 Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/ferbaiz/Comision-78130-BAIZ.git

Crear entorno virtual:

python -m venv entorno_virtual


Activar entorno:

entorno_virtual\Scripts\activate


Instalar dependencias:

pip install -r requirements.txt


Realizar migraciones:

python manage.py migrate


Crear superusuario:

python manage.py createsuperuser


Iniciar servidor:

python manage.py runserver

Panel Admin
http://127.0.0.1:8000/admin/