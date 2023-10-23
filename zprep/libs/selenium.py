from selenium import webdriver
from . import path


def open_chrome(mute_sound: bool):
    # Chromeのオプションを設定
    chrome_options = webdriver.ChromeOptions()
    if mute_sound:
        # ミュートする設定であればミュートするオプションを追加
        chrome_options.add_argument("--mute-audio")
    print(path.get_assets_path("chromedriver.exe"))
    # driver = webdriver.Chrome()
    # driver.get(
    #    "https://www.nnn.ed.nico/login?next_url=https%3A%2F%2Fwww.nnn.ed.nico%2Fmy_course"
    # )
