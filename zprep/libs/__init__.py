from . import const
import logging


# ロガーの取得
logger = logging.getLogger(const.Log.DEFAULT_LOGGER)

# ログの最低出力レベルを設定
logger.setLevel(logging.DEBUG)

# Streamハンドラクラスをインスタンス化
st_handler = logging.StreamHandler()
# フォーマッターを設定
st_handler.setFormatter(logging.Formatter(const.Log.DEFAULT_LOG_FORMAT))

# Fileハンドラクラスをインスタンス化
fl_handler = logging.FileHandler(
    filename=f"{const.Log.Path.DATA_PATH}/{const.Log.Path.FILE_NAME}", encoding="utf-8"
)
# フォーマッターを設定
fl_handler.setFormatter(logging.Formatter(const.Log.DEFAULT_LOG_FORMAT))

# ハンドラ設定
logger.addHandler(st_handler)
logger.addHandler(fl_handler)
