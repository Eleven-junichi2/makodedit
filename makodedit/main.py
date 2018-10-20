import pathlib
import sys

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.codeinput import CodeInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path

LabelBase.register("NotoSansCJKjp-Light",
                   fn_regular="./fonts/NotoSansCJKjp-Light.otf")

LabelBase.register("NotoSansMonoCJKjp-Regular",
                   fn_regular="./fonts/NotoSansMonoCJKjp-Regular.otf")


Window.size = (360, 640)


DATA_DIR_NAME = "data"

__file__ = sys.argv[0]


def data_dir(data_dir_name) -> pathlib.Path:
    """return data dir as pathlib.Path"""
    path = pathlib.Path(__file__).parent
    path = path / data_dir_name
    return path


def check_exist_data_dir(data_dir: "As Path object."):
    path = data_dir
    if not path.is_dir():
        path.mkdir()


class DialogSavedLayout(RelativeLayout):
    saved_file_name = StringProperty(None)
    popup = ObjectProperty(None)

    def __init__(self, saved_file_name, popup, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.saved_file_name = saved_file_name
        self.popup = popup


class DialogLoadLayout(RelativeLayout):
    file_manage_user = ObjectProperty(None)
    file_manager = ObjectProperty(None)
    data_dir = ObjectProperty(None)
    popup = ObjectProperty(None)

    def __init__(self, file_manage_user, file_manager, data_dir, popup,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_manage_user = file_manage_user
        self.file_manager = file_manager
        self.data_dir = data_dir
        self.popup = popup


class DialogSaved(Popup):
    def __init__(self, saved_file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint = (0.9, 0.9)
        self.title = " "
        self.content = DialogSavedLayout(saved_file_name, self)


class DialogLoad(Popup):
    def __init__(self, file_manage_user, file_manager, data_dir,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint = (0.9, 0.9)
        self.title = " "
        self.content = DialogLoadLayout(
            file_manage_user, file_manager, data_dir, self)


class MakodeditFileManage:
    def __init__(self, file_manage_user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        check_exist_data_dir(data_dir(DATA_DIR_NAME))
        self.data_dir_path = data_dir(DATA_DIR_NAME)
        self.file_manage_user = file_manage_user
        self.loaded_file_text = ""

    def load_file(self, file_name):
        file_path = self.data_dir_path / file_name
        file_name = file_path.parts[-1]
        with open(str(file_path), "r") as file_obj:
            return file_obj.read(), file_name

    def save_file(self, file_name, text):
        file_name = str(file_name)
        text = str(text)
        if not(file_name == "" or text == ""):
            # self.data_dir_path: pathlib.Path object
            with open(str(self.data_dir_path / file_name), "w") as file_obj:
                file_obj.write(text)
            return True
        else:
            return False

    def dialog_saved(self, saved_file_name):
        popup = DialogSaved(saved_file_name)
        popup.open()

    def dialog_load(self):
        popup = DialogLoad(self.file_manage_user, self, self.data_dir_path)
        popup.open()


class MakodeditCodeInput(CodeInput):
    def change_style(self, style_name="default"):
        self.style_name = style_name
        # -- Reset self.text for apply style.
        tmp = self.text
        self.text = ""
        self.text = tmp
        # --


class EditMemo(Screen):
    file_title = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_manage = MakodeditFileManage(self)

    def save(self, file_name, text):
        saved = self.file_manage.save_file(file_name, text)
        if saved:
            self.file_manage.dialog_saved(file_name)

    def load(self):
        self.file_manage.dialog_load()


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
        self.add_widget(EditMemo(name="edit_memo"))
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
