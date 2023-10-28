from . import const
import logging
import os

# ディレクトリが存在しない場合は作成する
# exist_ok=Trueとすると既に存在しているディレクトリを指定してもエラーにならない
os.makedirs(const.Save.Path.DATA_PATH, exist_ok=True)

# ロガーの取得
logger = logging.getLogger(const.Log.DEFAULT_LOGGER)

# ログの最低出力レベルを設定
logger.setLevel(logging.DEBUG)

# Streamハンドラクラスをインスタンス化
st_handler = logging.StreamHandler()
# フォーマッターを設定
st_handler.setFormatter(logging.Formatter(const.Log.DEFAULT_LOG_FORMAT))

# ログファイルを作成
with open(f"{const.Log.Path.DATA_PATH}/{const.Log.Path.FILE_NAME}", "w+") as file:
    file.write("")
    file.close()

# Fileハンドラクラスをインスタンス化
fl_handler = logging.FileHandler(
    filename=f"{const.Log.Path.DATA_PATH}/{const.Log.Path.FILE_NAME}",
    encoding="utf-8",
    # 毎回上書きする
    mode="w+",
)
# フォーマッターを設定
fl_handler.setFormatter(logging.Formatter(const.Log.DEFAULT_LOG_FORMAT))

# ハンドラ設定
logger.addHandler(st_handler)
logger.addHandler(fl_handler)
