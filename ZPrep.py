import datetime
import os
import sys
import time
import tkinter
import webbrowser
from tkinter import messagebox

import chromedriver_binary
import pygame
from appdirs import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

# --------------------動画関連--------------------

# 再生できる限り動画を再生し続ける
def play_video_loop(driver : webelement.WebElement):
    global video_and_test_elements_index
    result = exists_test_or_report()
    flag = result[0]
    message = result[1]
    if(flag == True):
        # 確認テストの直前で動画の再生が終わっていなかった場合の処理
        if '視聴済み' not in video_and_test_elements[video_and_test_elements_index - 1].text:
            print(f'{video_and_test_elements[video_and_test_elements_index - 1].text}'
                'は確認テスト, レポート直前だが再生が終了していないため再生が終わるまで待機します')
            try_until_play_video(video_and_test_elements[video_and_test_elements_index])
            print(f'{video_and_test_elements[video_and_test_elements_index - 1].text}の再生が終わりました')
        # テスト, レポートに到達したら終了時のウィンドウを生成する
        create_finish_window(driver, message)
        return
    video = play_new_video(driver)
    time.sleep(get_video_seconds(video))
    video_and_test_elements_index += 1
    play_video_loop(driver)

# 視聴済みでない動画を再生する
def play_new_video(driver : webelement.WebElement):
    global current_video_name
    videos = driver.find_elements(By.CLASS_NAME, 'movie')
    for i, video in enumerate(videos):
        if '視聴済み' not in video.text.strip():
            print(f'{video.text}が再生候補として見つかりました')
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
                print(f'indexは{video_and_test_elements_index}')
                current_video_name = video.text
                return video
    print('例外 フィルターにかからないテストまたはレポートが見つかりました')

def exists_test_or_report():
    if video_and_test_elements_index + 2 == len(video_and_test_elements):
            print('レポートに到達した')
            return (True, 'レポートに到達しました')
    if '確認テスト' in video_and_test_elements[video_and_test_elements_index].text:
        print('確認テストに到達した')
        return (True, '確認テストに到達しました')
    else:
        return (False, '')

# 動画が再生できるようになるまで繰り返す
def try_until_play_video(video : webelement.WebElement):
    video.click()
    try:
        video.find_element(By.CLASS_NAME, 'is-selected')
    except:
        time.sleep(1)
        try_until_play_video(video)

# 動画の秒数を取得する
def get_video_seconds(video : webelement.WebElement):
    # 動画のタイトルを取得
    texts = video.text.split()
    # 動画の秒数を抽出する
    hms_time = texts[len(texts) - 1].split(':')
    wait_seconds = datetime.timedelta(minutes=int(hms_time[0]), seconds=int(hms_time[1])).total_seconds()
    print(f'待機時間{wait_seconds}秒')
    return wait_seconds

# XPATHの入力フィールドにテキストを入力する
def send_text(XPATH : str, text : str, driver : webelement.WebElement):
    field = driver.find_element(By.XPATH, XPATH)
    field.send_keys(text)

# テストと動画を含めたエレメントのリストを登録する
def set_video_test_elements(driver : webelement.WebElement):
    global video_and_test_elements
    video_and_test_elements = driver.find_element(By.XPATH, '//*[@id="sections-contents"]/div[1]/div[1]/ul').find_elements(By.TAG_NAME, 'li')

def set_video_test_element_index():
    global video_and_test_elements_index, video_and_test_elements
    for i, element in enumerate(video_and_test_elements):
        try:
            element.find_element(By.CLASS_NAME, 'is-gate-closed')
            video_and_test_elements_index = i - 1
            print(f'{video_and_test_elements[video_and_test_elements_index].text}\nが現在のエレメント')
            print(f'indexは{video_and_test_elements_index}')
            return
        except:
            continue

# --------------------セーブデータ関連--------------------

# パス取得
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
            global student_id, password, chapter_url, use_sound_notice, use_window_notice, notice_sound_scale
            data = f.read().split(' ')
            print(data)
            student_id = data[0]
            password = data[1]
            chapter_url = data[2]
            if(data[3] == 'True'):
                use_sound_notice = True
            if(data[4] == 'True'):
                use_window_notice = True
            notice_sound_scale = data[5]
    except Exception:
        return

# tkinterのウィンドウ等からグローバル変数にデータを入力する
def set_data_from_box(id_txt, password_txt, chapter_url_txt,
                    use_sound_notice_var, use_window_notice_var,
                    notice_sound_scale_widget, save_data_var):

    global student_id, password, chapter_url, use_sound_notice, use_window_notice, notice_sound_scale, save_data

    student_id = id_txt.get()
    password = password_txt.get()
    chapter_url = chapter_url_txt.get()
    use_sound_notice = use_sound_notice_var.get()
    use_window_notice = use_window_notice_var.get()
    notice_sound_scale = notice_sound_scale_widget.get()
    save_data = save_data_var.get()

# 次回からログインを省略するモードだったらテキストファイルにデータを保存する
def try_write_data_file():
    global student_id, password, chapter_url, notice_sound_scale
    if save_data:
        os.makedirs(data_path, exist_ok=True)
        with open(f'{data_path}/{file_name}', "w+") as f:
            f.writelines(student_id + ' ' + password + ' '+ chapter_url + ' '+
                        str(use_sound_notice) + ' '+ str(use_window_notice) + ' ' +
                        str(notice_sound_scale))
            f.close()


# ----------------------------------------

# 最初に呼び出される tkinterのウィンドウを描画する
def create_window():
    # データの読み込みを試みる
    try_read_data_file()

    # 画面作成
    tki = tkinter.Tk()
    tki.geometry('320x220')
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

    notice_sound_label = tkinter.Label(text='ワッカさんの声量', font=("MS明朝", "8"))
    notice_sound_label.place(x=230, y=28)

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
    save_data_var = tkinter.BooleanVar()
    save_data_box = tkinter.Checkbutton(tki, text='次回からもこの設定を利用する', variable=save_data_var)
    save_data_box.place(x=40, y=150)
    save_data_box.select()

    use_sound_notice_var = tkinter.BooleanVar()
    use_sound_notice_box = tkinter.Checkbutton(tki, text='ワッカさん', variable=use_sound_notice_var)
    use_sound_notice_box.place(x=110, y=120)
    if(use_sound_notice):
        use_sound_notice_box.select()

    use_window_notice_var = tkinter.BooleanVar()
    use_window_notice_box = tkinter.Checkbutton(tki, text='ウィンドウ', variable=use_window_notice_var)
    use_window_notice_box.place(x=180, y=120)
    if(use_window_notice):
        use_window_notice_box.select()

    # ワッカさんの音量を調整するスケールウィジェット
    notice_sound_scale_widget = tkinter.Scale(tki, orient=tkinter.VERTICAL, from_=0, to=1, resolution=0.1, length = 100)
    notice_sound_scale_widget.place(x=265, y=45)
    notice_sound_scale_widget.set(notice_sound_scale)

    # ボタン
    btn = tkinter.Button(tki, text='始める',
                        command=lambda:[set_data_from_box(
                                        id_txt=id_txt, password_txt=password_txt, chapter_url_txt=chapter_url_txt,
                                        use_sound_notice_var=use_sound_notice_var, use_window_notice_var=use_window_notice_var,
                                        notice_sound_scale_widget=notice_sound_scale_widget, save_data_var=save_data_var),
                                        try_write_data_file(), tki.destroy(), open_chrome()])
    btn.place(x=140, y=180)

    #アイコン
    tki.iconbitmap(resource_path('icon.ico'))

    # 画面をそのまま表示
    tki.mainloop()

# クロームを開く
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
    driver = webdriver.Chrome(resource_path('chromedriver.exe'), options=options, chrome_options=chrome_options)

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
        None

    time.sleep(1.5)

    # テストと動画を含めたエレメントのリストを登録する
    set_video_test_elements(driver)
    set_video_test_element_index()

    # 動画をテストやレポートまで再生し続ける
    play_video_loop(driver)

# 確認テスト, レポートに到達した際のウィンドウを生成する
def create_finish_window(driver: webelement.WebElement, message : str):
    print('確認テストまたはレポートに到達しました')
    driver.quit()

    if(use_sound_notice):
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path('Wakka.mp3'))
        pygame.mixer.music.set_volume(notice_sound_scale)
        pygame.mixer.music.play()

    webbrowser.open(chapter_url)

    if(use_window_notice):
        messagebox.showinfo('お知らせ', f'{message}\nOKボタンでZ予備クンを新たに開きます')

    create_window()

# ----------変数宣言----------

appname = "Z予備クン"
appauthor = "IS"
data_path = user_data_dir(appname, appauthor)
file_name = 'SaveData.text'

# 学籍番号 パスワード URLの値
student_id, password, chapter_url = '', '', ''

# 通知の方法に関するフラグ
use_sound_notice, use_window_notice = False, False

# 通知の音量
notice_sound_scale = 0.1

# データをセーブするかのフラグ
save_data = True

# 現在再生している動画のタイトル
current_video_name = ''

# テストと動画を含めたエレメントのリスト
video_and_test_elements = []

# 現在のテストと動画を含めたエレメントのリストのIndex
video_and_test_elements_index = 0

# ウィンドウを作成 最初の呼び出し
create_window()