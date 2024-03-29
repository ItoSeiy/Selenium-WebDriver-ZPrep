import set_path

set_path.set()
from zprep.libs import gui, save, const


def _on_start_button_click(save_setting: bool, save_data: save.SaveData):
    if save_setting == True:
        save_data.save_to_json(
            save_data, const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
        )
    else:
        print("設定を保存しませんでした")

    save_data = save.SaveData.get_from_json(
        const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
    )

    print(f"student_id: {save_data.student_id}")
    print(f"password: {save_data.password}")
    print(f"chapter_url: {save_data.chapter_url_list}")
    print(f"max_playing_count: {save_data.max_playing_count}")
    print(f"time_out: {save_data.time_out}")
    print(f"chrome_window_pos: {save_data.chrome_window_pos}")
    print(f"chrome_window_size: {save_data.chrome_window_size}")
    print(f"use_sound_notice: {save_data.use_sound_notice}")
    print(f"use_window_notice: {save_data.use_window_notice}")
    print(f"mute_video: {save_data.mute_video}")
    print(f"notice_sound_scale: {save_data.notice_sound_scale}")


if __name__ == "__main__":
    save_data = save.SaveData.get_from_json(
        const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
    )
    gui.create(save_data=save_data, on_start_button_click=_on_start_button_click)
