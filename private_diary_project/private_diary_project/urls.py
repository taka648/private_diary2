# リスト5.8:プロジェクトのルーティング設定
from django.contrib import admin
# from django.urls import path
from django.urls import path, include  # <= ①追加:リスト5.8

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('diary.urls')),   # <= ②diaryアプリケーション用追加:リスト5.8
]
