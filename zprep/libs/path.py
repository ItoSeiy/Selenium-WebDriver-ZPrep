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
    # assetsディレクトリの相対パス
    assets_relative_path = os.path.join("..", "..", "assets")
    # assetsディレクトリの絶対パスを生成
    assets_path = os.path.normpath(os.path.join(path_directory, assets_relative_path))
    # assetsディレクトリの相対パス
    relative_path = os.path.join(assets_relative_path, relative_path)
    # assetsディレクトリの絶対パスを生成
    path = os.path.normpath(os.path.join(path_directory, relative_path))
    return path
