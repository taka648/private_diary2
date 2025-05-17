# リスト5.8:プロジェクトのルーティング設定
from django.contrib import admin
# リスト11.4:①
from django.contrib.staticfiles.urls import static
# from django.urls import path
# <= ①追加:リスト5.8
from django.urls import path, include

# リスト11.4:②
from . import settings_common, settings_dev 

# 「http(s)://<ホスト名>/accounts/~」というURLでアクセスがあった場合、django-allauthがデフォルトで持つurls.pyに処理を移譲させる。
urlpatterns = [
    path("admin/", admin.site.urls),
    # <= ②diaryアプリケーション用追加:リスト5.8
    path('', include('diary.urls')),
    # リストl0.8:
    path('accounts/', include('allauth.urls')), 
]

# リスト11.4:③開発サーバーでメディアを配信できるようにする設定
urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)
