import set_path

set_path.set()
from zprep.libs import path, const


import unittest


class TestPath(unittest.TestCase):
    def test_asset_path(self):
        self.assertEqual(
            path.get_assets_path(""), r"c:\Users\itose\1VSCode\Python\ZPrep\assets"
        )

    def test_audio_path(self):
        self.assertEqual(
            path.get_assets_path(f"{const.Audio.MP3.WAKKA_MP3}"),
            r"c:\Users\itose\1VSCode\Python\ZPrep\assets\audio\wakka.mp3",
        )

    def test_icon_path(self):
        self.assertEqual(
            path.get_assets_path(f"{const.Gui.Window.ICON_PATH}"),
            r"c:\Users\itose\1VSCode\Python\ZPrep\assets\icon\icon.ico",
        )

    def test_icon_path_01(self):
        self.assertEqual(
            path.get_assets_path(f"{const.Gui.Window.ICON_PATH_01}"),
            r"c:\Users\itose\1VSCode\Python\ZPrep\assets\icon\wakka01.ico",
        )

    def test_icon_path_02(self):
        self.assertEqual(
            path.get_assets_path(f"{const.Gui.Window.ICON_PATH_02}"),
            r"c:\Users\itose\1VSCode\Python\ZPrep\assets\icon\wakka02.ico",
        )


if __name__ == "__main__":
    unittest.main()
