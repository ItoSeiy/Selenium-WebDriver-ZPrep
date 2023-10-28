import set_path

set_path.set()
from zprep.libs import const, audio

if __name__ == "__main__":
    audio.play_sound(const.Audio.MP3.WAKKA_MP3, 0.1)
    input()
