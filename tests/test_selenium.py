import set_path

set_path.set()
from zprep.libs import const, save, selenium


def _on_finish(save_data: save.SaveData, message: str):
    print(save_data)
    print(message)


if __name__ == "__main__":
    save_data = save.SaveData.get_from_json(
        const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
    )
    sel = selenium.Selenium(save_data=save_data, chapter_url=save_data.chapter_url_list[0], on_finish=_on_finish)
    sel.start()
