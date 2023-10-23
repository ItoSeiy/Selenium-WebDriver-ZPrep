from __future__ import annotations

"""GUIに関する処理を行うモジュール"""

import os
import tkinter
import tkinter.ttk as ttk

from . import const, path, save


def create(save_data: save.SaveData, on_start_button_click):
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
        x=const.Gui.Window.STUDENT_ID_LABEL_POS_X,
        y=const.Gui.Window.STUDENT_ID_CONTENTS_POS_Y,
    )

    # 学籍番号入力UIの作成
    student_id_entry = tkinter.Entry(width=const.Gui.Window.ENTRY_WIDTH)
    student_id_entry.place(
        x=const.Gui.Window.STUDENT_ID_ENTRY_POS_X,
        y=const.Gui.Window.STUDENT_ID_CONTENTS_POS_Y,
    )
    student_id_entry.insert(tkinter.END, save_data.student_id)

    # パスワードラベルの作成
    password_label = tkinter.Label(text=const.Gui.Window.PASSWORD_LABEL_TEXT)
    password_label.place(
        x=const.Gui.Window.PASSWORD_LABEL_POS_X,
        y=const.Gui.Window.PASSWORD_CONTENTS_POS_Y,
    )

    # パスワード入力UIの作成
    password_entry = tkinter.Entry(
        width=const.Gui.Window.ENTRY_WIDTH,
        show=const.Gui.Window.PASSWORD_ENTRY_SHOW_TEXT,
    )
    password_entry.place(
        x=const.Gui.Window.PASSWORD_ENTRY_POS_X,
        y=const.Gui.Window.PASSWORD_CONTENTS_POS_Y,
    )
    password_entry.insert(tkinter.END, save_data.password)

    # チャプターURLラベルの作成
    chapter_url_label = tkinter.Label(text=const.Gui.Window.CHAPTER_URL_LABEL_TEXT)
    chapter_url_label.place(
        x=const.Gui.Window.CHAPTER_URL_LABEL_POS_X,
        y=const.Gui.Window.CHAPTER_URL_CONTENTS_POS_Y,
    )

    # チャプターURL入力UIの作成
    chapter_url_entry = tkinter.Entry(width=const.Gui.Window.ENTRY_WIDTH)
    chapter_url_entry.place(
        x=const.Gui.Window.CHAPTER_URL_ENTRY_POS_X,
        y=const.Gui.Window.CHAPTER_URL_CONTENTS_POS_Y,
    )
    chapter_url_entry.insert(tkinter.END, save_data.chapter_url)
    # コントロールキーが押されたときにURLの入力UIを選択する
    tki.bind(
        const.Gui.Window.CHAPTER_URL_ENTRY_SELECT_KEY,
        lambda x: chapter_url_entry.focus_set(),
    )

    # ログイン種別のラベルの作成
    login_kind_label = tkinter.Label(text=const.Gui.Window.LOGIN_KIND_LABEL_TEXT)
    login_kind_label.place(
        x=const.Gui.Window.LOGIN_KIND_LABEL_POS_X,
        y=const.Gui.Window.LOGIN_KIND_CONTENTS_POS_Y,
    )

    # ログイン種別の選択ドロップダウンUIの作成
    login_kind_combobox = ttk.Combobox(
        tki,
        values=const.Gui.Window.LOGIN_KIND_LIST,
        width=const.Gui.Window.LOGIN_KIND_COMBOBOX_WIDTH,
    )
    login_kind_combobox.place(
        x=const.Gui.Window.LOGIN_KIND_COMBOBOX_POS_X,
        y=const.Gui.Window.LOGIN_KIND_CONTENTS_POS_Y,
    )
    login_kind_combobox.insert(tkinter.END, save_data.login_kind.value)

    # 通知モードのラベルの作成
    notice_mode_label = tkinter.Label(text=const.Gui.Window.NOTICE_MODE_LABEL_TEXT)
    notice_mode_label.place(
        x=const.Gui.Window.NOTICE_MODE_CONTENTS_POS_X,
        y=const.Gui.Window.NOTICE_MODE_CONTENTS_POS_Y,
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
        x=const.Gui.Window.NOTICE_MODE_SOUND_CHECKBOX_POS_X,
        y=const.Gui.Window.NOTICE_MODE_CONTENTS_POS_Y,
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
        x=const.Gui.Window.NOTICE_MODE_WINDOW_CHECKBOX_POS_X,
        y=const.Gui.Window.NOTICE_MODE_CONTENTS_POS_Y,
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
        x=const.Gui.Window.MUTE_VIDEO_CHECKBOX_POS_X,
        y=const.Gui.Window.MUTE_VIDEO_CHECKBOX_POS_Y,
    )
    if save_data.mute_video == True:
        mute_mode_checkbutton.select()

    # 通知音量のラベルの作成
    notice_sound_scale_label = tkinter.Label(
        text=const.Gui.Window.NOTICE_SOUND_SCALE_LABEL_TEXT
    )
    notice_sound_scale_label.place(
        x=const.Gui.Window.NOTICE_SOUND_SCALE_LABEL_POS_X,
        y=const.Gui.Window.NOTICE_SOUND_SCALE_LABEL_POS_Y,
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
        x=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_POS_X,
        y=const.Gui.Window.NOTICE_SOUND_SCALE_SLIDER_POS_Y,
    )
    notice_sound_scale_slider.set(save_data.notice_sound_scale)

    # 設定保存のチェックボックスのBooleanVarの作成
    save_setting_boolean_var = tkinter.BooleanVar()
    # 設定保存のチェックボックスの作成
    save_setting_checkbutton = tkinter.Checkbutton(
        tki,
        text=const.Gui.Window.SAVE_SETTING_LABEL_TEXT,
        variable=save_setting_boolean_var,
    )
    save_setting_checkbutton.place(
        x=const.Gui.Window.SAVE_SETTING_BUTTON_POS_X,
        y=const.Gui.Window.SAVE_SETTING_BUTTON_POS_Y,
    )
    save_setting_checkbutton.select()

    # 開始ボタンの作成
    start_button = tkinter.Button(
        tki,
        text=const.Gui.Window.START_BUTTON_TEXT,
        command=lambda: _on_start_button_click(
            tki=tki,
            save_setting=save_setting_boolean_var.get(),
            new_save_data=save.SaveData(
                student_id=student_id_entry.get(),
                password=password_entry.get(),
                login_kind=const.Save.LoginKind(login_kind_combobox.get()),
                chapter_url=chapter_url_entry.get(),
                use_sound_notice=notice_mode_sound_boolean_var.get(),
                use_window_notice=notice_mode_window_boolean_var.get(),
                mute_video=mute_mode_boolean_var.get(),
                notice_sound_scale=notice_sound_scale_slider.get(),
            ),
            on_start_button_click=on_start_button_click,
        ),
    )
    start_button.place(
        x=const.Gui.Window.START_BUTTON_POS_X,
        y=const.Gui.Window.START_BUTTON_POS_Y,
    )

    # 開始ボタンが実行されるキーを設定する
    tki.bind(
        const.Gui.Window.START_BUTTON_EXECUTE_KEY,
        lambda x: _on_start_button_click(
            tki=tki,
            save_setting=save_setting_boolean_var.get(),
            new_save_data=save.SaveData(
                student_id=student_id_entry.get(),
                password=password_entry.get(),
                login_kind=const.Save.LoginKind.S,
                chapter_url=chapter_url_entry.get(),
                use_sound_notice=notice_mode_sound_boolean_var.get(),
                use_window_notice=notice_mode_window_boolean_var.get(),
                mute_video=mute_mode_boolean_var.get(),
                notice_sound_scale=notice_sound_scale_slider.get(),
            ),
            on_start_button_click=on_start_button_click,
        ),
    )

    # アイコン画像の絶対パスを取得
    icon_file_path = path.get_assets_path("icon/icon.ico")
    # アイコン設定
    tki.iconbitmap(icon_file_path)

    # ウィンドウを表示する
    tki.mainloop()


def _on_start_button_click(
    tki: tkinter.Tk,
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

    if save_setting == True:
        # 設定を保存する場合はon_start_button_clickにnew_save_dataを渡す
        on_start_button_click(new_save_data)
    else:
        # 設定を保存しない場合は on_start_button_clickにはなにも渡さない
        on_start_button_click(None)
    tki.destroy()
