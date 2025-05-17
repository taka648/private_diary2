# 本番と開発共通の設定ファイルsettings_common.py
# リスト5.6:追記
import os 
# リスト5.1:private_diary/settings.py:Python 
from pathlib import Path

# リスト9.10:Bootstrapのalertクラスをメッセージに適用させて、見た目を改善する。
from django.contrib.messages import constants as messages 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-h80au2x5cnfrrz(+kdoxf(utzjdi77kjqm+sh_p^@zw81t31n0"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # リスト5.1:①diaryアプリケーションをprivate_diaryプロジェクトに登録する。
    "diary.apps.DiaryConfig",      
    # リスト10.1:accountsアプリケーションをprivate_diaryプロジェクトに登録する。
    'accounts.apps.AccountsConfig', 

    # リスト10.7:django-allauthとdjango-bootstrap5をサンプルアプリで使えるようにする
    # リスト10.7:①django-allauth
    'django.contrib.sites', 
    'allauth', 
    'allauth.account', 
    # リスト10.7:②django-bootstrap5
    'django_bootstrap5', 
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # リスト10.7:django-allauthとdjango-bootstrap5をサンプルアプリで使えるようにする
    # django-allauth用に追加(v0.56.0以降で必要)
    'allauth.account.middleware.AccountMiddleware', 
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
# リスト7.1:静的ファイルの場所(パス)を設定する
STATICFILES_DIRS = ( 
    os.path.join(BASE_DIR, "static"),
) 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# リスト5.7:ロギング設定(開発用)
# LOGGING= { 
#   "version": 1,                      # 1固定
#   "disable_existing_loggers": False, # <= ①既存ロガーを無効化する。True=>False
# 
#   # ロガーの設定
#   "loggers": { 
#     # Djangoが利用するロガー
#       "django": { 
#         "handlers": ["console"], 
#         "level": "INFO", 
#       }, 
#       # diaryアプリケーションが利用するロガー 
#       "diary": { 
#         "handlers": ["console"], 
#         "level": "DEBUG", 
#       }, 
#     }, 
# 
#     # ハンドラの設定
#     "handlers": { 
#       "console": { 
#         "level": "DEBUG", 
#         "class": "logging.StreamHandler", # <= ②コンソールヘ出力するハンドラStreamHandler
#         "formatter": "dev" 
#       }, 
#     }, 
# 
#   # フォーマッタの設定
#   "formatters": { 
#     "dev": { 
#       "format": "\t".join([                # <= ③ログをタブ区切りで出力する
#         "%(asctime)s", 
#         "[%(levelname)s]", 
#         "%(pathname)s(Line:%(lineno)d)", 
#         "%(message)s" 
#       ]) 
#     }, 
#   } 
# } 

# リスト9.10:リスト9.9④の「{{ message.tags }}」にsettings_ common. pyに追加した設定がメッセージレベルに応じて反映される
MESSAGE_TAGS = { 
  messages.ERROR: 'alert alert-danger', 
  messages.WARNING: 'alert alert-warning', 
  messages.SUCCESS: 'alert alert-success', 
  messages.INFO: 'alert alert-info', 
} 

# リスト10.3:AUTH_USER_MODELに定義したカスタムユーザーモデルを設定する
AUTH_USER_MODEL = 'accounts.CustomUser' 

# リスト10.7:django-allauthとdjango-bootstrap5をサンプルアプリで使えるようにする
# django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別用IDを設定
# リスト10.7:③
SITE_ID = 1 

# リスト10.7:④認証バックエンド(認証をテストするクラス)を2つ設定する
AUTHENTICATION_BACKENDS = ( 
  'allauth.account.auth_backends.AuthenticationBackend',
  # 一般ユーザー用(メールアドレス認証)
  'django.contrib.auth.backends.ModelBackend',
  # 管理サイト用(ユーザー名認証)
) 

# メールアドレス認証に変更する設定
ACCOUNT_AUTHENTICATION_METHOD = 'email' 
ACCOUNT_USERNAME_REQUIRED = False 

# サインアップにメールアドレス確認をはさむよう設定
# リスト10.7:⑤サインアップ処理でユーザーにメールを送信し、メール上のリンクをクリックして、ブラウザ上でサインアップ処理を継続できる流れ＝「ユーザー登録(仮登録)→メール送信→メール上のリンクのクリック→ユーザー登録(本登録)」にする設定である。
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' 
ACCOUNT_EMAIL_REQUIRED = True

# ログイン/ログアウト後の遷移先を設定
LOGIN_REOIRECT_URL = 'diary:index' 
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login' 

# ログアウトリンクのクリック一発でログアウトする設定
# リスト10.7:⑥Falseでは、ログアウトリンクをクリックしたあとにログアウト画面が表示され、もう一度ログアウトボタンをクリックさせる動きになる。
ACCOUNT_LOGOUT_ON_GET = True

# django-allauthが送信するメールの件名に自動付与される接頭辞をブランクにする設定
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

# デフォルトのメール送信元を設定
# リスト10.7:⑦環境変数からデフォルトの送信元メールアドレスをセットする。
DEFAULT_FROM_EMAIL = os.environ.get('FROM_EMAIL') 

# リスト11.2:画像を配信するURLのホスト名以下のルートURLに使用される
MEDIA_URL = '/media/' 

# リスト11.12:ログイン/ログアウト後の遷移先を設定
LOGIN_REDIRECT_URL = 'diary:diary_list'

# リスト11.44:バックアップバッチ用バックアップファイルの出力先と保存しておくファイル数の設定
BACKUP_PATH = 'backup/'
NUM_SAVED_BACKUP = 30
