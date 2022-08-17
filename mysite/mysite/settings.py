from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)bgs&)*^ie0xy1_&p!-5r=*y^v1rp*5fxb)ynmm&2g44w-nr5='

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',]

# REST_AUTH_SERIALIZERS = {
#     'PASSWORD_RESET_SERIALIZER': 
#         'backend.serializers.PasswordResetSerializer',}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

# These are the default values if none are set
from datetime import timedelta
from rest_framework.settings import api_settings

# REST_KNOX = {
#   'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
#   'AUTH_TOKEN_CHARACTER_LENGTH': 64,
#   'TOKEN_TTL': timedelta(hours=2),
#   'USER_SERIALIZER': 'knox.serializers.UserSerializer',
#   'TOKEN_LIMIT_PER_USER': None,
#   'AUTO_REFRESH': False,
#   'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'knox.auth.TokenAuthentication'
    ],
    # 'DATETIME_FORMAT': "%d/%m/%Y %H:%M:%S",
    # 'DATE_INPUT_FORMATS': ["%d-%m-%Y",'%Y-%m-%d'],
    # 'DATE_FORMAT':["%d-%m-%Y",'%Y-%m-%d'],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')
# DATE_FORMAT = ('%d-%m-%Y','%Y-%m-%d')
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# RESET_PASSWORD_ROUTE = ''
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    # 'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': '',
    #    'USER': '',
    #    'PASSWORD': '',
    #    'HOST': '',
    #    'PORT': '',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
ROOT_URLCONF