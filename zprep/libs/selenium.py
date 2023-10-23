from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from . import const, path


def open_chrome(mute_sound: bool):
    # Chromeのオプションを設定
    options = webdriver.ChromeOptions()

    # ChromDriverのパスを指定
    service = Service(
        executable_path=path.get_assets_path(const.Selenium.CHROME_DRIVER_NAME)
    )

    if mute_sound:
        # ミュートする設定であればミュートするオプションを追加
        options.add_argument(const.Selenium.Option.MUTE_AUDIO)

    # ChromeDriverを起動、設定を適用
    driver = webdriver.Chrome(service=service, options=options)

    # ウィンドウサイズを設定
    driver.set_window_size(1500, 1000)
    # ウィンドウ位置を設定
    driver.set_window_position(550, 300)

    # N予備校のログイン画面を開く
    driver.get(
        "https://www.nnn.ed.nico/login?next_url=https%3A%2F%2Fwww.nnn.ed.nico%2Fmy_course"
    )

    input("press any key to finish :")
