#!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # """Run administrative tasks."""
    # """プログラムの最初で環境変数「DJANGO_SETTINGS_MODULE」が見つからなければ、自動的に「'DJANGO_SETTINGS_MODULE','private_diary.settings'」という環境変数をセットする。"""
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "private_diary_project.settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "private_diary_project.settings_dev")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
