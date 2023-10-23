import libs.const
import libs.gui
import libs.save


def _on_start_button_click(save_data: libs.save):
    if save_data is not None:
        libs.save.SaveData.save_to_json(
            save_data, libs.const.Save.Path.DATA_PATH, libs.const.Save.Path.FILE_NAME
        )
    print(save_data)


def main():
    save_data = libs.save.SaveData.get_from_json(
        libs.const.Save.Path.DATA_PATH, libs.const.Save.Path.FILE_NAME
    )
    libs.gui.create(save_data=save_data, on_start_button_click=_on_start_button_click)


if __name__ == "__main__":
    main()
