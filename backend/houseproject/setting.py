import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["*"]

# 개발서버 cors 허용
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'product',
    'story',
    'user',

]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
        ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'houseproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_DIR = os.path.join(os.path.dirname(BASE_DIR), 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "static"),
]

WSGI_APPLICATION = 'houseproject.wsgi.application'


MYSQL_NAME = os.environ.get("MYSQL_NAME", None)
MYSQL_USER = os.environ.get("MYSQL_USER", None)
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", None)
MYSQL_HOST = os.environ.get("MYSQL_HOST", None)
MYSQL_PORT = os.environ.get("MYSQL_PORT", None)
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", None)
MONGO_DB_HOST = os.environ.get("MONGO_DB_HOST", None)
MONGO_DB_USER = os.environ.get("MONGO_DB_USER", None)
MONGO_DB_PASSWORD = os.environ.get("MONGO_DB_PASSWORD", None)

DATABASE_ROUTERS = [
    "houseproject.routers.DatabaseRouter",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "django",
        "HOST": MYSQL_HOST,
        "PORT": MYSQL_PORT,
        "USER": MYSQL_USER,
        "PASSWORD": MYSQL_PASSWORD,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
        },
    },
    'mongo': {
        'ENGINE': 'djongo',
        'NAME': MONGO_DB_NAME,
        'CLIENT': {
            'host': MONGO_DB_HOST,
            'port': 27017,
            'username': MONGO_DB_USER,
            'password': MONGO_DB_PASSWORD,
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
