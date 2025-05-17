# リスト11.7:日記一覧表示。日記一覧ページはログイン直後に表示されるページです。
from django.urls import path
from . import views

# <= ①diaryアプリケーションのルーティングに名前を付ける
app_name ='diary'
# <= ②アプリケーション用ルーティング設定を追加する
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  # リスト8.1:①問い合わせ画面用のルーティングを追加する
  path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
  # リスト11.7:①日記一覧表示ルーティングの設定
  path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
  # リスト11.23:①日記作成機能用のルーティングを追加する
  # リスト11.16:①日記の詳細ページを表示するルーティングを作成する
  path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
  # リスト11.23:①日記作成機能用のルーティングを追加する
  path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
  # リスト11.28:①日記編集機能ルーティングの作成
  path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
  # リスト11.32:日記削除機能ルーティングの作成
  path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]

