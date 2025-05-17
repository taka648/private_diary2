# リスト11.6:日記テーブルを管理サイトで編集できるようにするため、管理サイトに日記モデルを登録する。
from django.contrib import admin
from .models import Diary

admin.site.register(Diary)
