import libs.const as const
import libs.gui as gui
import libs.save as save


def _on_start_button_click(save_data: save.SaveData):
    if save_data is not None:
        save_data.save_to_json(
            save_data, const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
        )
    print(save_data.student_id)


def main():
    save_data = save.SaveData.get_from_json(
        const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
    )
    gui.create(save_data=save_data, on_start_button_click=_on_start_button_click)


if __name__ == "__main__":
    main()
