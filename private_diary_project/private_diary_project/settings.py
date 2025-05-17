# リスト12.4:本番環境用Diangoプロジェクト設定ファイルを作成する
from .settings_common import *

# リスト12.4:①本番運用環境用にセキュリティキーを生成し環境変数から読み込む
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# リスト12.4:②デバッグモードを有効にするかどうか(本番運用では必ずFalseにする)
DEBUG = False

# リスト12.4:③許可するホスト名のリスト
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

# リスト12.4:④⑤静的ファイルを配置する場所
# 開発環境ではDjangoプロジェクト内に配置した静的ファイルから直接配信していたが、本番環境ではWebサーバーから配信するようにする
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

# リスト12.4:⑥Amazon SES関連設定
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
EMAIL_BACKEND ='django_ses.SESBackend' 
# AWSのリージョンがus-east-1(バージニア北部)以外であれば以下2つの設定が必要
# AWS_SES_REGION_NAME = 'us-west-2'
# AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'

# ロギング
LOGGING = { 
  'version': 1,
  'disable_existing_loggers': False,

  # ロガーの設定
  # リスト12.4:⑦ログレベルが「DEBUG」だった箇所をすべて「INFO」に変更
  'loggers': {
    # Djangoが利用するロガー
    'django': {
      'handlers': ['file'],
      'level': 'INFO',
    },
    # diaryアプリケーションが利用するロガー
    'diary': {
      'handlers': ['file'],
      'level': 'INFO',
    }, 
  }, 

  # ハンドラの設定
  # リスト12.4:⑧ハンドラを、コンソールヘ出力する「StreamHandler」からファイルに出力する「TimedRotatingFileHandler」に変更
  # リスト12.4:⑨本番環境で使っている「TimedRotatingFileHandler」で指定できる実行間隔単位
  'handlers': {
    'file': {
      'level': 'INFO',
      'class': 'logging.handlers. TimedRotatingFileHandler',
      'filename': os.path.join(BASE_0IR, 'logs/django.log),
      'formatter': 'prod',
      'when': '0',      # リスト12.4:⑨ログローテーション(新しいファイルヘの切り替え)間隔の単位(0=日)
      'interval': 1,    # リスト12.4:⑨ログローテーション間隔(1日単位)
      'backupCount': 7, # リスト12.4:⑨保存しておくログファイル数
    },
  },

  # フォーマッタの設定
  'formatters': {
    'prod': {
      'format':'¥t'.join([
        '%(asctime)s',
        '[%(levelname)s]',
        '%(pathname)s(Line:%(lineno)d)',
        '%(message)s'
      ]) 
    },
  }
}
