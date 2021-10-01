import os
import sys
from pathlib import Path
from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (414, 732)

# 환경설정
if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["BOOKSTAGRAM_ROOT"] = sys._MEIPASS
else:
    os.environ["BOOKSTAGRAM_ROOT"] = str(Path(__file__).parent)


KV_DIR = f"{os.environ['BOOKSTAGRAM_ROOT']}/libs/kv/"

for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())

KV = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import BookstagramRootScreen libs.baseclass.root_screen.BookstagramRootScreen

ScreenManager:
    transition: FadeTransition()
    
    BookstagramRootScreen:
        name: "bookstagram root screen"
"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Bookstagram"

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        FONT_PATH = f"{os.environ['BOOKSTAGRAM_ROOT']}/assets/fonts/"
        self.root = Builder.load_string(KV)
        self.theme_cls.font_styles.update({
            "H1": [FONT_PATH + "RobotoCondensed-Light", 96, False, -1.5],
            "H2": [FONT_PATH + "RobotoCondensed-Light", 60, False, -0.5],
            "H3": [FONT_PATH + "Eczar-Regular", 48, False, 0],
            "H4": [FONT_PATH + "RobotoCondensed-Regular", 34, False, 0.25],
            "H5": [FONT_PATH + "RobotoCondensed-Regular", 24, False, 0],
            "H6": [FONT_PATH + "RobotoCondensed-Bold", 20, False, 0.15],
            "Subtitle1": [
                FONT_PATH + "RobotoCondensed-Regular",
                16,
                False,
                0.15,
            ],
            "Subtitle2": [
                FONT_PATH + "RobotoCondensed-Medium",
                14,
                False,
                0.1,
            ],
            "Body1": [FONT_PATH + "Eczar-Regular", 16, False, 0.5],
            "Body2": [FONT_PATH + "RobotoCondensed-Light", 14, False, 0.25],
            "Button": [FONT_PATH + "RobotoCondensed-Bold", 14, True, 1.25],
            "Caption": [
                FONT_PATH + "RobotoCondensed-Regular",
                12,
                False,
                0.4,
            ],
            "Overline": [
                FONT_PATH + "RobotoCondensed-Regular",
                10,
                True,
                1.5,
            ],
            "Money": [FONT_PATH + "Eczar-SemiBold", 48, False, 0],
        })
        return Builder.load_string(KV)

if __name__ == "__main__":
    MainApp().run()