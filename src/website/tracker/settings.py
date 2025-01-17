"""
Django settings for tracker project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from os import environ as env
import os
from pathlib import Path
import dj_database_url
import importlib.util
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def get_secret(name: str, encoding: str = "utf-8") -> str:
    credentials_dir = env.get("CREDENTIALS_DIRECTORY")

    if credentials_dir is None:
        raise RuntimeError("No credentials directory available.")

    try:
        with open(f"{credentials_dir}/{name}", encoding=encoding) as f:
            secret = f.read().removesuffix("\n")
    except FileNotFoundError:
        raise RuntimeError(f"No secret named {name} found in {credentials_dir}.")

    return secret


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "compressor",
    # AllAuth config
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "rest_framework",
    "shared",
    "webview",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # Allauth account middleware
    "allauth.account.middleware.AccountMiddleware",
]

COMPRESS_PRECOMPILERS = [
    ("text/x-sass", "django_libsass.SassCompiler"),
]

STATICFILES_FINDERS = ["compressor.finders.CompressorFinder"]

STATIC_ROOT = os.path.join(BASE_DIR, "shared/static/")

ROOT_URLCONF = "tracker.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "shared/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tracker.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600, conn_health_checks=True)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"django.contrib.auth.password_validation.{v}"}
    for v in [
        "UserAttributeSimilarityValidator",
        "MinimumLengthValidator",
        "CommonPasswordValidator",
        "NumericPasswordValidator",
    ]
]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "SCOPE": [
            "read:user",
            "read:org",
        ],
        "APPS": [
            {
                "client_id": get_secret("GH_CLIENT_ID"),
                "secret": get_secret("GH_SECRET"),
                "key": "",
            }
        ],
    }
}

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"

LOGIN_REDIRECT_URL = "webview:home"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Customization via user settings
user_settings_file = env.get("USER_SETTINGS_FILE", None)
if user_settings_file is not None:
    spec = importlib.util.spec_from_file_location("user_settings", user_settings_file)
    if spec is None or spec.loader is None:
        raise RuntimeError("User settings specification failed!")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules["user_settings"] = module
    from user_settings import *  # noqa: F403 # pyright: ignore [reportMissingImports]

# needed for debug_toolbar
INTERNAL_IPS = [
    "127.0.0.1",
    "[::1]",
]
