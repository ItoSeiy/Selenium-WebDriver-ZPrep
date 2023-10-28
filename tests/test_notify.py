import set_path

set_path.set()
from zprep.libs import const, notify

if __name__ == "__main__":
    notify.notify(title="test notify", timeout=20)
    input()
