from .base import  *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x*15x&vm2x*cuye7ji)+_!^td-^mmnn-l%l(4!xya4p_#kf3gr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bd_restaurant_app',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'