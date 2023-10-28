import os
import sys


def set():
    # const.py ファイルのディレクトリを取得
    path_directory = os.path.dirname(__file__)
    # zprepディレクトリへの相対パス
    to_root_relative_path = os.path.join("..", "..", "ZPrep")
    # zprepディレクトリの絶対パスを生成
    root_path = os.path.normpath(os.path.join(path_directory, to_root_relative_path))
    # zprepディレクトリをパスに追加
    sys.path.append(root_path)
