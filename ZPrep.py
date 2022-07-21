from cgitb import text
import datetime
import os
import sys
import time
import tkinter
from turtle import goto
import webbrowser
from tkinter import messagebox

import chromedriver_binary
from appdirs import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

def open_chrome():
    # ブラウザを開いた後に消えないようにオプションを指定
    options = Options()
    options.add_experimental_option('detach', True)

    # エラーが出ないようにオプションを追加
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.use_chromium = True
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    # クロームのオプションで音をミュートする
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--mute-audio')

    # オプションをドライバに適用
    driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=options, chrome_options=chrome_options)

    # N予備校のログイン画面を開く
    driver.get('https://www.nnn.ed.nico/login?next_url=https%3A%2F%2Fwww.nnn.ed.nico%2Fmy_course')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/a').click()

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
def play_video_loop(driver : webelement.WebElement):
    video = play_new_video(driver)

    if(video == None):
        print('windowを新たに開きます')
        driver.quit()
        webbrowser.open(chapter_url)
        messagebox.showinfo('お知らせ', '確認テストまたはレポートに到達しました'
                            '\nOKボタンでZ予備クンを新たに開きます')
        create_window()
        return

    time.sleep(get_video_seconds(video))
    play_video_loop(driver)

# 視聴済みでない動画を再生する
def play_new_video(driver : webelement.WebElement):
    #すべての動画を取得する
    videos = driver.find_elements(By.CLASS_NAME, 'movie')
    # 視聴済みでない動画を取得し再生する
    for i, video in enumerate(videos):
        if '視聴済み' not in video.text.strip():
            print(f'{video.text}を視聴します')
            try:
                video.find_element(By.CLASS_NAME, 'is-gate-closed')
                print('再生可能な動画が見つかりませんでした')
                return None
            except:
                global current_video_name
                if video.text == current_video_name:
                    next_video = videos[i + 1]
                    print(f'現在再生している動画を再生しようとしたので次の\n{next_video.text}を再生できるまで待機します')
                    try_until_play_video(next_video)
                    print(f'{video.text}を再生できるようになったので再生します')
                    current_video_name = next_video.text
                    return next_video
                else:
                    print('新しい動画の再生を試みます')
                    try_until_play_video(video)
                    print('新しい動画を再生しました')
                    current_video_name = video.text
                    return video

# 動画の秒数を取得する
def get_video_seconds(video : webelement.WebElement):
    # 動画のタイトルを取得
    texts = video.text.split()
    # 動画の秒数を抽出する
    hms_time = texts[len(texts) - 1].split(':')
    wait_seconds = datetime.timedelta(minutes=int(hms_time[0]), seconds=int(hms_time[1])).total_seconds()
    print(f'待機時間{wait_seconds}秒')
    return wait_seconds

# 動画が再生できるようになるまで繰り返す
def try_until_play_video(video : webelement.WebElement):
    video.click()
    try:
        video.find_element(By.CLASS_NAME, 'is-selected')
    except:
        time.sleep(1)
        try_until_play_video(video)

# XPATHの入力フィールドにテキストを入力する
def send_text(XPATH : str, text : str, driver : webelement.WebElement):
    field = driver.find_element(By.XPATH, XPATH)
    field.send_keys(text)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# グローバル変数にデータを入力する
def set_data_from_box():
    global student_id, password, chapter_url
    student_id = id_txt.get()
    password = password_txt.get()
    chapter_url = chapter_url_txt.get()

# データのファイルの読み込みを試みる
def try_read_data_file():
    try:
        with open(f'{data_path}/{file_name}', encoding='utf-8') as f:
            global student_id, password, chapter_url, use_sound_notice, use_window_notice
            data = f.read().split(' ')
            print(data)
            student_id = data[0]
            password = data[1]
            chapter_url = data[2]
            if(data[3] == 'True'):
                use_sound_notice = True
            if(data[4] == 'True'):
                use_window_notice = True
    except Exception:
        return

# 次回からログインを省略するモードだったらテキストファイルにデータを保存する
def try_write_data_file():
    global save_data, student_id, password, chapter_url
    if save_data:
        os.makedirs(data_path, exist_ok=True)
        with open(f'{data_path}/{file_name}', "w+") as f:
            f.writelines(student_id + ' ' + password + ' '+ chapter_url + ' '+ str(use_sound_notice_var.get()) + ' '+ str(use_window_notice_var.get()))
            f.close()

def create_window():

    global id_txt, password_txt, chapter_url_txt, save_data_box, use_sound_notice_box, use_window_notice_box
    global use_sound_notice, use_window_notice, use_sound_notice_var, use_window_notice_var

    # データの読み込みを試みる
    try_read_data_file()

    # 画面作成
    tki = tkinter.Tk()
    tki.geometry('300x220')
    tki.title(appname)

    # ラベル
    id_label = tkinter.Label(text='学籍番号')
    id_label.place(x=30, y=30)

    password_label = tkinter.Label(text='パスワード')
    password_label.place(x=30, y=60)

    chapter_url_label = tkinter.Label(text='チャプターのURL')
    chapter_url_label.place(x=5, y=90)

    notice_box_label = tkinter.Label(text='通知のモード')
    notice_box_label.place(x=40, y=120)

    # テキストボックス
    id_txt = tkinter.Entry(width=20)
    id_txt.insert(tkinter.END, student_id)
    id_txt.place(x=100, y=30)

    password_txt = tkinter.Entry(width=20, show='*')
    password_txt.insert(tkinter.END, password)
    password_txt.place(x=100, y=60)

    chapter_url_txt = tkinter.Entry(width=20)
    chapter_url_txt.insert(tkinter.END, chapter_url)
    chapter_url_txt.place(x=100, y=90)

    # チェックボックス
    save_data_box = tkinter.Checkbutton(tki, text='次回からもこの設定を利用する')
    save_data_box.place(x=40, y=150)
    save_data_box.select()

    use_sound_notice_var = tkinter.BooleanVar()
    use_sound_notice_box = tkinter.Checkbutton(tki, text='ワッカさん', variable=use_sound_notice_var)
    use_sound_notice_box.place(x=120, y=120)
    if(use_sound_notice):
        use_sound_notice_box.select()

    use_window_notice_var = tkinter.BooleanVar()
    use_window_notice_box = tkinter.Checkbutton(tki, text='ウィンドウ', variable=use_window_notice_var)
    use_window_notice_box.place(x=190, y=120)
    if(use_window_notice):
        use_window_notice_box.select()

    # ボタン
    btn = tkinter.Button(tki, text='始める', command=lambda:[set_data_from_box() , try_write_data_file(), tki.destroy(), open_chrome()])
    btn.place(x=140, y=180)

    #アイコン
    tki.iconbitmap(resource_path('icon.ico'))

    # 画面をそのまま表示
    tki.mainloop()

appname = "Z予備クン"
appauthor = "IS"
data_path = user_data_dir(appname, appauthor)
file_name = 'SaveData.text'

# 学籍番号 パスワード URLの値
student_id, password, chapter_url = '', '', ''

# 通知の方法に関するフラグ
use_sound_notice, use_window_notice = False, False

# データをセーブするかどうかのフラグ
save_data = True

# ウィンドウのテキストボックス
id_txt, password_txt, chapter_url_txt= None, None, None

# ウィンドウのチェックボックス
save_data_box, use_sound_notice_box, use_window_notice_box = None, None, None

# 現在再生している動画のタイトル
current_video_name = None

create_window()
