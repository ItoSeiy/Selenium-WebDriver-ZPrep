from sys import exit
from time import sleep

import libs.audio as audio
import libs.const as const
import libs.gui as gui
import libs.notify as notify
import libs.path as path
import libs.save as save
import libs.selenium as selenium
from mutagen.mp3 import MP3


def _on_finish_selenium(save_data: save.SaveData, message: str):
    if save_data.use_sound_notice:
        audio.play_sound(const.Audio.MP3.WAKKA_MP3, save_data.notice_sound_scale)

    sound_length = MP3(path.get_assets_path(const.Audio.MP3.WAKKA_MP3)).info.length

    if save_data.use_sound_notice:
        notify.notify(
            title=message,
            timeout=int(
                # 通知の長さを音声の長さに合わせる
                sound_length
            ),
        )

    sleep(sound_length)
    exit()


def _on_start_button_click(save_data: save.SaveData):
    if save_data is not None:
        save_data.save_to_json(
            save_data, const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
        )

    sel = selenium.Selenium(save_data, on_finish=_on_finish_selenium)
    sel.start()


def main():
    save_data = save.SaveData.get_from_json(
        const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
    )
    gui.create(save_data=save_data, on_start_button_click=_on_start_button_click)


if __name__ == "__main__":
    main()
