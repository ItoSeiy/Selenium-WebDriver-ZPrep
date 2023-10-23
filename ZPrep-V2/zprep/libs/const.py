"""
定数を定義したモジュール

Appクラスを除く一階層目のクラス名は関係性が高いモジュールと同様にしている
"""

import tkinter
from enum import Enum

from appdirs import user_data_dir


class App:
    """
    アプリケーションの情報を定義したクラス
    """

    NAME = "Z予備クン"
    AUTHOR = "IS"


class Gui:
    class Window:
        """
        GUIに関する定数を定義したクラス
        """

        # 基本サイズ
        WINDOW_GEOMETRY = "320x265"
        # 入力UIの幅
        ENTRY_WIDTH = 20
        # アイコンのパス
        ICON_PATH = "assets/icon/icon.ico"
        # アイコン01のパス
        ICON_PATH_01 = "assets/icon/wakka01.ico"
        # アイコン02のパス
        ICON_PATH_02 = "assets/icon/wakka02.ico"

        # 学籍番号ラベルのテキスト
        STUDENT_ID_LABEL_TEXT = "学籍番号"
        # 学席番号ラベル、入力UIのY座標
        STUDENT_ID_CONTENTS_POS_Y = 30
        # 学籍番号ラベルのX座標
        STUDENT_ID_LABEL_POS_X = 100
        # 学籍番号入力UIのX座標
        STUDENT_ID_ENTRY_POS_X = 30

        # パスワードラベルのテキスト
        PASSWORD_LABEL_TEXT = "パスワード"
        # パスワードラベル、入力UIのY座標
        PASSWORD_CONTENTS_POS_Y = 60
        # パスワードラベルのX座標
        PASSWORD_LABEL_POS_X = 100
        # パスワード入力UIのX座標
        PASSWORD_ENTRY_POS_X = 30
        # パスワードが入力されている時に表示する文字
        PASSWORD_ENTRY_SHOW_TEXT = "*"

        # チャプターURLラベルのテキスト
        CHAPTER_URL_LABEL_TEXT = "チャプターのURL"
        # チャプターURLラベル、入力UIのY座標
        CHAPTER_URL_CONTENTS_POS_Y = 90
        # チャプターURLラベルのX座標
        CHAPTER_URL_LABEL_POS_X = 5
        # チャプターURL入力が選択されるキー
        CHAPTER_URL_ENTRY_SELECT_KEY = "<Control-Key>"
        # チャプターURL入力UIのX座標
        CHAPTER_URL_ENTRY_POS_X = 100

        # ログイン種別ラベルのテキスト
        LOGIN_KIND_LABEL_TEXT = "ログイン種別"
        # ログイン種別ラベル、ドロップダウンのY座標
        LOGIN_KIND_CONTENTS_POS_Y = 120
        # ログイン種別ラベルのX座標
        LOGIN_KIND_LABEL_POS_X = 20
        # ログイン種別のドロップダウンの種類
        LOGIN_KIND_LIST = ["N", "S"]
        # ログイン種別のドロップダウンの幅
        LOGIN_KIND_COMBOBOX_WIDTH = 17
        # ログイン種別ドロップダウンUIのX座標
        LOGIN_KIND_COMBOBOX_POS_X = 100

        # 通知モードのテキスト
        NOTICE_MODE_LABEL_TEXT = "通知モード"
        # 通知モードラベル、チェックボックスのY座標
        NOTICE_MODE_CONTENTS_POS_Y = 150
        # 通知モードラベルのX座標
        NOTICE_MODE_CONTENTS_POS_X = 35

        # サウンドの通知モードのテキスト
        NOTICE_MODE_SOUND_CHECKBOX_TEXT = "ワッカさん"
        # サウンドの通知モードのチェックボックスのX座標
        NOTICE_MODE_SOUND_CHECKBOX_POS_X = 110
        # ウィンドウの通知モードのテキスト
        NOTICE_MODE_WINDOW_CHECKBOX_TEXT = "ウィンドウ"
        # ウィンドウの通知モードのチェックボックスのX座標
        NOTICE_MODE_WINDOW_CHECKBOX_POS_X = 180

        # 通知音量のテキスト
        NOTICE_SOUND_SCALE_LABEL_TEXT = "ワッカさんの声量"
        # 通知音量のラベルのX座標
        NOTICE_SOUND_SCALE_LABEL_POS_X = 230
        # 通知音量のラベルのY座標
        NOTICE_SOUND_SCALE_LABEL_POS_Y = 28
        # 通知音量のスライドバーのX座標
        NOTICE_SOUND_SCALE_SLIDER_POS_X = 265
        # 通知音量のスライドバーのY座標
        NOTICE_SOUND_SCALE_SLIDER_POS_Y = 45
        # 通知音量のスライドバーの長さ
        NOTICE_SOUND_SCALE_SLIDER_LENGTH = 100

        # 動画のミュートのテキスト
        MUTE_VIDEO_LABEL_TEXT = "動画の音をミュートする"
        # 動画のミュートのチェックボックスのX座標
        MUTE_VIDEO_CHECKBOX_POS_X = 95
        # 動画のミュートのチェックボックスのY座標
        MUTE_VIDEO_CHECKBOX_POS_Y = 172

        # 設定保存のラベルのテキスト
        SAVE_SETTING_LABEL_TEXT = "次回からもこの設定を利用する"
        # 設定保存ボタンのX座標
        SAVE_SETTING_BUTTON_POS_X = 65
        # 設定保存ボタンのY座標
        SAVE_SETTING_BUTTON_POS_Y = 197

        # 通知音量のスライドバーの向き
        NOTICE_SOUND_SCALE_SLIDER_ORIENT = tkinter.VERTICAL
        # 通知音量のスライドバーの開始値
        NOTICE_SOUND_SCALE_SLIDER_FROM = 1.0
        # 通知音量のスライドバーの終了値
        NOTICE_SOUND_SCALE_SLIDER_TO = 0.0
        # 通知音量のスライドバーの刻み幅
        NOTICE_SOUND_SCALE_SLIDER_RESOLUTION = 0.1

        # 開始ボタンのテキスト
        START_BUTTON_TEXT = "開始"
        # 開始ボタンのX座標
        START_BUTTON_POS_X = 140
        # 開始ボタンのY座標
        START_BUTTON_POS_Y = 225
        # 開始ボタンが実行されるキー
        START_BUTTON_EXECUTE_KEY = "<Return>"


class Save:
    class Path:
        FILE_NAME = "save_data.json"
        DATA_PATH = user_data_dir(App.NAME, App.AUTHOR)

    class SaveDataJsonKey:
        """
        セーブデータのJsonのKeyを定義したクラス
        """

        class Object:
            """
            JsonのObjectのKeyを定義したクラス
            """

            LOGIN_INFO = "login_info"
            OPTION = "option"

        class String:
            """
            JsonのStringのKeyを定義したクラス
            """

            # login_infoオブジェクトのKey
            STUDENT_ID = "student_id"
            PASSWORD = "password"
            LOGIN_KIND = "login_kind"

            # optionオブジェクトのKey
            CHATPER_URL = "chapter_url"
            USE_SOUND_NOTICE = "use_sound_notice"
            USE_WINDOW_NOTICE = "use_window_notice"
            NOTICE_SOUND_SCALE = "notice_sound_scale"
            MUTE_VIDEO = "mute_video"

    class LoginKind(Enum):
        """
        ログイン種別を定義したクラス
        """

        N = "N"
        S = "S"
