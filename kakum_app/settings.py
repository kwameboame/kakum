import os
import dj_database_url
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ('7v*yftu%pj42qeyfp5*r=y9^c$g34(3k5ncd^d5q1sux*ke9_)')

DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition
DJANGO_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'corsheaders',
    'storages',
    'pagination',
    'bootstrap3_datetime',
    'sorl.thumbnail',
    'social.apps.django_app.default',
    'tinymce',
)

LOCAL_APPS = (
    'apps.users',
    'apps.projects',
)

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "paste",
    'theme': "advanced",
    'paste_auto_cleanup_on_paste': 'true',
    'paste_remove_styles': 'true',
    'paste_remove_styles_if_webkit': 'true',
    'paste_strip_class_attributes': 'true',
}


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gidboa@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'users.KAKUser'

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'apps.users.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'kakum_app.urls'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'kakum_app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()
    DATABASES['default']['CONN_MAX_AGE'] = 960

    DEBUG = False

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    DEBUG = True


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Kakum App',
}

# Rest framework config
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'
    ),

    'PAGE_SIZE': 15
}

STATIC_ROOT = 'staticfiles'

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_CREDENTIALS = True

AWS_STORAGE_BUCKET_NAME = 'afrstatic'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'

AWS_QUERYSTRING_AUTH = False
S3DIRECT_UNIQUE_RENAME = False
S3DIRECT_REGION = 'us-east-1'

VIDEOS_PATH = 'CACHES/VIDEOS/' + datetime.now().strftime("%Y/%m/%d")
AUDIO_PATH = 'CACHES/AUDIO/' + datetime.now().strftime("%Y/%m/%d")
IMAGES_PATH = 'CACHES/IMAGES/' + datetime.now().strftime("%Y/%m/%d")

S3DIRECT_DESTINATIONS = {
    'vids': (VIDEOS_PATH, lambda u: u.is_authenticated(), ['video/mp4'],),
    'audios': (AUDIO_PATH, lambda u: u.is_authenticated(), ['audio/mp3'],),
    'imgs': (IMAGES_PATH, lambda u: True, ['image/jpeg', 'image/png'],),
    'docs': (IMAGES_PATH, lambda u: True, ['application/pdf',
                                           'application/vnd.ms-excel',
                                           'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                           'application/msword',
                                           'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                           'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                                           'application/vnd.ms-powerpointtd>'],),
}


ADMINS = (
    ('kakum', 'gidboa@gmail.com'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = "Kakum <gidboa@gmail.com>"
SERVER_EMAIL = "Kakum Error <gidboa@gmail.com>"

TODAY = datetime.now()
TODAY_PATH = TODAY.strftime("%Y/%m/%d")
THUMBNAIL_PREFIX = 'cache/' + TODAY_PATH + '/'

AUTHENTICATION_BACKENDS = (
   "django.contrib.auth.backends.ModelBackend",
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.twitter.TwitterOAuth',
)

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_TWITTER_KEY =  os.environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('SOCIAL_AUTH_TWITTER_SECRET')

LOGIN_REDIRECT_URL = '/issues/'
LOGIN_URL = '/user_login/'
LOGIN_ERROR_URL = '/'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'apps.users.pipeline.update_user_social_data',
)

SOCIAL_AUTH_USER_MODEL = 'users.KAKUser'
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

THUMBNAIL_DEBUG = True
