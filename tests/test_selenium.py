import set_path

set_path.set()
from zprep.libs import selenium

if __name__ == "__main__":
    selenium.open_chrome(True)
