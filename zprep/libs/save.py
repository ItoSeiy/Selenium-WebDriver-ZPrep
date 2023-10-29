from __future__ import annotations

"""セーブデータ関連を扱うモジュール"""

import json
import os

from . import const


class SaveData:
    """セーブデータクラス"""

    def __init__(
        self,
        student_id: str = "",
        password: str = "",
        chapter_url: str = "your,\nurl",
        max_playing_count: int = 50,
        time_out: float = 5.0,
        chrome_window_pos: str = "550x300",
        chrome_window_size: tuple = "1500x1000",
        use_sound_notice: bool = True,
        use_window_notice: bool = True,
        mute_video: bool = True,
        notice_sound_scale: float = 0.5,
    ):
        self.login_info = {}
        self.login_info = {
            const.Save.SaveDataJsonKey.String.STUDENT_ID: student_id,
            const.Save.SaveDataJsonKey.String.PASSWORD: password,
        }

        self.option = {}
        self.option = {
            const.Save.SaveDataJsonKey.String.CHATPER_URL: chapter_url,
            const.Save.SaveDataJsonKey.String.MAX_PLAYING_COUNT: max_playing_count,
            const.Save.SaveDataJsonKey.String.TIME_OUT: time_out,
            const.Save.SaveDataJsonKey.String.CHROME_WINDOW_POS: chrome_window_pos,
            const.Save.SaveDataJsonKey.String.CHROME_WINDOW_SIZE: chrome_window_size,
            const.Save.SaveDataJsonKey.String.USE_SOUND_NOTICE: use_sound_notice,
            const.Save.SaveDataJsonKey.String.USE_WINDOW_NOTICE: use_window_notice,
            const.Save.SaveDataJsonKey.String.MUTE_VIDEO: mute_video,
            const.Save.SaveDataJsonKey.String.NOTICE_SOUND_SCALE: notice_sound_scale,
        }

    @staticmethod
    def get_from_json(path: str, file_name: str, encoding="utf-8") -> SaveData:
        """セーブデータをJSONから取得する

        Args:
            path (str): 保存先のJSONのパス
            file_name (str): 保存先のJSONのファイル名
            encoding (str, optional): 開く際の文字コード. デフォルト : "utf-8".

        Returns:
            SaveData: セーブデータ
        """

        try:
            # ファイルを開き、jsonファイルを読み込む
            with open(f"{path}/{file_name}", encoding=encoding) as file:
                # JSON文字列をSaveDataに変換(デコード)する
                dec = json.loads(file.read())
                return SaveData(
                    student_id=dec[const.Save.SaveDataJsonKey.Object.LOGIN_INFO][
                        const.Save.SaveDataJsonKey.String.STUDENT_ID
                    ],
                    password=dec[const.Save.SaveDataJsonKey.Object.LOGIN_INFO][
                        const.Save.SaveDataJsonKey.String.PASSWORD
                    ],
                    chapter_url=dec[const.Save.SaveDataJsonKey.Object.OPTION][
                        const.Save.SaveDataJsonKey.String.CHATPER_URL
                    ],
                    max_playing_count=int(
                        dec[const.Save.SaveDataJsonKey.Object.OPTION][
                            const.Save.SaveDataJsonKey.String.MAX_PLAYING_COUNT
                        ]
                    ),
                    time_out=float(
                        dec[const.Save.SaveDataJsonKey.Object.OPTION][
                            const.Save.SaveDataJsonKey.String.TIME_OUT
                        ]
                    ),
                    chrome_window_pos=
                        dec[const.Save.SaveDataJsonKey.Object.OPTION][
                            const.Save.SaveDataJsonKey.String.CHROME_WINDOW_POS
                    ],
                    chrome_window_size=
                        dec[const.Save.SaveDataJsonKey.Object.OPTION][
                            const.Save.SaveDataJsonKey.String.CHROME_WINDOW_SIZE
                    ],
                    use_sound_notice=bool(
                        dec[const.Save.SaveDataJsonKey.Object.OPTION][
                            const.Save.SaveDataJsonKey.String.USE_SOUND_NOTICE
                        ]
                    ),
                    use_window_notice=bool(
                        dec[const.Save.SaveDataJsonKey.Object.OPTION][
                            const.Save.SaveDataJsonKey.String.USE_WINDOW_NOTICE
                        ]
                    ),
                    mute_video=bool(
                        dec[const.Save.SaveDataJsonKey.Object.OPTION][
                            const.Save.SaveDataJsonKey.String.MUTE_VIDEO
                        ]
                    ),
                    notice_sound_scale=float(
                        dec[const.Save.SaveDataJsonKey.Object.OPTION][
                            const.Save.SaveDataJsonKey.String.NOTICE_SOUND_SCALE
                        ]
                    ),
                )
        except (FileNotFoundError, KeyError):
            # ファイルが存在しない場合は空なセーブデータを返す
            return SaveData()

    @staticmethod
    def save_to_json(save_data: SaveData, path: str, file_name: str):
        """セーブデータをJsonに保存する"""

        # SaveDataが持つ値すべての値(__dict__)をJSON形式に変換(エンコード)する
        json_str = json.dumps(save_data.__dict__)

        """
        openの第二引数 'w+' は下記のようなファイルの読み書きのモードを指定している
        mode=	説明
        r	読み込み
        w	書き込み（新規作成）
        a	追加書き込み
        r+	既存ファイルの読み書き
        w+	ファイルの読み書き（新規作成）
        a+	追記・読み書き
        t	テキストモード
        b	バイナリモード
        """
        # ファイルを開き、jsonファイルを書き込み、保存する
        with open(f"{path}/{file_name}", "w+") as file:
            file.write(json_str)
            file.close()

    @property
    def student_id(self) -> str:
        """学籍番号を取得する"""
        return self.login_info[const.Save.SaveDataJsonKey.String.STUDENT_ID]

    @property
    def password(self) -> str:
        """パスワードを取得する"""
        return self.login_info[const.Save.SaveDataJsonKey.String.PASSWORD]

    @property
    def chapter_url_raw_list(self) -> list[str]:
        """チャプターURLを未整形のリストとして取得する"""
        return self.option[const.Save.SaveDataJsonKey.String.CHATPER_URL]

    @property
    def chapter_url_list(self) -> list[str]:
        """チャプターURLをリストとして取得する"""
        return str(self.option[const.Save.SaveDataJsonKey.String.CHATPER_URL]
                    ).replace(' ', '').replace('　', '').replace('\t', '').replace('\n', '').split(',')


    @property
    def max_playing_count(self) -> int:
        """同時に流せる動画の数を取得する"""
        return int(self.option[const.Save.SaveDataJsonKey.String.MAX_PLAYING_COUNT])

    @property
    def time_out(self) -> float:
        """タイムアウトを取得する"""
        return float(self.option[const.Save.SaveDataJsonKey.String.TIME_OUT])

    @property
    def chrome_window_pos(self) -> tuple:
        """Chromeのウィンドウの位置を取得する"""

        splited_pos = self.option[const.Save.SaveDataJsonKey.String.CHROME_WINDOW_POS].split('x')

        return (splited_pos[0], splited_pos[1])

    @property
    def chrome_window_size(self) -> tuple:
        """Chromeのウィンドウのサイズを取得する"""

        splited_pos = self.option[const.Save.SaveDataJsonKey.String.CHROME_WINDOW_SIZE].split('x')

        return (splited_pos[0], splited_pos[1])

    @property
    def use_sound_notice(self) -> bool:
        """音声通知を使用するかを取得する"""
        return bool(self.option[const.Save.SaveDataJsonKey.String.USE_SOUND_NOTICE])

    @property
    def use_window_notice(self) -> bool:
        """ウィンドウ通知を使用するかを取得する"""
        return bool(self.option[const.Save.SaveDataJsonKey.String.USE_WINDOW_NOTICE])

    @property
    def mute_video(self) -> bool:
        """動画をミュートするかを取得する"""
        return bool(self.option[const.Save.SaveDataJsonKey.String.MUTE_VIDEO])

    @property
    def notice_sound_scale(self) -> float:
        """通知音量を取得する"""
        return float(self.option[const.Save.SaveDataJsonKey.String.NOTICE_SOUND_SCALE])
