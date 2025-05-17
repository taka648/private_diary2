# 開発環境固有の設定ファイルsettings_dev.py
# リスト9.3:最終的settings_dev.py
# リスト9.3:①開発環境と本番環境の共通設定ファイル「settings_common.py」を読み込む
from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-h80au2x5cnfrrz(+kdoxf(utzjdi77kjqm+sh_p^@zw81t31n0"

# SECURITY WARNING: don't run with debug turned on in production!
# リスト9.3:②「DEBUG」を「True」にすることでエラー発生時にデバッグ情報が画面に出力される。本番運用時はセキュリティの観点で「False」にする。
DEBUG = True 

ALLOWED_HOSTS = []

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

# リスト9.4:開発時のメール配信先設定を追加する。
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# リスト11.1:メディアファイルの配置場所を指定する。「media」ディレクトリは存在しなければ初回の画像保存時に自動作成される。
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
