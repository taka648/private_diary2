# リスト5.9:アプリケーション用新規ファイルurls.pyを作成する
from django.urls import path 
from . import views 

app_name ='diary' # <= ①diaryアプリケーションのルーティングに名前を付ける
urlpatterns = [   # <= ②アプリケーション用ルーティング設定を追加する
  path('', views.IndexView.as_view(), name="index"), 
] 
