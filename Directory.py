import sys
import os
from appdirs import *

appname = "Z予備クン"
appauthor = "IS"
data_path = user_data_dir(appname, appauthor)
file_name = 'SaveData.text'

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)