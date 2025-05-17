# リスト9.2:send_emailメソッドを実装
import os 

# リスト8.3:問い合わせページ用フォームのフィールドを定義するforms.pyを新規作成する
from django import forms 

# リスト9.2:①Beeやファイル添付が使えなかったりと機能が限られている、メール送信を簡便に扱うdjango.core.mail.send_mail関数ではなく、django.core.mail.EmailMessageクラスを使ってメール送信する
from django.core.mail import EmailMessage

# リスト11.25:django.forms.ModelFormクラスを継承してフォームを作る
from .models import Diary

# リスト8.3:①汎用的に使えるdjango.forms.Formクラスを継承したInquiryFormクラスを作り、その中で名前(name)とメールアドレス(email)とタイトル(title)とメッセージ(message)の4つのフォームフィールドを定義する
class InquiryForm(forms.Form): 
  name = forms.CharField(label='お名前',max_length=30) 
  email = forms.EmailField(label='メールアドレス') 
  title = forms.CharField(label='タイトル',max_length=30) 
  message = forms.CharField(label='メッセージ',widget=forms.Textarea)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.fields['name'].widget.attrs['class'] = 'form-control' 
    self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

    self.fields['email'].widget.attrs['class'] ='form-control' 
    self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

    self.fields['title'].widget.attrs['class'] = 'form-control' 
    self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。' 

    self.fields['message'].widget.attrs['class'] ='form-control' 
    self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

    def send_email(self):
        # リスト9.2:②フォームバリデーションをとおったユーザー入力値を取得する
        name = self.cleaned_data['name'] 
        email = self.cleaned_data['email'] 
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject ='お問い合わせ{}'.format(title) 
        message = '送信者名:{0}\nメールアドレス:{1}\nメッセージ:\n{2}'.format(name, email, message)
        # リスト9.2:③の送信元(from_email)と宛先(to_list)を環境変数からセットする
        from_email = os.environ.get('FROM_EMAIL') 

        to_list = [ 
            os.environ.get('FROM_EMAIL')
        ] 
        cc_list = [ 
            email 
        ] 

        # リスト9.2:④EmailMessageインスタンスを作成する
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list) 
        # リスト9.2:⑤sendメソッドを呼び出す
        message.send() 

# リスト11.25:django.forms.ModelFormクラスを継承してフォームを作る
class DiaryCreateForm(forms.ModelForm):
  class Meta:
    model = Diary
    fields = ('title', 'content', 'photo1', 'photo2', 'photo3',)

  def __init__(self, *args, **kwargs):
    super.__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'
