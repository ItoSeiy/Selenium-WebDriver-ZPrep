from libs import gui
from libs import const
from libs import save


def _on_start_button_click(save_data: save):
    print("Click")
    print("Save Data", str(save_data.student_id))


def main():
    save_data = save.SaveData.get_from_json(
        const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
    )
    gui.create(save_data=save_data, on_start_button_click=_on_start_button_click)

if __name__ == "__main__":
    main()