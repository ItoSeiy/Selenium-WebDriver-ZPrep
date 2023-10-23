import libs.const
import libs.gui
import libs.save


def _on_start_button_click(save_data: libs.save):
    print("Save Data", str(save_data.student_id))


def main():
    save_data = libs.save.SaveData.get_from_json(
        libs.const.Save.Path.DATA_PATH, libs.const.Save.Path.FILE_NAME
    )
    libs.gui.create(save_data=save_data, on_start_button_click=_on_start_button_click)


if __name__ == "__main__":
    main()
