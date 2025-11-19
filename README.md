# 🛒 Supermercado — Proyecto Final Python / Django  
**Autor:** Fernando Baiz  
**Comisión:** 78130 – Coderhouse  
**Curso:** Python  

---

## 📌 Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con **Python + Django**, que simula la administración básica de un **supermercado**.

Incluye gestión de:

- Productos  
- Categorías (tipos de rubros fijos mediante `choices`)  
- Proveedores  
- Clientes  
- Páginas tipo blog  
- Sistema de usuarios  
- Mensajería interna  

El proyecto cumple todos los requisitos del **Playground Final Project** del curso.

---

## 🎯 Funcionalidades Principales

### 🌐 Secciones públicas (sin login)
- Home
- About
- Listado de productos
- Detalle de producto
- Listado y detalle de páginas del blog

---

### 🔐 Secciones protegidas (requiere login)
- **CRUD de Productos**
- **CRUD de Categorías** (select fijo por `choices`)
- **CRUD de Proveedores**
- **CRUD de Clientes**
- Crear / editar / borrar páginas del blog
- Bandeja de mensajes internos
- Enviados, nuevo mensaje, responder
- Vista protegida de ejemplo

---

## 👤 Sistema de Usuarios (App: `accounts`)

- Registro (Signup)
- Login
- Logout
- Perfil del usuario
- Edición de perfil
- Cambio de contraseña

Datos del perfil:
- Nombre / Apellido  
- Email  
- Avatar (opcional)  
- Biografía  

---

## 🧱 Modelo Principal — **Producto**

Cumple todos los requisitos del docente:

- `codigo` – IntegerField (único)
- `nombre` – CharField
- `categoria` – ForeignKey a Categoria
- `descripcion` – TextField
- `imagen` – ImageField (media/)
- `precio` – DecimalField
- `stock` – PositiveIntegerField
- `creado` – DateTimeField (auto)

---

## 📂 Estructura del Proyecto (simplificada)

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


---

## 🎨 Templates

Sistema completo de templates con:
- Herencia desde `base.html`
- Navbar Bootstrap  
- Mensajes del sistema  
- Formularios seguros  
- Estilo moderno con Bootstrap Icons  

---

## 🔧 Requisitos Técnicos — 

### Django / Backend
- Proyecto Django 100% funcional
- Models + Forms + Admin configurados
- Uso de **CBV**: ListView, DetailView, CreateView, UpdateView, DeleteView
- Uso de **LoginRequiredMixin**
- Uso de **@login_required**
- CRUD completos en todas las apps
- Subida de imágenes
- Migraciones correctas
- APIs y vistas protegidas

### Git / GitHub
- Proyecto subido correctamente  
- `.gitignore` incluye:
  - `__pycache__/`
  - `db.sqlite3`
  - `media/`

### Requirements
Generado con:
pip freeze > requirements.txt


---

## ▶️ Cómo Ejecutar el Proyecto

### 1️⃣ Crear entorno virtual
```bash
python -m venv entorno_virtual

2️⃣ Activarlo

Windows:

entorno_virtual\Scripts\activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Migrar base de datos
python manage.py migrate

5️⃣ Crear superusuario
python manage.py createsuperuser

6️⃣ Ejecutar servidor
python manage.py runserver


Acceso:
👉 http://127.0.0.1:8000/

💬 Acerca del Desarrollador (About)

La sección /about/ incluye presentación personal, intereses y datos relevantes del autor.

🔐 Seguridad

CRUD y APIs protegidos

Acceso restringido a usuarios autenticados

Formularios validados por Django

Mensajes internos privados

📝 Licencia

Proyecto educativo realizado para el curso de Python – Coderhouse.
Uso libre para fines académicos.