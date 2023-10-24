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
        login_kind: const.Save.LoginKind = const.Save.LoginKind.S,
        chapter_url: str = "",
        use_sound_notice: bool = True,
        use_window_notice: bool = True,
        mute_video: bool = True,
        notice_sound_scale: float = True,
    ):
        self.login_info = {}
        self.login_info = {
            const.Save.SaveDataJsonKey.String.STUDENT_ID: student_id,
            const.Save.SaveDataJsonKey.String.PASSWORD: password,
            const.Save.SaveDataJsonKey.String.LOGIN_KIND: login_kind.value,
        }

        self.option = {}
        self.option = {
            const.Save.SaveDataJsonKey.String.CHATPER_URL: chapter_url,
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
                    login_kind=const.Save.LoginKind(
                        dec[const.Save.SaveDataJsonKey.Object.LOGIN_INFO][
                            const.Save.SaveDataJsonKey.String.LOGIN_KIND
                        ]
                    ),
                    chapter_url=dec[const.Save.SaveDataJsonKey.Object.OPTION][
                        const.Save.SaveDataJsonKey.String.CHATPER_URL
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
        except FileNotFoundError:
            # ファイルが存在しない場合は空なセーブデータを返す
            return SaveData()

    @staticmethod
    def save_to_json(save_data: SaveData, path: str, file_name: str):
        """セーブデータをJsonに保存する"""

        # ディレクトリが存在しない場合は作成する
        # exist_ok=Trueとすると既に存在しているディレクトリを指定してもエラーにならない
        os.makedirs(path, exist_ok=True)

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
    def login_kind(self) -> const.Save.LoginKind:
        """ログイン種別を取得する"""
        return const.Save.LoginKind(
            self.login_info[const.Save.SaveDataJsonKey.String.LOGIN_KIND]
        )

    @property
    def chapter_url(self) -> str:
        """チャプターURLを取得する"""
        return self.option[const.Save.SaveDataJsonKey.String.CHATPER_URL]

    @property
    def use_sound_notice(self) -> bool:
        """音声通知を使用するかを取得する"""
        return self.option[const.Save.SaveDataJsonKey.String.USE_SOUND_NOTICE]

    @property
    def use_window_notice(self) -> bool:
        """ウィンドウ通知を使用するかを取得する"""
        return self.option[const.Save.SaveDataJsonKey.String.USE_WINDOW_NOTICE]

    @property
    def mute_video(self) -> bool:
        """動画をミュートするかを取得する"""
        return self.option[const.Save.SaveDataJsonKey.String.MUTE_VIDEO]

    @property
    def notice_sound_scale(self) -> float:
        """通知音量を取得する"""
        return self.option[const.Save.SaveDataJsonKey.String.NOTICE_SOUND_SCALE]
