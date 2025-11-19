🛒 Supermercado — Proyecto Final Python / Django

Autor: Fernando Baiz
Comisión: 78130
Curso: Python — Coderhouse

📌 Descripción del Proyecto

Este proyecto es una aplicación web desarrollada en Python + Django, que simula la administración básica de un supermercado.
Incluye gestión de productos, categorías, proveedores, clientes, páginas tipo blog, perfiles de usuario y autenticación completa.

Es una entrega individual correspondiente al Playground Final Project del curso.

🎯 Funcionalidades Principales
🌐 Secciones Públicas

Home

About / Acerca de mí

Listado de productos

Detalle de productos

Páginas tipo blog (listado y detalle)

🔐 Secciones Protegidas (solo usuarios logueados)

CRUD de Productos

CRUD de Categorías

CRUD de Proveedores

CRUD de Clientes

Crear/editar/borrar páginas (blog)

Acceso a APIs internas protegidas

Vista protegida de ejemplo

👤 Sistema de Usuarios (APP: accounts)

Registro (Signup)

Login

Logout

Perfil del usuario

Edición de perfil (nombre, apellido, avatar, biografía, etc.)

Cambio de contraseña

🧱 Modelo Principal: Producto

Cumple todos los requisitos del docente:

✔ codigo: IntegerField unique=True

✔ nombre: CharField

✔ categoria: ForeignKey

✔ descripcion: TextField

✔ imagen: ImageField

✔ precio: DecimalField

✔ stock: PositiveIntegerField

✔ creado: DateTimeField (fecha automática)

📂 Estructura del Proyecto (simplificada)
supermercado/
│── accounts/
│── supermercado/
│   │── models.py
│   │── views.py
│   │── forms.py
│   │── urls.py
│   │── admin.py
│── mensajeria/
│── templates/
│   │── base.html
│   ├── accounts/
│   ├── supermercado/
│   └── mensajes/
│── media/
│── static/
│── requirements.txt
│── .gitignore
│── manage.py

🖼️ Templates

Se utiliza herencia de templates, con un base.html que contiene:

NavBar

Bootstrap

Mensajes

Footer

Includes reutilizables

🔧 Requisitos Técnicos — Cumplidos ✔
Django + Python

✔ Proyecto Django funcionando
✔ Models, Forms, Views, Admin
✔ Uso de CBVs (ListView, DetailView, CreateView, UpdateView, DeleteView)
✔ Uso de Mixin (LoginRequiredMixin)
✔ Uso de decorador (@login_required)
✔ CRUD completos
✔ Templates con herencia
✔ Formularios compatibles con imágenes
✔ APIs protegidas
✔ Migraciones aplicadas correctamente

Git

✔ Proyecto subido a GitHub
✔ .gitignore configurado:

__pycache__/
db.sqlite3
media/

Requirements

✔ requirements.txt generado con:

pip freeze > requirements.txt

▶️ Cómo ejecutar el proyecto
1️⃣ Crear entorno virtual
python -m venv entorno_virtual

2️⃣ Activarlo

Windows:

entorno_virtual\Scripts\activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Aplicar migraciones
python manage.py migrate

5️⃣ Crear superusuario
python manage.py createsuperuser

6️⃣ Iniciar servidor
python manage.py runserver


Acceso:
👉 http://127.0.0.1:8000/

👤 Acerca de Mí (About)

La página /about/ detalla información personal del desarrollador:

Nombre

Presentación

Intereses

Redes

🔐 Usuario / Perfil

Desde la app accounts el usuario puede:

Registrarse

Loguearse

Cerrar sesión

Ver su perfil

Editarlo

Cambiar la contraseña

Incluye:

Avatar (opcional)

Email

Nombre y apellido

Biografía

🛡️ Seguridad

Rutas protegidas mediante LoginRequiredMixin y @login_required

Las APIs y CRUD no se pueden usar sin autenticación

Sanitización de formularios estándar Django

📝 Licencia

Proyecto educativo realizado para Coderhouse.
Uso libre para fines académicos.

✔️ Estado Final

PROYECTO COMPLETAMENTE FUNCIONAL Y LISTO PARA ENTREGAR.