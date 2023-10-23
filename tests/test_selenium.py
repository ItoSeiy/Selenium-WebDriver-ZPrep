import set_path

set_path.set()
from zprep.libs import const, save, selenium

if __name__ == "__main__":
    save_data = save.SaveData.get_from_json(
        const.Save.Path.DATA_PATH, const.Save.Path.FILE_NAME
    )
    selenium.setup_chrome(save_data=save_data)
