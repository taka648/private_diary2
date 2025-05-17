# リスト11.8:DiaryListViewビューを定義する
# リスト9.1:問い合わせ画面用のビュー(InquiryView)にメール送信に関する処理とロギング処理を追加する。
# リスト9.1:ロギング処理
import logging
# リスト9.1:URLを逆引きするreverse_lazy関数
from django.urls import reverse_lazy
# リスト11.8:
# リスト11.36:日記詳細/日記編集/日記削除ビューの修正
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# リスト5.10:トップページ用ビューを作成する
# from django.shortcuts import render
# リスト11.36:日記詳細/日記編集/日記削除ビューの修正
from django.shortcuts import get_object_or_404

from django.views import generic
# リスト8.2:①
from .forms import InquiryForm
# リスト11.8:
from .models import Diary

# 11.24:リストクラスベースビューであるCreateViewを継承したDiaryCreateViewクラスを作る
from .forms import InquiryForm, DiaryCreateForm

# リスト9.1:①ロガーを取得する
logger = logging.getLogger(__name__)



class IndexView(generic.TemplateView):
    template_name="index.html" # <=①アプリケーション用ディレクトリ内にあるtemplatesディレクトリから探し出す

# リスト8.2:②InquiryViewクラスを追加する
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry') # リスト9.1:②クラス変数(success_url)処理に問題がなかったときに指定URL('<urls.pyのapp_name>:<ルーティングに付けたname>')にリダイレクトする

    # リスト9.1:③form_validメソッド
    def form_valid(self, form):
        # リスト9.1:④forms.pyに次節で記述するメール送信メソッドを呼び出す
        forms.send_email()  
        # リスト9.1:⑤フォームバリデーションをとおったユーザー入力値を取り出す。ビューからログを出力する。
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))  
        return super().form_valid(form) 


# リスト11.36:①Djangoが提供するUserPassesTestMixinというMixinを継承したOnlyYouMixinというクラスを作る。UserPassesTestMixinはログイン済みユーザーのアクセスを制限する
# リスト11.36:
class OnlyYouMixin(UserPassesTestMixin):
  # リスト11.36:②Trueの場合は403エラーのページに遷移し、False(デフォルト値)の場合はログインページに遷移する。
  raise_exception = True

  # リスト11.36:③どのような制限をかけるかはtest funcメソッドをオーバーライドして記述する
  def test_func(self):
    # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
    # リスト11.36:④指定した「検索するキーワード引数」に該当するデータオブジェクトをモデルの対象テーブルから取り出す
    diary = get_object_or_404(Diary, pk=self.kwargs['pk'])

    # 1件のデータオブジェクトを取得するgetメソッドを用いた場合
    # 存在しないデータを取得しようとすると500エラー(サーバー内エラー)が発生する
    # diary = Diary.objects.get(pk=self.kwargs['pk'])

    # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
    return self.request.user == diary.user


# リスト11.8:①ListViewを継承してDiaryListViewを作る。また、Djangoが提供するLoginRequiredMixinを継承し、ログイン状態でないとDiaryListViewにアクセスできないようにしている。「Mixin」は継承されることを前提にしたPythonクラスで、継承先のクラスに機能を付加する。LoginRequiredMixinはListViewより先に記述しなければならない。メソッド解決順序は継承した順番に従うため、Mixinは最初に書くのが基本になる。
class DiaryListView(LoginRequiredMixin, generic.ListView):
  model = Diary
  template_name = 'diary_list.html'
  # リスト11.14:①
  paginate_by= 2

  def get_queryset(self):
    # リスト11.8:②「self.request.user」でログインしているユーザーのユーザーインスタンスを取得して、「order_by('-created_at')」と「—」を付けて作成日時で降順に並べ替えている。これでログインユーザーの日記データが作成日時の新しい順に表示される。
    diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
    return diaries 

# リスト11.19:日記詳細表示機能は、特定のデータベースデータを画面に表示するため、この目的に合うクラスベースビューであるDetailViewを継承してDiaryDetailViewクラスを作成する
# class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
# リスト11.36:⑤OnlyYouMixinクラスをアクセス制御するビューにそれぞれ継承する。これで日記の作成者以外はのビューにアクセスできない
class DiaryDetailView(LoginRequiredMixin, OnlyYouMixin, generic.DetailView):
  model = Diary
  template_name = 'diary_detail.html'

# リスト11.24:リストクラスベースビューであるCreateViewを継承したDiaryCreateViewクラスを作る
class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
  model = Diary
  template_name = 'diary_create.html'
  # リスト11.24:①クラス変数(form_class)をオーバーライドしてフォーム(DiaryCreateForm)を利用することを宣言する。
  form_class = DiaryCreateForm
  # リスト11.24:②正常に処理が完了した際の遷移先を設定する。ここでは日記一覧ページに遷移する。
  success_url = reverse_lazy('diary:diary_list')


  # リスト11.24:フォームのバリデーションに問題がなければ実行されるメソッド
  def form_valid(self, form):
    # リスト11.24:③データベースにフォームの内容を保存しないで該当のモデルオブジェクト(Diary)を取得する
    diary = form.save(commit=False)
    # リスト11.24:④ログインしているユーザーのモデルオブジェクトをセットする
    diary.user = self.request.user
    # リスト11.24:⑤データベースにフォームの内容を保存する。user値の入カフィールドを設けないため、サーバー側でuser値をモデルにセットしておく必要がある
    diary.save()
    messages.success(self.request, '日記を作成しました。')
    return super().form_valid(form)

  # リスト11.24:⑥フォームバリデーションが失敗したときに実行されるメソッドオーバーライドし、エラーメッセージを画面に出力する
  def form_invalid(self, form):
    messages.error(self.request, "日記の作成に失敗しました。")
    return super().form_invalid(form)

# リスト11.29:UpdateViewを継承し、DiaryUpdateViewクラスを作成する
# class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
# リスト11.36:⑤OnlyYouMixinクラスをアクセス制御するビューにそれぞれ継承する。これで日記の作成者以外はのビューにアクセスできない
# class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
class DiaryUpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
  model = Diary
  template_name = 'diary_update.html'
  # リスト11.29:①
  form_class = DiaryCreateForm

  # リスト11.29:②
  def get_success_url(self):
    return reverse_lazy('diary:diary_detail', kwargs={'pk':self.kwargs['pk']})

  def form_valid(self,form):
    messages.success(self.request, "日記を更新しました。")
    return super().form_valid(form)

  def form_invalid(self,form):
    messages.error(self.request, "日記の更新に失敗しました。")
    return super().form_invalid(form)

# リスト11.33:削除を行うクラスベースビューのDeleteViewを継承してDiaryDeleteViewクラスを作成する
# class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
# リスト11.36:⑤OnlyYouMixinクラスをアクセス制御するビューにそれぞれ継承する。これで日記の作成者以外はのビューにアクセスできない
# class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
class DiaryDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
  model = Diary
  template_name = 'diary_delete.html'
  # リスト11.33:①削除処理が成功したときは日記一覧ページに遷移する。日記一覧ページはURLが変わらないので、クラス変数(success_url)をオーバーライドしている
  success_url = reverse_lazy('diary:diary_list')

  # リスト11.33:②DeleteViewの削除成功時に実行されるdeleteメソッドをオーバーライドして、画面にメッセージを表示する
  def delete(self, request, *args, **kwargs):
    messages.success(self.request, "日記を削除しました。")
    return super().delete(request, *args, **kwargs)
