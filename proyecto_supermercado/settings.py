from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-6tzr$^h0-b6#(r)70igdh3$%sl+5&r(62q_^lhg!3690hn7=60'
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# ===========================
# APPS INSTALADAS
# ===========================
INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'ckeditor',

    # Apps propias
    'supermercado',
    'accounts',
    'mensajes',
]


# ===========================
# MIDDLEWARE
# ===========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'proyecto_supermercado.urls'


# ===========================
# TEMPLATES
# ===========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 👇 Plantillas globales (como base.html)
        'DIRS': [BASE_DIR / 'templates'],

        # 👇 Permite cargar templates dentro de cada app
        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'proyecto_supermercado.wsgi.application'


# ===========================
# BASE DE DATOS
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===========================
# PASSWORDS (DESACTIVAR VALIDADORES)
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    # Desactivados a propósito para permitir contraseñas libres
]


# ===========================
# IDIOMA Y HORA
# ===========================
LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True
USE_TZ = True


# ===========================
# ARCHIVOS ESTÁTICOS (CSS, JS, IMGS)
# ===========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Para desarrollo
STATIC_ROOT = BASE_DIR / 'staticfiles'     # Para producción


# ===========================
# MEDIA (para imágenes subidas)
# ===========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ===========================
# LOGIN / LOGOUT
# ===========================
LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# ===========================
# DEFAULT PK
# ===========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
