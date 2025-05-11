#リスト5.2:diary/apps.py:Python
from django.apps import AppConfig


class DiaryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "diary"
