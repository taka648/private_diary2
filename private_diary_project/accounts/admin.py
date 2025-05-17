from django.contrib import admin

# リスト10.4:accountsアプリケーションの「accounts/admin.py」にCustomUserを設定する
from .models import CustomUser 

admin.site.register(CustomUser)
