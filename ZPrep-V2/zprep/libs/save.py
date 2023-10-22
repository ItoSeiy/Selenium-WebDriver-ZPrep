'''
セーブデータ関連を扱うモジュール
'''

import json
import const

class SaveData:
    def __init__(self, student_id : str, password : str, login_kind : const.Save.LoginKind,
                use_sound_notice : bool, use_window_notice : bool, notice_sound_scale : float, mute_video : bool):

        self.login_info[const.Save.SaveDataJsonKey.Object.LOGIN_INFO] = {
            const.Save.SaveDataJsonKey.String.STUDENT_ID: student_id,
            const.Save.SaveDataJsonKey.String.PASSWORD: password,
            const.Save.SaveDataJsonKey.String.LOGIN_KIND: login_kind.value
        }

        self.option[const.Save.SaveDataJsonKey.Object.OPTION] = {
            const.Save.SaveDataJsonKey.String.USE_SOUND_NOTICE: use_sound_notice,
            const.Save.SaveDataJsonKey.String.USE_WINDOW_NOTICE: use_window_notice,
            const.Save.SaveDataJsonKey.String.NOTICE_SOUND_SCALE: notice_sound_scale,
            const.Save.SaveDataJsonKey.String.MUTE_VIDEO: mute_video
        }

    @staticmethod
    def load_from_json(self, path : str, file_name : str, encoding = 'utf-8'):
        """
        セーブデータをJsonから読み込む
        """

        with open(path + '/' + file_name, mode='r', encoding=encoding) as f:
            json_data = json.load(f)

        self.login_info = json_data[const.Save.SaveDataJsonKey.Object.LOGIN_INFO]
        self.option = json_data[const.Save.SaveDataJsonKey.Object.OPTION]