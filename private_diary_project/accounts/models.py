from django.db import models

# リスト10.2:CustomUserモデルクラスを定義する
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser): 
  """拡張ユーザーモデル"""

  class Meta: 
    verbose_name_plural = 'CustomUser' 
