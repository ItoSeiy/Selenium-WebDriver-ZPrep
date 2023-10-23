from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from . import const, path, save


def _send_text(XPATH: str, text: str, driver: webelement.WebElement):
    """指定したXPathの要素に指定したテキストを入力する関数"""

    field = driver.find_element(By.XPATH, XPATH)
    field.send_keys(text)


def setup_chrome(save_data: save.SaveData):
    """Chromeをセットアップする関数"""

    # Chromeのオプションを設定
    options = webdriver.ChromeOptions()

    # ログを無効化
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    if save_data.mute_video:
        # ミュートする設定であればミュートするオプションを追加
        options.add_argument(const.Selenium.Option.MUTE_AUDIO)

    # ChromDriverのパスを指定
    service = Service(
        executable_path=path.get_assets_path(const.Selenium.CHROME_DRIVER_NAME)
    )

    # ChromeDriverを起動、設定を適用
    driver = webdriver.Chrome(service=service, options=options)

    # 指定した要素が見つかるまでの待ち時間を設定
    driver.implicitly_wait(10)

    # ウィンドウサイズを設定
    driver.set_window_size(1500, 1000)
    # ウィンドウ位置を設定
    driver.set_window_position(550, 300)

    # ログインページを開く
    _open_login_page(driver=driver, save_data=save_data)


def _open_login_page(driver: webdriver.Chrome, save_data: save.SaveData):
    """ログインページを開く関数"""

    # ログイン画面を開く
    driver.get(const.Selenium.Url.LOGIN)
    driver.find_element(
        By.XPATH, const.Selenium.XPath.LOGIN_KIND_BUTTON(kind=save_data.login_kind)
    ).click()

    # ログイン情報を入力
    _send_text(const.Selenium.XPath.STUDENT_ID_FIELD, save_data.student_id, driver)
    _send_text(const.Selenium.XPath.PASSWORD_FIELD, save_data.password, driver)
    # ログインボタンをクリック
    driver.find_element(By.XPATH, const.Selenium.XPath.LOGIN_BUTTON).click()

    # 教材ページを開く
    _open_subject_page(driver=driver, save_data=save_data)


def _open_subject_page(driver: webdriver.Chrome, save_data: save.SaveData):
    """教材ページを開く関数"""

    # 指定された教材を開く
    driver.get(save_data.chapter_url)

    # 同意
    try:
        driver.find_element(
            By.XPATH, const.Selenium.XPath.AGREEMENT_ELEMENTS[0]
        ).click()
        driver.find_element(
            By.XPATH, const.Selenium.XPath.AGREEMENT_ELEMENTS[1]
        ).click()
        driver.find_element(
            By.XPATH, const.Selenium.XPath.AGREEMENT_ELEMENTS[2]
        ).click()
        driver.find_element(
            By.XPATH, const.Selenium.XPath.AGREEMENT_ELEMENTS[3]
        ).click()
        driver.find_element(
            By.XPATH, const.Selenium.XPath.AGREEMENT_ELEMENTS[4]
        ).click()
        driver.find_element(By.XPATH, const.Selenium.XPath.AGREEMENT_BUTTON).click()
    except:
        None

    # 必修教材のみを表示する
    try:
        driver.find_element(
            By.XPATH, const.Selenium.XPath.ONLY_REQUIRED_SUBJECT_BUTTON
        ).click()
    except:
        None

    input("press any key to finish :")


# def _play_video_loop(driver: webelement.WebElement):
