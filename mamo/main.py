from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase

LabelBase.register("NotoSansCJKjp-Light",
                   fn_regular="./fonts/NotoSansCJKjp-Light.otf")

Window.size = (360, 640)


class EditMemo(Screen):
    pass


class Tutorial(Screen):
    pass


class ManageMemoMenu(Screen):
    pass


class MainMenu(Screen):
    pass


class MakodeditScreenManager(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(MainMenu(name="main"))
        self.add_widget(ManageMemoMenu(name="manage_memo"))
        self.add_widget(Tutorial(name="tutorial"))
        self.add_widget(EditMemo(name="edit_memo"))


class MakodeditApp(App):
    def build(self):
        self.title = "Makodedit"
        self.icon = "images/makodedit.png"
        return MakodeditScreenManager()


if __name__ == '__main__':
    print(LabelBase.get_system_fonts_dir())
    MakodeditApp().run()
