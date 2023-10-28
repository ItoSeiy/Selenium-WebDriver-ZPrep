"""トースト通知を行うモジュール"""

from plyer import notification
from . import const, path
from random import randint


def notify(title: str, timeout: int):
    notification.notify(
        title=title,
        message=const.Notify.MESSAGE,
        app_name=const.App.NAME,
        app_icon=path.get_assets_path(
            const.Notify.ICON_PATH_LIST[
                randint(0, len(const.Notify.ICON_PATH_LIST) - 1)
            ]
        ),
        timeout=timeout,
    )
