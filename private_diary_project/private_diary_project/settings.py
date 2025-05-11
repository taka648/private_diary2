# リスト5.6:追記
import os 
# リスト5.1:private_diary/settings.py:Python 
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-h80au2x5cnfrrz(+kdoxf(utzjdi77kjqm+sh_p^@zw81t31n0"

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
    "diary.apps.DiaryConfig",      # リスト5.1:<= ①
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "private_diary_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "private_diary_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# リスト5.6:データベース設定
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = { 
    "default": { 
        "ENGINE": "django.db.backends.postgresql", 
        "NAME": "private_diary", 
        "USER": os.environ.get('DB_USER'),
        "PASSWORD": os.environ.get('DB_PASSWORD'),
        "HOST": '',
        "PORT": '',
    }
} 


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# リスト5.4:Djangoプロジェクトの言語とタイムゾーンを日本仕様に変更する。
# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
LANGUAGE_CODE = "ja" 
TIME_ZONE = "Asia/Tokyo" 

USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# リスト5.7:ロギング設定(開発用)
LOGGING= { 
  "version": 1,                      # 1固定
  "disable_existing_loggers": False, # <= ①既存ロガーを無効化する。True=>False

  # ロガーの設定
  "loggers": { 
    # Djangoが利用するロガー
      "django": { 
        "handlers": ["console"], 
        "level": "INFO", 
      }, 
      # diaryアプリケーションが利用するロガー 
      "diary": { 
        "handlers": ["console"], 
        "level": "DEBUG", 
      }, 
    }, 

    # ハンドラの設定
    "handlers": { 
      "console": { 
        "level": "DEBUG", 
        "class": "logging.StreamHandler", # <= ②コンソールヘ出力するハンドラStreamHandler
        "formatter": "dev" 
      }, 
    }, 

  # フォーマッタの設定
  "formatters": { 
    "dev": { 
      "format": "\t".join([                # <= ③ログをタブ区切りで出力する
        "%(asctime)s", 
        "[%(levelname)s]", 
        "%(pathname)s(Line:%(lineno)d)", 
        "%(message)s" 
      ]) 
    }, 
  } 
} 
