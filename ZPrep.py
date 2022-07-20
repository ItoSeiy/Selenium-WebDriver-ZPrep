import datetime
from importlib.resources import path
import os
import sys
import time
import tkinter
from contextlib import nullcontext
from tkinter import messagebox

import chromedriver_binary
from appdirs import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

appname = "Z予備クン"
appauthor = "IS"
data_path = user_data_dir(appname, appauthor)
file_name = 'SaveData.text'
save_data = True

student_id = ''
password = ''
chapter_url = ''

id_txt = ''
password_txt = ''
chapter_url_txt = ''
save_data_box = ''

def open_chrome():
    # ブラウザを開いた後に消えないようにオプションを指定
    options = Options()
    options.add_experimental_option('detach', True)

    # クロームのオプションで音をミュートする
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--mute-audio')

    # オプションをドライバに適用
    driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=options, chrome_options=chrome_options)

    # N予備校のログイン画面を開く
    driver.get('https://www.nnn.ed.nico/login?next_url=https%3A%2F%2Fwww.nnn.ed.nico%2Fmy_course')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/a').click()

    global student_id, password, chapter_url

    time.sleep(1.5)

    # 学籍番号とパスワードの入力
    send_text('//*[@id="oauth_identifier_loginId"]', student_id, driver)
    send_text('//*[@id="oauth_identifier_password"]', password, driver)
    # ログインボタンをクリック
    driver.find_element(By.XPATH, '//*[@id="oauth_identifier_"]').click()

    # 指定された教材を開く
    driver.get(chapter_url)
    # 必修教材のみを表示する
    try:
        driver.find_element(By.XPATH, '//*[@id="sections-contents"]/div[1]/div[1]/div[2]/div/div[1]').click()
    except:
        print('')

    time.sleep(1.5)

    # 動画をテストやレポートまで再生し続ける
    play_video_loop(driver)

# 再生できる限り動画を再生し続ける
def play_video_loop(driver):
    video = play_new_video(driver)

    if(video == nullcontext):
        print('windowを新たに開きます')
        create_info_window('お知らせ', '確認テストまたはレポートに到達しました\n新しくZ予備クンのウィンドウを作成します')
        main()
        return

    time.sleep(get_video_seconds(video, 1.5))
    play_video_loop(driver)

# 視聴済みでない動画を再生する
def play_new_video(driver):
    #すべての動画を取得する
    videos = driver.find_elements(By.CLASS_NAME, 'movie')
    # 視聴済みでない動画を取得し再生する
    for video in videos:
        if '視聴済み' not in video.text.strip():
            try:
                video.find_element(By.CLASS_NAME, 'is-gate-closed')
                print('再生可能な動画が見つかりませんでした')
                return nullcontext
            except Exception:
                print('新しい動画を再生します')
                video.click()
                return video

# 動画の秒数を取得する
def get_video_seconds(video, buffer):
    # 動画のタイトルを取得
    texts = video.text.split()
    # 動画の秒数を抽出する
    hms_time = texts[2].split(':')
    return datetime.timedelta(minutes=int(hms_time[0]), seconds=int(hms_time[1])).total_seconds() + buffer

# XPATHの入力フィールドにテキストを入力する
def send_text(XPATH, text, driver):
    field = driver.find_element(By.XPATH, XPATH)
    field.send_keys(text)

# お知らせのwindowを開く
def create_info_window(window_name, message):
    messagebox.showinfo(window_name, message)

def temp_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# データのファイルの読み込みを試みる
def try_read_data_file():
    try:
        with open(f'{data_path}/{file_name}', encoding='utf-8') as f:
            global student_id, password, chapter_url
            data = f.read().split(' ')
            print(data)
            student_id = data[0]
            password = data[1]
            chapter_url = data[2]
    except Exception:
        nullcontext

# 次回からログインを省略するモードだったらテキストファイルにデータを保存する
def try_write_data_file():
    global save_data, student_id, password, chapter_url
    save_data = save_data_box.getboolean(save_data)
    if save_data:
        os.makedirs(data_path, exist_ok=True)
        with open(f'{data_path}/{file_name}', "w+") as f:
            f.writelines(student_id + ' ' + password + ' '+ chapter_url)
            f.close()

# グローバル変数にデータを入力する
def set_data_from_box():
    global student_id, password, chapter_url
    student_id = id_txt.get()
    password = password_txt.get()
    chapter_url = chapter_url_txt.get()

def main():

    global id_txt, password_txt, chapter_url_txt, save_data_box

    # データの読み込みを試みる
    try_read_data_file()

    # 画面作成
    tki = tkinter.Tk()
    tki.geometry('300x200')
    tki.title(appname)

    # ラベル
    id_label = tkinter.Label(text='学籍番号')
    id_label.place(x=30, y=30)

    password_label = tkinter.Label(text='パスワード')
    password_label.place(x=30, y=60)

    chapter_url_label = tkinter.Label(text='チャプターのURL')
    chapter_url_label.place(x=5, y=90)

    # テキストボックス
    id_txt = tkinter.Entry(width=20)
    id_txt.insert(tkinter.END, student_id)
    id_txt.place(x=90, y=30)

    password_txt = tkinter.Entry(width=20, show='*')
    password_txt.insert(tkinter.END, password)
    password_txt.place(x=90, y=60)

    chapter_url_txt = tkinter.Entry(width=20)
    chapter_url_txt.insert(tkinter.END, chapter_url)
    chapter_url_txt.place(x=90, y=90)

    # チェックボックス
    save_data_box = tkinter.Checkbutton(tki, text='次回からもこの学籍番号、パスワード、URLを使用する')
    save_data_box.place(x=30, y=120)
    save_data_box.select()

    # ボタン
    btn = tkinter.Button(tki, text='始める', command=lambda:[set_data_from_box() , try_write_data_file(), tki.destroy(), open_chrome()])
    btn.place(x=130, y=150)

    #アイコン
    tki.iconbitmap(temp_path('icon.ico'))

    # 画面をそのまま表示
    tki.mainloop()

main()