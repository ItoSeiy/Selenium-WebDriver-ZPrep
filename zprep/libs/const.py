"""
定数を定義したモジュール

Appクラスを除く一階層目のクラス名は関係性が高いモジュールと同様にしている
"""

import tkinter
from enum import Enum

from appdirs import user_data_dir


class App:
    """アプリケーションの情報を定義したクラス"""

    NAME = "Z予備クン"
    AUTHOR = "IS"


class Gui:
    class Window:
        """GUIに関する定数を定義したクラス"""

        # 基本サイズ
        WINDOW_GEOMETRY = "320x265"
        # 入力UIの幅
        ENTRY_WIDTH = 20
        # アイコンの相対パス
        ICON_PATH = "assets/icon/icon.ico"
        # アイコン01の相対パス
        ICON_PATH_01 = "assets/icon/wakka01.ico"
        # アイコン02のパス
        ICON_PATH_02 = "assets/icon/wakka02.ico"

        # 学籍番号ラベルのテキスト
        STUDENT_ID_LABEL_TEXT = "学籍番号"
        # 学籍番号ラベルの座標
        STUDENT_ID_LABEL_POS = (30, 30)
        # 学籍番号入力UIの座標
        STUDENT_ID_ENTRY_POS = (100, 30)

        # パスワードラベルのテキスト
        PASSWORD_LABEL_TEXT = "パスワード"
        # パスワードラベルの座標
        PASSWORD_LABEL_POS = (30, 60)
        # パスワード入力UIの座標
        PASSWORD_ENTRY_POS = (100, 60)
        # パスワードが入力されている時に表示する文字
        PASSWORD_ENTRY_SHOW_TEXT = "*"

        # チャプターURLラベルのテキスト
        CHAPTER_URL_LABEL_TEXT = "チャプターのURL"
        # チャプターURL入力が選択されるキー
        CHAPTER_URL_ENTRY_SELECT_KEY = "<Control-Key>"
        # チャプターURLラベルの座標
        CHAPTER_URL_LABEL_POS = (5, 90)
        # チャプターURL入力UIの座標
        CHAPTER_URL_ENTRY_POS = (100, 90)

        # ログイン種別ラベルのテキスト
        LOGIN_KIND_LABEL_TEXT = "ログイン種別"
        # ログイン種別のドロップダウンの種類
        LOGIN_KIND_LIST = ["N", "S"]
        # ログイン種別のドロップダウンの幅
        LOGIN_KIND_COMBOBOX_WIDTH = 17
        # ログイン種別ラベルの座標
        LOGIN_KIND_LABEL_POS = (20, 120)
        # ログイン種別ドロップダウンUIの座標
        LOGIN_KIND_COMBOBOX_POS = (100, 120)

        # 通知モードのテキスト
        NOTICE_MODE_LABEL_TEXT = "通知モード"
        # 通知モードラベルの座標
        NOTICE_MODE_LABEL_POS = (35, 150)

        # サウンドの通知モードのテキスト
        NOTICE_MODE_SOUND_CHECKBOX_TEXT = "ワッカさん"
        # ウィンドウの通知モードのテキスト
        NOTICE_MODE_WINDOW_CHECKBOX_TEXT = "ウィンドウ"
        # サウンドの通知モードのチェックボックスの座標
        NOTICE_MODE_SOUND_CHECKBOX_POS = (110, 150)
        # ウィンドウの通知モードのチェックボックスの座標
        NOTICE_MODE_WINDOW_CHECKBOX_POS = (110, 180)

        # 動画のミュートのテキスト
        MUTE_VIDEO_LABEL_TEXT = "動画の音をミュートする"
        # 動画のミュートのチェックボックスの座標
        MUTE_VIDEO_CHECKBOX_POS = (95, 172)

        # 設定保存のラベルのテキスト
        SAVE_SETTING_LABEL_TEXT = "次回からもこの設定を利用する"
        # 設定保存ボタンの座標
        SAVE_SETTING_BUTTON_POS = (65, 197)

        # 通知音量のテキスト
        NOTICE_SOUND_SCALE_LABEL_TEXT = "ワッカさんの声量"
        # 通知音量のラベルの座標
        NOTICE_SOUND_SCALE_LABEL_POS = (230, 28)

        # 通知音量のスライドバーの座標
        NOTICE_SOUND_SCALE_SLIDER_POS = (265, 45)
        # 通知音量のスライドバーの向き
        NOTICE_SOUND_SCALE_SLIDER_ORIENT = tkinter.VERTICAL
        # 通知音量のスライドバーの長さ
        NOTICE_SOUND_SCALE_SLIDER_LENGTH = 100
        # 通知音量のスライドバーの開始値
        NOTICE_SOUND_SCALE_SLIDER_FROM = 1.0
        # 通知音量のスライドバーの終了値
        NOTICE_SOUND_SCALE_SLIDER_TO = 0.0
        # 通知音量のスライドバーの刻み幅
        NOTICE_SOUND_SCALE_SLIDER_RESOLUTION = 0.1

        # 開始ボタンのテキスト
        START_BUTTON_TEXT = "開始"
        # 開始ボタンの座標
        START_BUTTON_POS = (140, 225)
        # 開始ボタンが実行されるキー
        START_BUTTON_EXECUTE_KEY = "<Return>"


class Log:
    DEFAULT_LOGGER = "default_logger"
    DEFAULT_LOG_FORMAT = (
        f"%(levelname)-9s  %(asctime)s [%(filename)s:%(lineno)d] %(message)s"
    )

    class Path:
        FILE_NAME = "log.log"
        DATA_PATH = user_data_dir(App.NAME, App.AUTHOR)


class Save:
    class Path:
        FILE_NAME = "save_data.json"
        DATA_PATH = user_data_dir(App.NAME, App.AUTHOR)

    class SaveDataJsonKey:
        """セーブデータのJsonのKeyを定義したクラス"""

        class Object:
            """JsonのObjectのKeyを定義したクラス"""

            LOGIN_INFO = "login_info"
            OPTION = "option"

        class String:
            """JsonのStringのKeyを定義したクラス"""

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
        """ログイン種別を定義したクラス"""

        N = "N"
        S = "S"


class Selenium:
    CHROME_DRIVER_NAME = "chromedriver.exe"

    class Option:
        """Selenium関連のオプション、設定を定義したクラス"""

        # ミュート
        MUTE_AUDIO = "--mute-audio"

        # ログの無効化
        DISABLE_LOGGING = "disable-logging"
        # ログレベル3 (余分なログが出ないレベル)
        LOG_LEVEL_3 = "--log-level=3"
        # 長文ログの無効化
        EXPERMENTAL_OPTION = ("excludeSwitches", ["enable-logging"])

        # タイムアウトまでの時間
        TIME_TO_WAIT = 8

        # ウィンドウサイズ
        WINDOW_SIZE = (1500, 1000)
        # ウィンドウ位置
        WINDOW_POS = (550, 300)

    class Url:
        """URLを定義したクラス"""

        LOGIN = "https://www.nnn.ed.nico/login?next_url=https%3A%2F%2Fwww.nnn.ed.nico%2Fmy_course"

    class XPath:
        """XPathを定義したクラス"""

        def LOGIN_KIND_BUTTON(kind: Save.LoginKind) -> str:
            """ログイン種別のボタンのXPathを返す関数"""

            if kind == Save.LoginKind.N:
                return (
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/a'
                )
            else:
                return (
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/a'
                )

        # 学籍番号入力欄
        STUDENT_ID_FIELD = '//*[@id="oauth_identifier_loginId"]'
        # パスワード入力欄
        PASSWORD_FIELD = '//*[@id="oauth_identifier_password"]'
        # ログインボタン
        LOGIN_BUTTON = '//*[@id="oauth_identifier_"]'

        # 同意チェック項目
        AGREEMENT_ELEMENTS = [
            "/html/body/div[5]/div/div/div/form/div[1]/div/div/div[1]/input",
            "/html/body/div[5]/div/div/div/form/div[1]/div/div/div[2]/input",
            "/html/body/div[5]/div/div/div/form/div[1]/div/div/div[3]/input",
            "/html/body/div[5]/div/div/div/form/div[1]/div/div/div[4]/input",
            "/html/body/div[5]/div/div/div/form/div[1]/div/div/div[5]/input",
        ]
        AGREEMENT_BUTTON = "/html/body/div[5]/div/div/div/form/div[2]/button"

        # 必修教材のみボタン
        ONLY_REQUIRED_SUBJECT_BUTTON = "/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[1]/div[1]/div[2]/div/div[2]/button[1]"

        # 動画、テストのエレメントのリストの格納場所
        SUBJECT_ELEMENTS_CONTAINER = (
            "/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[1]/div[1]/ul"
        )

    class Tag:
        """タグを定義したクラス"""

        LIST_ITEM = "li"

        DIVISION = "div"

        CLASS = "CLASS"

    class SpecificPath:
        """具体的なエレメントまでのパスを定義したクラス"""

        # 動画の視聴判定に必要なエレメントまでのパス
        VIDEO_PLAYED_PATH = (
            "div",
            "div",
            ".sc-aXZVg.sc-gEvEer.sc-lcfvsp-11.dKubqp.fteAEG.hZhBzF",
            ".sc-aXZVg.sc-gEvEer.sc-lcfvsp-12.dKubqp.fteAEG.jrmmTF",
            ".sc-aXZVg.sc-gEvEer.miLza.fteAEG",
            "div",
            "div",
            ".sc-aXZVg.kXcVyQ",
        )

        # エレメントのテスト判定に必要なエレメントまでのパス
        JUDGE_TEST_ELEMENT_PATH = ("div", "div", ".sc-aXZVg.iFkSEV")
