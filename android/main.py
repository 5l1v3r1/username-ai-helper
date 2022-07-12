import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import Builder
from kivy.core.window import Window
from ast import literal_eval


class WelcomeScreen1(Screen):
    pass


class WelcomeScreen2(Screen):
    pass


class WelcomeScreen3(Screen):
    pass


class WelcomeScreen4(Screen):
    pass


class MainScreen(Screen):
    pass


class WindowManager(ScreenManager):
    # with open("/data/data/org.test.myapp/setting.txt", 'r') as f:
    #      config_file = literal_eval(f.read())
    # if config_file["skip-welcome-screen"]:
    print("Skipping welcome screens")


class AiNameApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.5, 0.6, 1)
        # window size for testing only, remove for release
        Window.size = (540, 1140)
        return kv_styling


kv_styling = Builder.load_file("styling.kv")
if __name__ == "__main__":
    AiNameApp().run()
