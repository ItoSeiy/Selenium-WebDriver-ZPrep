"""
定数を定義したモジュール

Appクラスを除く一階層目のクラス名は関係性が高いモジュールと同様にしている
"""

import tkinter

from appdirs import user_data_dir


class App:
    """アプリケーションの情報を定義したクラス"""

    NAME = "Z予備クン"
    AUTHOR = "IS"


class Audio:
    """オーディオの情報を定義したクラス"""

    class MP3:
        """MP3の情報を定義したクラス"""

        WAKKA_MP3 = r"audio\wakka.mp3"


class Notify:
    MESSAGE = "作り直しした新生Z予備クンきもちよすぎだろ!!!"
    # 通知用の相対パスのリスト
    ICON_PATH_LIST = [r"icon\wakka01.ico", r"icon\wakka02.ico"]


class Gui:
    class Window:
        """GUIに関する定数を定義したクラス"""

        # 基本サイズ
        WINDOW_GEOMETRY = "350x380"
        # 入力UIの幅
        ENTRY_WIDTH = 20
        # アイコンの相対パス
        ICON_PATH = r"icon\icon.ico"

        # 学籍番号ラベルのテキスト
        STUDENT_ID_LABEL_TEXT = "学籍番号"
        # 学籍番号ラベルの座標
        STUDENT_ID_LABEL_POS = (70, 30)
        # 学籍番号入力UIの座標
        STUDENT_ID_ENTRY_POS = (130, 30)

        # パスワードラベルのテキスト
        PASSWORD_LABEL_TEXT = "パスワード"
        # パスワードラベルの座標
        PASSWORD_LABEL_POS = (70, 60)
        # パスワード入力UIの座標
        PASSWORD_ENTRY_POS = (130, 60)
        # パスワードが入力されている時に表示する文字
        PASSWORD_ENTRY_SHOW_TEXT = "*"

        # チャプターURLラベルのテキスト
        CHAPTER_URL_LABEL_TEXT = "チャプターのURL\n(カンマ区切りで複数入力)"
        # チャプターURL入力が選択されるキー
        CHAPTER_URL_ENTRY_SELECT_KEY = "<Control-Key-a>"
        # チャプターURLラベルの座標
        CHAPTER_URL_LABEL_POS = (0, 90)
        # チャプターURL入力UIの座標
        CHAPTER_URL_ENTRY_POS = (130, 90)

        # 同時に流せる動画の数のラベルのテキスト
        MAX_PLAYING_COUNT_LABEL_TEXT = "同時に流せる動画の数"
        # 同時に流せる動画の数のラベルの座標
        MAX_PLAYING_COUNT_LABEL_POS = (5, 170)
        # 同時に流せる動画の数の入力UIの座標
        MAX_PLAYING_COUNT_ENTRY_POS = (130, 170)

        # タイムアウトのラベルのテキスト
        TIME_OUT_LABEL_TEXT = "タイムアウト(秒)"
        # タイムアウトのラベルが押されるキー
        TIME_OUT_LABEL_CLICK_KEY = "<Button-1>"
        # タイムアウトのラベルの色
        TIME_OUT_LABEL_COLOR = "blue"
        # タイムアウトのラベルが押されたときに飛ぶURL
        TIME_OUT_LABEL_CLICK_URL = r"https://e-words.jp/w/%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%A2%E3%82%A6%E3%83%88.html#:~:text=%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%A2%E3%82%A6%E3%83%88%20%E3%80%90time%20out%E3%80%91&text=IT%E3%81%AE%E5%88%86%E9%87%8E%E3%81%A7%E3%81%AF%E3%80%81%E5%87%A6%E7%90%86,%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%82%92%E6%84%8F%E5%91%B3%E3%81%99%E3%82%8B%E3%80%82"
        # タイムアウトのラベルの座標
        TIME_OUT_LABEL_POS = (45, 200)
        # タイムアウト入力UIの座標
        TIME_OUT_ENTRY_POS = (130, 200)

        # Chromeのウィンドウの位置のラベルのテキスト
        CHROME_WINDOW_POS_LABEL_TEXT = "ウィンドウの初期位置"
        # Chromeのウィンドウの位置のラベルの座標
        CHROME_WINDOW_POS_LABEL_POS = (5, 230)
        # Chromeのウィンドウの位置の入力UIの座標
        CHROME_WINDOW_POS_ENTRY_POS = (130, 230)

        # Chromeのウィンドウのサイズのラベルのテキスト
        CHROME_WINDOW_SIZE_LABEL_TEXT = "ウィンドウの初期サイズ"
        # Chromeのウィンドウのサイズのラベルの座標
        CHROME_WINDOW_SIZE_LABEL_POS = (5, 260)
        # Chromeのウィンドウのサイズの入力UIの座標
        CHROME_WINDOW_SIZE_ENTRY_POS = (130, 260)

        # 通知モードのテキスト
        NOTICE_MODE_LABEL_TEXT = "通知モード"
        # 通知モードラベルの座標
        NOTICE_MODE_LABEL_POS = (30, 290)

        # サウンドの通知モードのテキスト
        NOTICE_MODE_SOUND_CHECKBOX_TEXT = "ワッカさん"
        # ウィンドウの通知モードのテキスト
        NOTICE_MODE_WINDOW_CHECKBOX_TEXT = "ウィンドウ"
        # サウンドの通知モードのチェックボックスの座標
        NOTICE_MODE_SOUND_CHECKBOX_POS = (125, 290)
        # ウィンドウの通知モードのチェックボックスの座標
        NOTICE_MODE_WINDOW_CHECKBOX_POS = (195, 290)

        # 動画のミュートのテキスト
        MUTE_VIDEO_LABEL_TEXT = "動画の音をミュートする"
        # 動画のミュートのチェックボックスの座標
        MUTE_VIDEO_CHECKBOX_POS = (125, 310)

        # 設定保存のラベルのテキスト
        SAVE_SETTING_LABEL_TEXT = "次回からもこの設定を利用する"
        # 設定保存ボタンの座標
        SAVE_SETTING_BUTTON_POS = (125, 310)

        # 通知音量のテキスト
        NOTICE_SOUND_SCALE_LABEL_TEXT = "ワッカさんの声量"
        # 通知音量のラベルの座標
        NOTICE_SOUND_SCALE_LABEL_POS = (260, 28)

        # 通知音量のスライドバーの座標
        NOTICE_SOUND_SCALE_SLIDER_POS = (295, 45)
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
        START_BUTTON_POS = (140, 340)
        # 開始ボタンの幅
        START_BUTTON_WIDTH = 80
        # 開始ボタンが実行されるキー
        START_BUTTON_EXECUTE_KEY = "<Control-Key-Return>"


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

            # optionオブジェクトのKey
            CHATPER_URL = "chapter_url"
            MAX_PLAYING_COUNT = "max_playing_count"
            TIME_OUT = "time_out"
            CHROME_WINDOW_POS = "chrome_window_pos"
            CHROME_WINDOW_SIZE = "chrome_window_size"
            USE_SOUND_NOTICE = "use_sound_notice"
            USE_WINDOW_NOTICE = "use_window_notice"
            NOTICE_SOUND_SCALE = "notice_sound_scale"
            MUTE_VIDEO = "mute_video"


class Selenium:
    class Message:
        ALL_VIDEO_PLAYED_MESSAGE = "全ての動画を視聴しました"
        ALREADY_REACHED_TEST = "既にテストに到達しています"

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

    class Url:
        """URLを定義したクラス"""

        LOGIN = "https://www.nnn.ed.nico/login?next_url=https%3A%2F%2Fwww.nnn.ed.nico%2Fmy_course"

    class XPath:
        """XPathを定義したクラス"""

        def LOGIN_KIND_BUTTON(student_id: str) -> str:
            """ログイン種別のボタンのXPathを返す関数"""

            if "N" in student_id:
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
            '//*[@id="root"]/div/div[2]/div[2]/main/div[2]/div[1]/div[1]/ul'
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

        # 動画時間の取得に必要なエレメントまでのパス
        VIDEO_LENGTH_PATH = ("div", "div", ".sc-aXZVg.iuHQbN")

        # エレメントが未開放かどうかの判定に必要なエレメントまでのパス
        UNOPENED_ELEMENT_PATH = (
            ".sc-aXZVg.sc-gEvEer.hYNtMZ.fteAEG.sc-1otp79h-0.sc-35qwhb-0.evJGlU.hoWVG"
        )
