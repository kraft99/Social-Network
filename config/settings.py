"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.urls import reverse, reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ijt9=mm#s2gs6o5i21*8-h^7*y8o43vag6hw!p%0wfey($##&&'

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

    #3rd Party apps
    'crispy_forms',
    'social_django',

    #project apps
    'apps.account.apps.AccountConfig',
    'apps.comment.apps.CommentConfig',
    'apps.favorite.apps.FavoriteConfig',
    'apps.activity.apps.ActivityConfig',
    'apps.follow.apps.FollowConfig',
    'apps.report.apps.ReportConfig',
    'apps.post.apps.PostConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]


AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    
    'django.contrib.auth.backends.ModelBackend',
]

BACKEND_AUTH = 'django.contrib.auth.backends.ModelBackend'


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.context_processors.is_auth',

                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]




WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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



LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('account:auth')
LOGOUT_URL = reverse_lazy('account:logout')

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# CRISPY
CRISPY_TEMPLATE_PACK = 'bootstrap4'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media') 

STATICFILES_DIRS = [os.path.join(BASE_DIR,'staticfiles','static_env')]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles','static_cdn')



# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]



# AVATAR 
DEFAULT_AVATAR_PATH = 'dp/avatar_dir/default_avatar.jpeg'


# RANDOM_AVATAR_PATH = os.path.join(BASE_DIR,'static_env','images','dir_avatars') 
RANDOM_AVATAR_PATH = os.path.join(MEDIA_ROOT,'dir_avatars') 



SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1033445391512-60jl4bqpj01nmuolsssgmjo18q05m3ue.apps.googleusercontent.com' # App ID
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ajhZxLSnd4Pmfoh2Mbz-HBtl' # App Secrets

SOCIAL_AUTH_FACEBOOK_KEY = '651867272011825' # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '04e339229a647523d50fb70d8d08661a' # App Secrets