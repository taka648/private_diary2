# リスト11.38:ログイン機能だけをテストするテストモジュールのテストコード
from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLogin(LiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    # リスト11.38:①親クラスのメソッドを呼び出しておく
    super().setClass()
    cls.selenium = webdriver.Chorme()

  @classmethod
  def tearDownClass(cls):
    # リスト11.38:①親クラスのメソッドを呼び出しておく
    cls.selenium.quit()
    super().tearDownClass()

  def test_login(self):
    # ログインページを開く
    self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

    # メールアドレス欄の入力
    # リスト11.38:②
    username_input = self.selenium.find_element(By.NAME, "login") 
    username_input.send_keys('<ユーザー登録済みのメールアドレス>')
    # パスワード欄の入力
    password_input= self.selenium.find_element(By.NAME, "password')
    password_input.send_keys('<ログインパスワード>')

    # ログインボタンのクリック
    # リスト11.38:③ボタン要素を取得する
    button = self.selenium.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div/form/button')
    button.click() 

    # 指定秒数待機(ページ遷移のため)
    time.sleep(3) 

    # ページタイトルの検証
    self.assertEqual('日記一覧 | Private Diary', self.selenium.title) 
