from __future__ import annotations

"""GUIに関する処理を行うモジュール"""

import webbrowser
import tkinter
from tkinter import scrolledtext
from typing import Callable

from . import const, path, save


def create(
    save_data: save.SaveData, on_start_button_click: Callable[[bool, save.SaveData], None]
):
    """_summary_

    Args:
        save_data (save.SaveData): _description_
    """
    # ベースUIの作成
    tki = tkinter.Tk()
    tki.title(const.App.NAME)
    tki.geometry(const.Gui.Window.WINDOW_GEOMETRY)

    # 学籍番号ラベルの作成
    student_id_label = tkinter.Label(text=const.Gui.Window.STUDENT_ID_LABEL_TEXT)
    student_id_label.place(
        x=const.Gui.Window.STUDENT_ID_LABEL_POS[0],
        y=const.Gui.Window.STUDENT_ID_LABEL_POS[1],
    )

    # 学籍番号入力UIの作成
    student_id_entry = tkinter.Entry(width=const.Gui.Window.ENTRY_WIDTH)
    student_id_entry.place(
        x=const.Gui.Window.STUDENT_ID_ENTRY_POS[0],
        y=const.Gui.Window.STUDENT_ID_ENTRY_POS[1],
    )
    student_id_entry.insert(tkinter.END, save_data.student_id)

    # パスワードラベルの作成
    password_label = tkinter.Label(text=const.Gui.Window.PASSWORD_LABEL_TEXT)
    password_label.place(
        x=const.Gui.Window.PASSWORD_LABEL_POS[0],
        y=const.Gui.Window.PASSWORD_LABEL_POS[1],
    )

    # パスワード入力UIの作成
    password_entry = tkinter.Entry(
        width=const.Gui.Window.ENTRY_WIDTH,
        show=const.Gui.Window.PASSWORD_ENTRY_SHOW_TEXT,
    )
    password_entry.place(
        x=const.Gui.Window.PASSWORD_ENTRY_POS[0],
        y=const.Gui.Window.PASSWORD_ENTRY_POS[1],
    )
    password_entry.insert(tkinter.END, save_data.password)

    # チャプターURLラベルの作成
    chapter_url_label = tkinter.Label(text=const.Gui.Window.CHAPTER_URL_LABEL_TEXT)
    chapter_url_label.place(
        x=const.Gui.Window.CHAPTER_URL_LABEL_POS[0],
        y=const.Gui.Window.CHAPTER_URL_LABEL_POS[1],
    )

    # チャプターURL入力UIの作成
    chapter_url_scrolled_entry = scrolledtext.ScrolledText(tki, width=17, height=5)
    chapter_url_scrolled_entry.place(
        x=const.Gui.Window.CHAPTER_URL_ENTRY_POS[0],
        y=const.Gui.Window.CHAPTER_URL_ENTRY_POS[1],
    )
    chapter_url_scrolled_entry.insert(tkinter.END, save_data.chapter_url_raw_list)
    # コントロールキーが押されたときにURLの入力UIを選択する
    tki.bind(
        const.Gui.Window.CHAPTER_URL_ENTRY_SELECT_KEY,
        lambda x: chapter_url_scrolled_entry.focus_set(),
    )

    # 再生できる動画の上限数のラベルの作成
    max_playing_count_label = tkinter.Label(
        text=const.Gui.Window.MAX_PLAYING_COUNT_LABEL_TEXT
    )
    max_playing_count_label.place(
        x=const.Gui.Window.MAX_PLAYING_COUNT_LABEL_POS[0],
        y=const.Gui.Window.MAX_PLAYING_COUNT_LABEL_POS[1],
    )
    # 再生できる動画の上限数の入力UIの作成
    max_playing_count_entry = tkinter.Entry(width=const.Gui.Window.ENTRY_WIDTH)
    max_playing_count_entry.place(
        x=const.Gui.Window.MAX_PLAYING_COUNT_ENTRY_POS[0],
        y=const.Gui.Window.MAX_PLAYING_COUNT_ENTRY_POS[1],
    )
    max_playing_count_entry.insert(tkinter.END, save_data.max_playing_count)

    # タイムアウトのラベルの作成
    time_out_label = tkinter.Label(
        text=const.Gui.Window.TIME_OUT_LABEL_TEXT,
        fg=const.Gui.Window.TIME_OUT_LABEL_COLOR,
    )
    time_out_label.place(
        x=const.Gui.Window.TIME_OUT_LABEL_POS[0],
        y=const.Gui.Window.TIME_OUT_LABEL_POS[1],
    )
    # タイムアウトのラベルをクリックしたときに説明ページを開く
    time_out_label.bind(
        const.Gui.Window.TIME_OUT_LABEL_CLICK_KEY,
        lambda x: webbrowser.open(const.Gui.Window.TIME_OUT_LABEL_CLICK_URL),
    )

    # タイムアウト入力UIの作成
    time_out_entry = tkinter.Entry(width=const.Gui.Window.ENTRY_WIDTH)
    time_out_entry.place(
        x=const.Gui.Window.TIME_OUT_ENTRY_POS[0],
        y=const.Gui.Window.TIME_OUT_ENTRY_POS[1],
    )
    time_out_entry.insert(tkinter.END, save_data.time_out)

    # Chromeのウィンドウの位置のラベルの作成
    chrome_window_pos_label = tkinter.Label(
        text=const.Gui.Window.CHROME_WINDOW_POS_LABEL_TEXT
    )
    chrome_window_pos_label.place(
        x=const.Gui.Window.CHROME_WINDOW_POS_LABEL_POS[0],
        y=const.Gui.Window.CHROME_WINDOW_POS_LABEL_POS[1],
    )
    # Chromeのウィンドウの位置の入力UIの作成
    chrome_window_pos_entry = tkinter.Entry(width=const.Gui.Window.ENTRY_WIDTH)
    chrome_window_pos_entry.place(
        x=const.Gui.Window.CHROME_WINDOW_POS_ENTRY_POS[0],
        y=const.Gui.Window.CHROME_WINDOW_POS_ENTRY_POS[1],
    )
    chrome_window_pos_entry.insert(tkinter.END, f"{save_data.chrome_window_pos[0] + 'x' + save_data.chrome_window_pos[1]}")

    # Chromeのウィンドウのサイズのラベルの作成
    chrome_window_size_label = tkinter.Label(
        text=const.Gui.Window.CHROME_WINDOW_SIZE_LABEL_TEXT
    )
    chrome_window_size_label.place(
        x=const.Gui.Window.CHROME_WINDOW_SIZE_LABEL_POS[0],
        y=const.Gui.Window.CHROME_WINDOW_SIZE_LABEL_POS[1],
    )
    # Chromeのウィンドウのサイズの入力UIの作成
    chrome_window_size_entry = tkinter.Entry(width=const.Gui.Window.ENTRY_WIDTH)
    chrome_window_size_entry.place(
        x=const.Gui.Window.CHROME_WINDOW_SIZE_ENTRY_POS[0],
        y=const.Gui.Window.CHROME_WINDOW_SIZE_ENTRY_POS[1],
    )
    chrome_window_size_entry.insert(tkinter.END, f"{save_data.chrome_window_size[0] + 'x' + save_data.chrome_window_size[1]}")

    # 通知モードのラベルの作成
    notice_mode_label = tkinter.Label(text=const.Gui.Window.NOTICE_MODE_LABEL_TEXT)
    notice_mode_label.place(
        x=const.Gui.Window.NOTICE_MODE_LABEL_POS[0],
        y=const.Gui.Window.NOTICE_MODE_LABEL_POS[1],
    )

    # 通知モード(サウンド)のBooleanVarの作成
    notice_mode_sound_boolean_var = tkinter.BooleanVar()
    # 通知モード(サウンド)のチェックボックスの作成
    notice_mode_sound_checkbutton = tkinter.Checkbutton(
        tki,
        text=const.Gui.Window.NOTICE_MODE_SOUND_CHECKBOX_TEXT,
        variable=notice_mode_sound_boolean_var,
    )
    notice_mode_sound_checkbutton.place(
        x=const.Gui.Window.NOTICE_MODE_SOUND_CHECKBOX_POS[0],
        y=const.Gui.Window.NOTICE_MODE_SOUND_CHECKBOX_POS[1],
    )
    if save_data.use_sound_notice == True:
        notice_mode_sound_checkbutton.select()

    # 通知モード(ウィンドウ)のBooleanVarの作成
    notice_mode_window_boolean_var = tkinter.BooleanVar()
    # 通知モード(ウィンドウ)のチェックボックスの作成
    notice_mode_window_checkbutton = tkinter.Checkbutton(
        tki,
        text=const.Gui.Window.NOTICE_MODE_WINDOW_CHECKBOX_TEXT,
        variable=notice_mode_window_boolean_var,
    )
    notice_mode_window_checkbutton.place(
        x=const.Gui.Window.NOTICE_MODE_WINDOW_CHECKBOX_POS[0],
        y=const.Gui.Window.NOTICE_MODE_WINDOW_CHECKBOX_POS[1],
    )
    if save_data.use_window_notice == True:
        notice_mode_window_checkbutton.select()

    # ミュートモードのBooleanVarの作成
    mute_mode_boolean_var = tkinter.BooleanVar()
    # ミュートモードのチェックボックスの作成
    mute_mode_checkbutton = tkinter.Checkbutton(
        tki, text=const.Gui.Window.MUTE_VIDEO_LABEL_TEXT, variable=mute_mode_boolean_var
    )
    mute_mode_checkbutton.place(
        x=const.Gui.Window.MUTE_VIDEO_CHECKBOX_POS[0],
        y=const.Gui.Window.MUTE_VIDEO_CHECKBOX_POS[1],
    )
    if save_data.mute_video == True:
        mute_mode_checkbutton.select()

    # 設定保存のチェックボックスのBooleanVarの作成
    save_setting_boolean_var = tkinter.BooleanVar()
    # 設定保存のチェックボックスの作成
    save_setting_checkbutton = tkinter.Checkbutton(
        tki,
        text=const.Gui.Window.SAVE_SETTING_LABEL_TEXT,
        variable=save_setting_boolean_var,
    )
    save_setting_checkbutton.place(
        x=const.Gui.Window.SAVE_SETTING_BUTTON_POS[0],
        y=const.Gui.Window.SAVE_SETTING_BUTTON_POS[1],
    )
    save_setting_checkbutton.select()

    # 通知音量のラベルの作成
    notice_sound_scale_label = tkinter.Label(
        text=const.Gui.Window.NOTICE_SOUND_SCALE_LABEL_TEXT
    )
    notice_sound_scale_label.place(
        x=const.Gui.Window.NOTICE_SOUND_SCALE_LABEL_POS[0],
        y=const.Gui.Window.NOTICE_SOUND_SCALE_LABEL_POS[1],
    )

    # 通知音量のスライダーの作成
    notice_sound_scale_slider = tkinter.Scale(
        tki,
        orient=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_ORIENT,
        from_=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_FROM,
        to=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_TO,
        resolution=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_RESOLUTION,
        length=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_LENGTH,
    )
    notice_sound_scale_slider.place(
        x=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_POS[0],
        y=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_POS[1],
    )
    notice_sound_scale_slider.set(save_data.notice_sound_scale)

    # 開始ボタンの作成
    start_button = tkinter.Button(
        tki,
        text=const.Gui.Window.START_BUTTON_TEXT,
        command=lambda: _on_start_button_click(
            save_setting=save_setting_boolean_var.get(),
            new_save_data=save.SaveData(
                student_id=student_id_entry.get(),
                password=password_entry.get(),
                chapter_url=chapter_url_scrolled_entry.get(0., tkinter.END),
                max_playing_count=max_playing_count_entry.get(),
                time_out=time_out_entry.get(),
                chrome_window_pos=chrome_window_pos_entry.get(),
                chrome_window_size=chrome_window_size_entry.get(),
                use_sound_notice=notice_mode_sound_boolean_var.get(),
                use_window_notice=notice_mode_window_boolean_var.get(),
                mute_video=mute_mode_boolean_var.get(),
                notice_sound_scale=notice_sound_scale_slider.get(),
            ),
            on_start_button_click=on_start_button_click,
        ),
    )
    start_button.place(
        x=const.Gui.Window.START_BUTTON_POS[0],
        y=const.Gui.Window.START_BUTTON_POS[1],
        width=const.Gui.Window.START_BUTTON_WIDTH,
    )

    # 開始ボタンが実行されるキーを設定する
    tki.bind(
        const.Gui.Window.START_BUTTON_EXECUTE_KEY,
        lambda x: _on_start_button_click(
            save_setting=save_setting_boolean_var.get(),
            new_save_data=save.SaveData(
                student_id=student_id_entry.get(),
                password=password_entry.get(),
                chapter_url=chapter_url_scrolled_entry.get(0., tkinter.END),
                max_playing_count=max_playing_count_entry.get(),
                time_out=time_out_entry.get(),
                chrome_window_pos=chrome_window_pos_entry.get(),
                chrome_window_size=chrome_window_size_entry.get(),
                use_sound_notice=notice_mode_sound_boolean_var.get(),
                use_window_notice=notice_mode_window_boolean_var.get(),
                mute_video=mute_mode_boolean_var.get(),
                notice_sound_scale=notice_sound_scale_slider.get(),
            ),
            on_start_button_click=on_start_button_click,
        ),
    )

    # アイコン画像の絶対パスを取得
    icon_file_path = path.get_assets_path(const.Gui.Window.ICON_PATH)
    # アイコン設定
    tki.iconbitmap(icon_file_path)

    # ウィンドウを表示する
    tki.mainloop()


def _on_start_button_click(
    save_setting: bool,
    new_save_data: save.SaveData,
    on_start_button_click,
):
    """開始ボタン押下時の処理

    Args:
        tki (tkinter.Tk): tkinter\n
        save_setting (bool): 設定を保存するかどうか\n
        new_save_data (save.SaveData): 開始ボタン押下時点での設定\n
        on_start_button_click (function): 開始ボタン押下時の処理\n
    """

    on_start_button_click(save_setting, new_save_data)
