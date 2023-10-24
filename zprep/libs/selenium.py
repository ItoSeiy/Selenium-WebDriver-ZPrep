import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from . import const, path, save


def _set_driver_implicitly_wait_default(driver: webdriver.Chrome):
    """指定した要素が見つかるまでの待ち時間をデフォルトにする関数"""

    driver.implicitly_wait(const.Selenium.Option.TIME_TO_WAIT)


def _set_driver_implicitly_wait_zero(driver: webdriver.Chrome):
    """指定した要素が見つかるまでの待ち時間を0にする関数"""

    driver.implicitly_wait(0)


def _send_text(xPath: str, text: str, driver: webelement.WebElement):
    """指定したXPathの要素に指定したテキストを入力する関数"""

    field = driver.find_element(By.XPATH, xPath)
    field.send_keys(text)


def _get_subject_elements(driver: webdriver.Chrome) -> list[webelement.WebElement]:
    """動画、テストのエレメントのリストを取得する"""

    return driver.find_element(
        By.XPATH, const.Selenium.XPath.SUBJECT_ELEMENTS_CONTAINER
    ).find_elements(By.TAG_NAME, const.Selenium.Tag.LIST_ITEM)


def _get_first_not_played_element(
    driver: webdriver.Chrome,
    elements: list[webelement.WebElement],
) -> webelement.WebElement:
    """'視聴済み'のテキストが存在しない最初のエレメントを取得する関数"""

    # 指定した要素が見つかるまでの待ち時間を設定
    # 見つからなかったらすぐにエラーを出したいので0に設定
    _set_driver_implicitly_wait_zero(driver=driver)

    for element in elements:
        try:
            # "視聴済み"のテキストが存在するエレメントの取得を試みる
            element.find_element(
                By.TAG_NAME, const.Selenium.SpecificPath.VIDEO_PLAYED_PATH[0]
            ).find_element(
                By.TAG_NAME, const.Selenium.SpecificPath.VIDEO_PLAYED_PATH[1]
            ).find_element(
                By.CSS_SELECTOR, const.Selenium.SpecificPath.VIDEO_PLAYED_PATH[2]
            ).find_element(
                By.CSS_SELECTOR, const.Selenium.SpecificPath.VIDEO_PLAYED_PATH[3]
            ).find_element(
                By.CSS_SELECTOR, const.Selenium.SpecificPath.VIDEO_PLAYED_PATH[4]
            ).find_element(
                By.TAG_NAME, const.Selenium.SpecificPath.VIDEO_PLAYED_PATH[5]
            ).find_element(
                By.TAG_NAME, const.Selenium.SpecificPath.VIDEO_PLAYED_PATH[6]
            ).find_element(
                By.CSS_SELECTOR, const.Selenium.SpecificPath.VIDEO_PLAYED_PATH[7]
            )
            # "視聴済み"のテキストが存在するエレメントが見つかった場合は次のエレメントを探す
            continue
        except NoSuchElementException:
            # 指定した要素が見つかるまでの待ち時間の設定を元に戻す
            _set_driver_implicitly_wait_default(driver=driver)
            # "視聴済み"のテキストが存在するエレメントが見つからなかったらそれが未再生の動画のエレメントのため、そのエレメントを返す
            return element

    class_name_list = []
    for element in elements:
        class_name_list.append(element.get_attribute(const.Selenium.Tag.CLASS))

    logger = logging.getLogger(const.Log.DEFAULT_LOGGER)

    # 未再生の動画のエレメントが見つからなかった場合はエラーのロギングを行う
    logger.error(
        msg=f"[selenium.py _get_first_not_played_element] \n"
        f"未再生の動画のエレメントが見つかりませんでした、以下が引数で渡されたエレメントのリストのクラス名です\n"
        f"{str(class_name_list)}"
    )


def _is_test_element(element: webelement.WebElement) -> bool:
    """テストのエレメントかどうかを判定する関数"""

    try:
        test_element = (
            element.find_element(
                By.CLASS_NAME, const.Selenium.SpecificPath.JUDGE_TEST_ELEMENT_PATH[0]
            )
            .find_element(
                By.CLASS_NAME, const.Selenium.SpecificPath.JUDGE_TEST_ELEMENT_PATH[1]
            )
            .find_element(
                By.CSS_SELECTOR, const.Selenium.SpecificPath.JUDGE_TEST_ELEMENT_PATH[2]
            )
        )
        return True
    except NoSuchElementException:
        return False


def setup_chrome(save_data: save.SaveData):
    """Chromeをセットアップする関数"""

    # Chromeのオプションを設定
    options = webdriver.ChromeOptions()

    # ログを無効化
    options.add_argument(const.Selenium.Option.DISABLE_LOGGING)
    # ログレベルを下げて、余計なログを出さないようにする
    options.add_argument(const.Selenium.Option.LOG_LEVEL_3)
    # 長文をコンソールに表示させない
    options.add_experimental_option(
        const.Selenium.Option.EXPERMENTAL_OPTION[0],
        const.Selenium.Option.EXPERMENTAL_OPTION[1],
    )

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
    driver.implicitly_wait(const.Selenium.Option.TIME_TO_WAIT)

    # ウィンドウサイズを設定
    driver.set_window_size(
        const.Selenium.Option.WINDOW_SIZE[0], const.Selenium.Option.WINDOW_SIZE[1]
    )
    # ウィンドウ位置を設定
    driver.set_window_position(
        const.Selenium.Option.WINDOW_POS[0],
        const.Selenium.Option.WINDOW_POS[1],
    )

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

    _play_video_loop(driver=driver)


def _play_video_loop(driver: webdriver.Chrome):
    """再生できる限り動画を再生し続ける関数"""

    elements = _get_subject_elements(driver=driver)
    not_played_element = _get_first_not_played_element(driver=driver, elements=elements)

    if _is_test_element(not_played_element) == True:
        

    input("press any key to finish :")
