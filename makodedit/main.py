import pathlib

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.codeinput import CodeInput
from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window
from kivy.core.text import LabelBase

LabelBase.register("NotoSansCJKjp-Light",
                   fn_regular="./fonts/NotoSansCJKjp-Light.otf")

LabelBase.register("NotoSansMonoCJKjp-Regular",
                   fn_regular="./fonts/NotoSansMonoCJKjp-Regular.otf")


Window.size = (360, 640)


DATA_DIR_NAME = "data"


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


class DialogLoadedLayout(RelativeLayout):
    loaded_file_name = StringProperty(None)
    popup = ObjectProperty(None)

    def __init__(self, loaded_file_name, popup, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loaded_file_name = loaded_file_name
        self.popup = popup


class DialogSaved(Popup):
    def __init__(self, saved_file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.saved_file_name = saved_file_name
        self.size_hint = (0.9, 0.9)
        self.content = DialogSavedLayout(saved_file_name, self)


class DialogLoaded(Popup):
    def __init__(self, loaded_file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loaded_file_name = loaded_file_name
        self.size_hint = (0.9, 0.9)
        self.content = DialogLoadedLayout(loaded_file_name, self)


class MakodeditFileManage:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        check_exist_data_dir(data_dir(DATA_DIR_NAME))
        self.data_dir_path = data_dir(DATA_DIR_NAME)

    def load_file(self, file_name):
        with open(str(self.data_dir_path / file_name), "r") as file_obj:
            return file_obj.read()

    def save_file(self, file_name, text):
        file_name = str(file_name)
        text = str(text)
        if not(file_name == "" or text == ""):
            # self.data_dir_path: pathlib.Path object
            file_name = str(self.data_dir_path / file_name)
            with open(file_name, "w") as file_obj:
                file_obj.write(text)
            return True
        else:
            return False

    def dialog_saved(self, saved_file_name):
        popup = DialogSaved(saved_file_name)
        popup.open()

    def dialog_loaded(self, loaded_file_name):
        popup = DialogLoaded(loaded_file_name)
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
    text_input = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_manage = MakodeditFileManage()

    def save(self, file_name, text, show_dialog=True):
        saved = self.file_manage.save_file(file_name, text)
        if saved and show_dialog:
            self.file_manage.dialog_saved(file_name)


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


if __name__ == "__main__":
    print(LabelBase.get_system_fonts_dir())
    MakodeditApp().run()
