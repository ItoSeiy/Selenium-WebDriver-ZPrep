import os
import sys

def get_assets_path(relative_path: str) -> str:
    """assetsディレクトリのパスを取得する

    Args:
        relative_path (str): assetsディレクトリからの相対パス

    Returns:
        str: assetsディレクトリのパス
    """

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "assets", relative_path)

    return os.path.join(os.path.abspath("assets"), relative_path)
