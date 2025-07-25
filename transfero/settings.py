from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p0a*r41y0lg#da3lm40qfo@*)(^5iujy527bi94lnqz%ahn1%6'
=======

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s!$6!dss-4n!n6(bvzqw(6$5g8c1-z7qk$4xzd5s#p!lnpvrkv'
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sistema',
<<<<<<< HEAD
    'filmes',
    'usuarios',
=======
    'usuarios',
    'filmes',
    
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'transfero.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'base_templates'],
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

WSGI_APPLICATION = 'transfero.wsgi.application'


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
=======
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
=======
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/topics/i18n/
=======
# https://docs.djangoproject.com/en/4.2/topics/i18n/
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/SAO_PAULO'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/howto/static-files/


=======
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600

# Tupla que direciona os arquivos estáticos para dentro da pasta base_static
STATICFILES_DIRS = (
    BASE_DIR / 'base_static',
)
<<<<<<< HEAD

MEDIA_URL = 'media/' # É o endereco url inicial onde os arquivos de midia serão salvos. 
MEDIA_ROOT = BASE_DIR / 'media' # Um caminho onde os arquivos de midia serão salvos.

STATIC_URL = 'static/' # É o endereco url inicial aonde estão os arquivos estáticos.
STATIC_ROOT = BASE_DIR / 'static'# Um caminho para onde os arquivos estáticos são coletados.


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
=======
MEDIA_URL = 'media/' #é onde o endereco url inicial onde os arquivos de midia serão salvos.
MEDIA_ROOT = BASE_DIR/ 'media' # Um caminho onde os aqrquivos de midia serão salvos.

STATIC_URL= 'static/' # é o endereco url inicial aonde estão os arquivos estáticos.
STATIC_ROOT = BASE_DIR / 'static' # um caminho para onde os arquivos estáticos são coletados

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
>>>>>>> eb3e681827ada180133916620ee3ac2c19629600

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
