import sys
import pathlib

from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.codeinput import CodeInput
from kivy.properties import ObjectProperty

from file_manage import FileManager

LabelBase.register("NotoSansCJKjp-Light",
                   fn_regular="./fonts/NotoSansCJKjp-Light.otf")

LabelBase.register("NotoSansMonoCJKjp-Regular",
                   fn_regular="./fonts/NotoSansMonoCJKjp-Regular.otf")


Window.size = (360, 640)

__file__ = sys.argv[0]


class MakodeditFileManager(FileManager):
    def load_file(self, file_path):
        with open(file_path, "r") as file_obj:
            return file_obj.read()

    def save_file(self, file_path, file_name, text):
        if not file_path == "":
            file_path = pathlib.Path(file_path)
            if file_path.is_dir():
                file_path = file_path / file_name
            with open(file_path, "w") as file_obj:
                file_obj.write(text)
            saved_file_name = file_path.parts[-1]
            return saved_file_name

    # def save_file(self, file_name, file_path, text):
    #     file_name = str(file_name)
    #     text = str(text)
    #     if not(file_name == "" or text == ""):
    #         # self.data_dir_path: pathlib.Path object
    #         with open(str(self.data_dir_path / file_name), "w") as file_obj:
    #             file_obj.write(text)
    #         return True
    #     else:
    #         return False


class MakodeditCodeInput(CodeInput):
    def change_style(self, style_name="default"):
        self.style_name = style_name
        # -- Reset self.text for apply style.
        tmp = self.text
        self.text = ""
        self.text = tmp
        # --


class FileEdit(Screen):
    file_name_input = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_manager = MakodeditFileManager(self)

    def show_load_dialog(self):
        self.file_manager.load_dialog()

    def show_save_dialog(self):
        if not self.file_name_input.text == "":
            self.file_manager.save_dialog()

    def load_file(self, file_path):
        self.text_input.text = self.file_manager.load_file(file_path)
        self.file_name_input.text = str(pathlib.Path(file_path).parts[-1])

    def save_file(self, file_path):
        saved_file_name = \
            self.file_manager.save_file(
                file_path,
                self.file_name_input.text,
                self.text_input.text)
        if saved_file_name:
            self.file_name_input.text = saved_file_name


class Tutorial(Screen):
    pass


class ManageFileMenu(Screen):
    pass


class License(Screen):
    pass


class MainMenu(Screen):
    pass


class MakodeditScreenManager(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(MainMenu(name="main"))
        self.add_widget(ManageFileMenu(name="manage_memo"))
        self.add_widget(Tutorial(name="tutorial"))
        self.add_widget(FileEdit(name="file_edit"))
        self.add_widget(License(name="license"))


class MakodeditApp(App):
    def build(self):
        self.title = "Makodedit"
        self.icon = "images/makodedit.png"
        return MakodeditScreenManager()


if __name__ == "__main__":
    if hasattr(sys, "_MEIPASS"):
        resource_add_path(sys._MEIPASS)
    MakodeditApp().run()
