import set_path

set_path.set()
from zprep.libs import gui, save, const


def _on_start_button_click(save_data: save):
    if save_data is not None:
        save.SaveData.save_to_json(
            save_data, const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
        )
    print(save_data)


if __name__ == "__main__":
    save_data = save.SaveData.get_from_json(
        const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
    )
    gui.create(save_data=save_data, on_start_button_click=_on_start_button_click)
