# リスト5.10:トップページ用ビューを作成する
# from django.shortcuts import render
from django.views import generic 

class IndexView(generic.TemplateView): 
    template_name="index.html" # <=①アプリケーション用ディレクトリ内にあるtemplatesディレクトリから探し出す

