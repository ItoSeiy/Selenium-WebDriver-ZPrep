import datetime
import os
import time
import tkinter
from turtle import window_height
import webbrowser
import directory
from tkinter import messagebox
import tkinter.ttk as ttk
from plyer import notification
from mutagen.mp3 import MP3

import chromedriver_binary
import pygame
import random
from appdirs import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

# 学籍番号 パスワード URL ログイン方式の値
student_id, password, chapter_url, login_option = '', '', '', ''

# 通知の方法に関するフラグ
use_sound_notice, use_window_notice = False, False

# 通知の音量
notice_sound_scale = 0.1

# データをセーブするかどうかのフラグ
save_data = True

# 音ミュートするかどうかのフラグ
mute_sound = False

# 現在再生している動画のタイトル
current_video_name = ''

# テストと動画を含めたエレメントのリスト
video_and_test_elements = []

# 現在のテストと動画を含めたエレメントのリストのIndex
video_and_test_elements_index = 0

# トースト通知に使用するアイコンのパスの配列
toast_icon_array = [directory.resource_path('wakka01.ico'), directory.resource_path('wakka02.ico')]

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
            print(f'indexは{video_and_test_elements_index}')
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
    print('例外 フィルターにかからないテストまたはレポートが見つかりました')

def exists_test_or_report():
    if video_and_test_elements_index + 1 == len(video_and_test_elements):
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

# データのファイルの読み込みを試みる
def try_read_data_file():
    try:
        with open(f'{directory.data_path}/{directory.file_name}', encoding='utf-8') as f:
            global student_id, password, chapter_url, login_option, use_sound_notice, use_window_notice, notice_sound_scale, mute_sound
            data = f.read().split(' ')
            print(f'読み込んだ設定ファイルの中身は{data}')
            print(f'設定ファイルのパス{directory.data_path}/{directory.file_name}')
            student_id = data[0]
            password = data[1]
            chapter_url = data[2]
            login_option = data[3]

            if(data[4] == 'True'):
                use_sound_notice = True
            elif(data[4] == 'False'):
                use_sound_notice = False
            else:
                raise ValueError

            if(data[5] == 'True'):
                use_window_notice = True
            elif(data[5] == 'False'):
                use_window_notice = False
            else:
                raise ValueError

            notice_sound_scale = data[6]

            if(data[7] == 'True'):
                mute_sound = True
            elif(data[7] == 'False'):
                mute_sound = False
            else:
                raise ValueError
    except Exception:
        student_id, password, chapter_url, login_option = '', '', '', ''
        use_sound_notice, use_window_notice = False, False
        notice_sound_scale = 0
        mute_sound = False
        return

# tkinterのウィンドウ等からグローバル変数にデータを入力する
def set_data_from_box(id_txt, password_txt, chapter_url_txt, login_option_var,
                    use_sound_notice_var, use_window_notice_var,
                    notice_sound_scale_widget, save_data_var, mute_sound_var):

    global student_id, password, chapter_url, login_option, use_sound_notice, use_window_notice, notice_sound_scale, save_data, mute_sound

    student_id = id_txt.get()
    password = password_txt.get()
    chapter_url = chapter_url_txt.get()
    login_option = login_option_var.get()
    use_sound_notice = use_sound_notice_var.get()
    use_window_notice = use_window_notice_var.get()
    notice_sound_scale = notice_sound_scale_widget.get()
    save_data = save_data_var.get()
    mute_sound = mute_sound_var.get()

# 次回からログインを省略するモードだったらテキストファイルにデータを保存する
def try_write_data_file():
    if save_data:
        os.makedirs(directory.data_path, exist_ok=True)
        with open(f'{directory.data_path}/{directory.file_name}', "w+") as f:
            f.writelines(student_id + ' ' + password + ' '+ chapter_url + ' '+ login_option + ' ' +
                        str(use_sound_notice) + ' '+ str(use_window_notice) + ' ' +
                        str(notice_sound_scale) + ' ' + str(mute_sound))
            f.close()

window_geometry = '320x265'
txt_box_width = 20

# 学籍番号
id_content_y = 30
id_label_x = 30
id_txt_x = 100

# パスワード
password_content_y = 60
password_label_x = 30
password_txt_x = 100

# URL
chapter_url_content_y = 90
chapter_url_label_x = 5
chapter_url_txt_x = 100

# ログイン方式
login_option_list = ['N', 'S']
login_option_box_width = 17
login_option_content_y = 120
login_option_label_x = 20
login_option_box_x = 100

# 通知
notice_box_label_x = 35
notice_box_label_y = 150

sound_notice_box_x = 110
window_notice_box_x = 180
notice_box_y = 148

# 音量調整
sound_widget_x = 265
sound_widget_y = 45
sound_widget_from = 1
sound_widget_to = 0
sound_widget_resolution = 0.1
sound_widget_length = 100

sound_label_x = 230
sound_label_y = 28

# ブラウザのミュート
mute_sound_box_x = 95
mute_sound_box_y = 172

# 設定保存
save_data_box_x = 65
save_data_box_y = 197

# スタートボタン
start_btn_x = 140
start_btn_y = 225

# GUIを描画する
def create_window():
    # データの読み込みを試みる
    try_read_data_file()

    # 画面作成
    tki = tkinter.Tk()
    tki.geometry(window_geometry)
    tki.title(directory.appname)

    # 学籍番号GUI
    id_label = tkinter.Label(text='学籍番号')
    id_label.place(x=id_label_x, y=id_content_y)

    id_txt = tkinter.Entry(width=txt_box_width)
    id_txt.insert(tkinter.END, student_id)
    id_txt.place(x=id_txt_x, y=id_content_y)


    # パスワードGUI
    password_label = tkinter.Label(text='パスワード')
    password_label.place(x=password_label_x, y=password_content_y)

    password_txt = tkinter.Entry(width=txt_box_width, show='*')
    password_txt.insert(tkinter.END, password)
    password_txt.place(x=password_txt_x, y=password_content_y)

    # URL GUI
    chapter_url_label = tkinter.Label(text='チャプターのURL')
    chapter_url_label.place(x=chapter_url_label_x, y=chapter_url_content_y)

    chapter_url_txt = tkinter.Entry(width=txt_box_width)
    chapter_url_txt.insert(tkinter.END, chapter_url)
    chapter_url_txt.place(x=chapter_url_txt_x, y=chapter_url_content_y)
    # コントロールキーが押されたときにURLのテキストが選択状態になる
    tki.bind('<Control-Key>', lambda x: chapter_url_txt.focus_set())

    # ログイン方式
    login_option_label = tkinter.Label(text='ログイン方式')
    login_option_label.place(x=login_option_label_x, y=login_option_content_y)

    login_option_var = tkinter.StringVar()
    login_option_box = ttk.Combobox(tki, values=login_option_list, textvariable=login_option_var, width=login_option_box_width)
    login_option_box.insert(tkinter.END, login_option)
    login_option_box.place(x=login_option_box_x, y=login_option_content_y)

    # 通知モードGUI
    notice_box_label = tkinter.Label(text='通知のモード')
    notice_box_label.place(x=notice_box_label_x, y=notice_box_label_y)

    use_sound_notice_var = tkinter.BooleanVar()
    use_sound_notice_box = tkinter.Checkbutton(tki, text='ワッカさん', variable=use_sound_notice_var)
    use_sound_notice_box.place(x=sound_notice_box_x, y=notice_box_y)
    if(use_sound_notice):
        use_sound_notice_box.select()

    use_window_notice_var = tkinter.BooleanVar()
    use_window_notice_box = tkinter.Checkbutton(tki, text='ウィンドウ', variable=use_window_notice_var)
    use_window_notice_box.place(x=window_notice_box_x, y=notice_box_y)
    if(use_window_notice):
        use_window_notice_box.select()

    # ミュートGUI
    mute_sound_var = tkinter.BooleanVar()
    mute_sound_box = tkinter.Checkbutton(tki, text='動画の音をミュートする', variable=mute_sound_var)
    mute_sound_box.place(x=mute_sound_box_x, y=mute_sound_box_y)
    if(mute_sound):
        mute_sound_box.select()

    # 音量GUI
    notice_sound_label = tkinter.Label(text='ワッカさんの声量', font=("MS明朝", "8"))
    notice_sound_label.place(x=sound_label_x, y=sound_label_y)

    notice_sound_scale_widget = tkinter.Scale(tki, orient=tkinter.VERTICAL, from_=sound_widget_from, to=sound_widget_to,
                                            resolution=sound_widget_resolution, length =sound_widget_length)
    notice_sound_scale_widget.place(x=sound_widget_x, y=sound_widget_y)
    notice_sound_scale_widget.set(notice_sound_scale)

    # 設定データ保存GUI
    save_data_var = tkinter.BooleanVar()
    save_data_box = tkinter.Checkbutton(tki, text='次回からもこの設定を利用する', variable=save_data_var)
    save_data_box.place(x=save_data_box_x, y=save_data_box_y)
    save_data_box.select()

    # スタートボタン
    btn = tkinter.Button(tki, text='始める',
                        command=lambda:on_start_btn(id_txt=id_txt, password_txt=password_txt, chapter_url_txt=chapter_url_txt, login_option_var=login_option_var,
                                        use_sound_notice_var=use_sound_notice_var, use_window_notice_var=use_window_notice_var,
                                        notice_sound_scale_widget=notice_sound_scale_widget, save_data_var=save_data_var,
                                        mute_sound_var=mute_sound_var, tki=tki))
    btn.place(x=start_btn_x, y=start_btn_y)
    # スタートボタンが押された時の処理の登録
    tki.bind('<Return>', lambda x: on_start_btn(id_txt=id_txt, password_txt=password_txt, chapter_url_txt=chapter_url_txt, login_option_var=login_option_var,
                                        use_sound_notice_var=use_sound_notice_var, use_window_notice_var=use_window_notice_var,
                                        notice_sound_scale_widget=notice_sound_scale_widget, save_data_var=save_data_var,
                                        mute_sound_var=mute_sound_var, tki=tki))

    #アイコン設定
    tki.iconbitmap(directory.resource_path('icon.ico'))

    # 描画開始
    tki.mainloop()

def on_start_btn(id_txt, password_txt, chapter_url_txt, login_option_var,
                use_sound_notice_var, use_window_notice_var,
                notice_sound_scale_widget, save_data_var, mute_sound_var, tki):

    set_data_from_box(id_txt=id_txt, password_txt=password_txt, chapter_url_txt=chapter_url_txt, login_option_var=login_option_var,
                    use_sound_notice_var=use_sound_notice_var, use_window_notice_var=use_window_notice_var,
                    notice_sound_scale_widget=notice_sound_scale_widget, save_data_var=save_data_var,
                    mute_sound_var=mute_sound_var)
    try_write_data_file()
    tki.destroy()
    open_chrome()

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

    chrome_options = webdriver.ChromeOptions()
    if mute_sound:
        # 音をミュートするモードだったらクロームのオプションで音をミュートする
        chrome_options.add_argument('--mute-audio')

    # オプションをドライバに適用
    driver = webdriver.Chrome(directory.resource_path('chromedriver.exe'), options=options, chrome_options=chrome_options)
    driver.set_window_size(1500, 1000)
    driver.set_window_position(550, 300)

    # N予備校のログイン画面を開く
    driver.get('https://www.nnn.ed.nico/login?next_url=https%3A%2F%2Fwww.nnn.ed.nico%2Fmy_course')
    if login_option == 'N':
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/a').click()
    else:
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/a').click()

    time.sleep(1.5)

    # 学籍番号とパスワードの入力
    send_text('//*[@id="oauth_identifier_loginId"]', student_id, driver)
    send_text('//*[@id="oauth_identifier_password"]', password, driver)
    # ログインボタンをクリック
    driver.find_element(By.XPATH, '//*[@id="oauth_identifier_"]').click()

    # 指定された教材を開く
    driver.get(chapter_url)

    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/form/div[1]/div/div/div[1]/label/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/form/div[1]/div/div/div[2]/label/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/form/div[1]/div/div/div[3]/label/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/form/div[1]/div/div/div[4]/label/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/form/div[1]/div/div/div[5]/label/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/form/div[2]/button').click()
    except:
        None

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

    if(use_sound_notice):
        pygame.mixer.init()
        pygame.mixer.music.load(directory.resource_path('wakka.mp3'))
        pygame.mixer.music.set_volume(notice_sound_scale)
        pygame.mixer.music.play()

    if(use_window_notice):
        notification.notify(
        title = '確認テストまたはレポートに到達しました',
        message = 'Z予備クン帰ってきて気持ち良すぎだろ!',
        app_name = directory.appname,
        app_icon = toast_icon_array[random.randint(0, len(toast_icon_array) - 1)],
        timeout = int(MP3(directory.resource_path('wakka.mp3')).info.length)
        )

if __name__ == '__main__':
    create_window()
