"""
定数を定義したモジュール
"""

from appdirs import user_data_dir
from enum import Enum


class App:
    NAME = "Z予備クン"
    AUTHOR = "IS"


class Path:
    FILE_NAME = "save_data.json"
    DATA_PATH = user_data_dir(App.NAME, App.AUTHOR)


class Save:
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
