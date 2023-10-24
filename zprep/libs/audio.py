"""オーディオ関連の処理を行うモジュール"""
import pygame

from . import path


def play_sound(sound_relative_path: str, volume: float):
    pygame.mixer.init()
    pygame.mixer.music.load(path.get_assets_path(sound_relative_path))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
