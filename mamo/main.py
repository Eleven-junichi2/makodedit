from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase

LabelBase.register("NotoSansCJKjp-Light",
                   fn_regular="./fonts/NotoSansCJKjp-Light.otf")

Window.size = (360, 640)


class Tutorial(Screen):
    pass


class ManageMemoMenu(Screen):
    pass


class MainMenu(Screen):
    pass


class MamoScreenManager(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(MainMenu(name="main"))
        self.add_widget(ManageMemoMenu(name="manage_memo"))
        self.add_widget(Tutorial(name="tutorial"))


class MamoApp(App):
    def build(self):
        self.title = "Mamo"
        self.icon = "images/mamo.png"
        return MamoScreenManager()


if __name__ == '__main__':
    print(LabelBase.get_system_fonts_dir())
    MamoApp().run()
