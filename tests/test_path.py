import set_path

set_path.set()
from zprep.libs import path, const


import unittest


class TestPath(unittest.TestCase):

    def test_audio_path(self):
        self.assertEqual(
            path.get_assets_path(const.Audio.MP3.WAKKA_MP3),
            r"C:\Users\itose\1VSCode\Python\ZPrep\assets\audio\wakka.mp3",
        )

    def test_icon_path(self):
        self.assertEqual(
            path.get_assets_path(const.Gui.Window.ICON_PATH),
            r"C:\Users\itose\1VSCode\Python\ZPrep\assets\icon\icon.ico",
        )

    def test_icon_path_01(self):
        self.assertEqual(
            path.get_assets_path(const.Notify.ICON_PATH_LIST[0]),
            r"C:\Users\itose\1VSCode\Python\ZPrep\assets\icon\wakka01.ico",
        )

    def test_icon_path_02(self):
        self.assertEqual(
            path.get_assets_path(const.Notify.ICON_PATH_LIST[1]),
            r"C:\Users\itose\1VSCode\Python\ZPrep\assets\icon\wakka02.ico",
        )


if __name__ == "__main__":
    unittest.main()
