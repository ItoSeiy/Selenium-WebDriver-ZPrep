import os


def get_assets_path(relative_path: str) -> str:
    """assetsディレクトリのパスを取得する

    Args:
        relative_path (str): assetsディレクトリからの相対パス

    Returns:
        str: assetsディレクトリのパス
    """
    # path.py ファイルのディレクトリを取得
    path_directory = os.path.dirname(__file__)
    # assetsディレクトリへの相対パス
    to_assets_relative_path = os.path.join("..", "..", "assets")
    # 指定されたassetsディレクトリの相対パス
    relative_path = os.path.join(to_assets_relative_path, relative_path)
    # assetsディレクトリの絶対パスを生成
    path = os.path.normpath(os.path.join(path_directory, relative_path))
    return path
