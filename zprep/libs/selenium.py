import logging
from time import sleep
from typing import Callable, Union

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from . import const, path, save


class Selenium:
    "==========================汎用関数============================"

    def _set_driver_implicitly_wait_default(self, driver: webdriver.Chrome):
        """指定した要素が見つかるまでの待ち時間をデフォルトにする関数"""

        driver.implicitly_wait(self._save_data.time_out)

    def _set_driver_implicitly_wait_zero(self, driver: webdriver.Chrome):
        """指定した要素が見つかるまでの待ち時間を0にする関数"""

        driver.implicitly_wait(0)

    def _send_text(self, x_path: str, text: str, driver: webelement.WebElement):
        """指定したXPathの要素に指定したテキストを入力する関数"""

        field = driver.find_element(By.XPATH, x_path)
        field.send_keys(text)

    def _get_subject_elements(
        self, driver: webdriver.Chrome
    ) -> list[webelement.WebElement]:
        """動画、テストのエレメントのリストを取得する"""

        return driver.find_element(
            By.XPATH, const.Selenium.XPath.SUBJECT_ELEMENTS_CONTAINER
        ).find_elements(By.TAG_NAME, const.Selenium.Tag.LIST_ITEM)

    def _get_first_not_played_video_element(
        self,
        driver: webdriver.Chrome,
        elements: list[webelement.WebElement],
    ) -> Union[webelement.WebElement, str]:
        """未再生の動画のエレメントを取得する関数

        Returns:
            Union[webelement.WebElement, str]: 未再生の動画のエレメントが取得できなかった場合はエラーメッセージが返される
        """

        for i, element in enumerate(elements):
            if self._is_test_element(driver=driver, element=element) == True:
                # テストのエレメントであれば次のエレメントを探す
                if len(elements) - 1 == i:
                    # 最後のエレメントまでテストのエレメントだった場合はエラーメッセージを返す
                    return const.Selenium.Message.ALL_VIDEO_PLAYED_MESSAGE
                continue

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
                # "視聴済み"のテキストが存在するエレメントが見つからなかったらそれが未再生の動画のエレメントのため、そのエレメントを返す
                return element

        class_name_list = []
        for element in elements:
            class_name_list.append(element.get_attribute(const.Selenium.Tag.CLASS))

        logger = logging.getLogger(const.Log.DEFAULT_LOGGER)

        # 未再生の動画のエレメントが見つからなかった場合はエラーのロギングを行う
        logger.error(
            msg=f"[selenium.py _get_first_not_played_video_element] \n"
            f"未再生の動画のエレメントが見つかりませんでした、以下が引数で渡されたエレメントのリストのクラス名です\n"
            f"{str(class_name_list)}"
        )

    def _is_test_element(
        self, driver: webdriver.Chrome, element: webelement.WebElement
    ) -> bool:
        """テストのエレメントかどうかを判定する関数"""

        test_element = None

        try:
            test_element = (
                element.find_element(
                    By.TAG_NAME,
                    const.Selenium.SpecificPath.JUDGE_TEST_ELEMENT_PATH[0],
                )
                .find_element(
                    By.TAG_NAME,
                    const.Selenium.SpecificPath.JUDGE_TEST_ELEMENT_PATH[1],
                )
                .find_element(
                    By.CSS_SELECTOR,
                    const.Selenium.SpecificPath.JUDGE_TEST_ELEMENT_PATH[2],
                )
            )
        except NoSuchElementException:
            test_element = None

        if test_element == None:
            # テストのエレメントでなければテストではないのでFalseを返す
            return False
        else:
            # テストのエレメントであればテストなのでTrueを返す
            return True

    def _is_opend_element(self, element: webelement.WebElement):
        """エレメントが解放されているかどうかを判定する関数"""

        try:
            # 未開放と判定できるエレメントを探す
            element.find_element(
                By.CSS_SELECTOR, const.Selenium.CSSSelector.UNOPENED_ELEMENT_PATH
            )
            # ここまで処理が来たら未開放と判定できるエレメントが見つかったので、Falseを返す
            return False
        except NoSuchElementException:
            # 未開放と判定できるエレメントが無かったので、Trueを返す
            return True

    def _get_video_length(self, element: webelement.WebElement) -> int:
        """動画の長さを取得する関数"""

        # 動画の長さを取得する
        video_length = (
            element.find_element(
                By.TAG_NAME, const.Selenium.SpecificPath.VIDEO_LENGTH_PATH[0]
            )
            .find_element(By.TAG_NAME, const.Selenium.SpecificPath.VIDEO_LENGTH_PATH[1])
            .find_element(
                By.CSS_SELECTOR, const.Selenium.SpecificPath.VIDEO_LENGTH_PATH[2]
            )
            .text
        )

        # 動画の長さを秒数に変換する
        video_length = int(video_length.split(":")[0]) * 60 + int(
            video_length.split(":")[1]
        )

        return video_length

    "==========================汎用関数ここまで============================"

    _save_data: save.SaveData = None
    _chapter_url: str = None
    _on_finish: Callable[[save.SaveData, str], None] = None

    def __init__(
        self, save_data: save.SaveData, chapter_url: str,  on_finish: Callable[[save.SaveData, str], None]
    ):
        self._save_data = save_data
        self._chapter_url = chapter_url
        self._on_finish = on_finish

    def start(self):
        self._setup_chrome()

    "==========================メイン関数================================="

    def _setup_chrome(self):
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

        if self._save_data.mute_video:
            # ミュートする設定であればミュートするオプションを追加
            options.add_argument(const.Selenium.Option.MUTE_AUDIO)

        # ChromeDriverを起動、設定を適用
        driver = webdriver.Chrome(options=options)

        # 指定した要素が見つかるまでの待ち時間を設定
        self._set_driver_implicitly_wait_default(driver=driver)

        # ウィンドウ位置を設定
        driver.set_window_position(
            self._save_data.chrome_window_pos[0], self._save_data.chrome_window_pos[1]
        )

        # ウィンドウサイズを設定
        driver.set_window_size(
            self._save_data.chrome_window_size[0], self._save_data.chrome_window_size[1]
        )

        # ログインページを開く
        self._open_login_page(driver=driver)

    def _open_login_page(self, driver: webdriver.Chrome):
        """ログインページを開く関数"""

        # ログイン画面を開く
        driver.get(const.Selenium.Url.LOGIN)
        driver.find_element(
            By.XPATH,
            const.Selenium.XPath.LOGIN_KIND_BUTTON(
                student_id=self._save_data.student_id
            ),
        ).click()

        # ログイン情報を入力
        self._send_text(
            x_path=const.Selenium.XPath.STUDENT_ID_FIELD,
            text=self._save_data.student_id,
            driver=driver,
        )
        self._send_text(
            x_path=const.Selenium.XPath.PASSWORD_FIELD,
            text=self._save_data.password,
            driver=driver,
        )
        # ログインボタンをクリック
        driver.find_element(By.XPATH, const.Selenium.XPath.LOGIN_BUTTON).click()

        # 教材ページを開く
        self._open_subject_page(driver=driver)

    def _open_subject_page(self, driver: webdriver.Chrome):
        """教材ページを開く関数"""

        # 指定された教材を開く
        driver.get(self._chapter_url)

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
            driver.find_element(By.CSS_SELECTOR, const.Selenium.CSSSelector.AGREEMENT_BUTTON).click()
        except:
            None

        # 必修教材のみを表示する
        try:
            driver.find_element(
                By.XPATH, const.Selenium.XPath.ONLY_REQUIRED_SUBJECT_BUTTON
            ).click()
        except:
            None

        self._play_video_loop(driver=driver)

    def _play_video_loop(
        self, driver: webdriver.Chrome, before_clicked_element: webdriver.Chrome = None
    ):
        """再生できる限り動画を再生し続ける関数

        Args:
            before_clicked_element (webdriver.Chrome): 1実行の内の前回再生しようとした動画のエレメント
        """

        # 指定した要素が見つかるまでの待ち時間を0にする
        # 見つからない事をトリガーにしている判定が存在するため
        self._set_driver_implicitly_wait_zero(driver=driver)

        # 動画、テストのエレメントのリストを取得
        elements = self._get_subject_elements(driver=driver)

        # 未再生の動画エレメントを取得
        not_played_element = self._get_first_not_played_video_element(
            driver=driver, elements=elements
        )

        # すべての動画を再生した場合は終了
        if not_played_element == const.Selenium.Message.ALL_VIDEO_PLAYED_MESSAGE:
            # ログ
            logger = logging.getLogger(const.Log.DEFAULT_LOGGER)
            logger.debug(f"{const.Selenium.Message.ALL_VIDEO_PLAYED_MESSAGE}")

            self._on_finish(
                self._save_data, const.Selenium.Message.ALL_VIDEO_PLAYED_MESSAGE
            )
            driver.close()
            return

        # 未再生のエレメントが未開放であれば、既にテストに到達しているので終了
        if self._is_opend_element(element=not_played_element) == False:
            # ログ
            logger = logging.getLogger(const.Log.DEFAULT_LOGGER)
            logger.debug(
                f"{const.Selenium.Message.ALL_VIDEO_PLAYED_MESSAGE} \n not_played_element:{not_played_element.get_attribute(const.Selenium.Tag.CLASS)} \n text:{not_played_element.text}"
            )

            self._on_finish(
                self._save_data, const.Selenium.Message.ALREADY_REACHED_TEST
            )
            driver.close()
            return

        # 前回再生しようとしたエレメントと今回再生しようとしているエレメントが同じかどうかを判定する
        if (
            before_clicked_element != None
            and before_clicked_element == not_played_element
        ):
            # ログ
            logger = logging.getLogger(const.Log.DEFAULT_LOGGER)
            logger.debug("same element playing")

            # 同じであればタイムアウト時間を待ち、再帰呼び出しを行う
            sleep(self._save_data.time_out)
            self._play_video_loop(
                driver=driver, before_clicked_element=not_played_element
            )
            return

        not_played_element.click()

        # 動画の長さを取得
        video_length = self._get_video_length(element=not_played_element)

        # ログ
        logger = logging.getLogger(const.Log.DEFAULT_LOGGER)
        logger.debug(f"before sleep : sleep : time{video_length}")

        # 動画の長さを待つ
        sleep(video_length)

        # ログ
        logger.debug(f"after sleep : sleep time : {video_length}")

        self._play_video_loop(driver=driver, before_clicked_element=not_played_element)
        return
