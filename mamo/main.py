import pathlib

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.codeinput import CodeInput
# from kivy.uix.floatlayout import FloatLayout
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


class MakodeditFileBrowser(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        check_exist_data_dir(data_dir(DATA_DIR_NAME))


# class LoadDialog(FloatLayout):
#     load = ObjectProperty(None)
#     cancel = ObjectProperty(None)


# class SaveDialog(FloatLayout):
#     save = ObjectProperty(None)
#     text_input = ObjectProperty(None)
#     cancel = ObjectProperty(None)

# class LoadDialog(Popup):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.content = MakodeditFileBrowser()


class MakodeditCodeInput(CodeInput):
    def change_style(self, style_name="default"):
        self.style_name = style_name
        # -- Reset self.text for apply style.
        tmp = self.text
        self.text = ""
        self.text = tmp
        # --


class EditMemo(Screen):
    code_input = ObjectProperty(None)
    # loadfile = ObjectProperty(None)
    # savefile = ObjectProperty(None)
    # text_input = ObjectProperty(None)

    # def dismiss_popup(self):
    #     self._popup.dismiss()

    # def show_load(self):
    #     content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
    #     self._popup = Popup(title="Load file", content=content,
    #                         size_hint=(0.9, 0.9))
    #     self._popup.open()

    # def show_save(self):
    #     content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
    #     self._popup = Popup(title="Save file", content=content,
    #                         size_hint=(0.9, 0.9))
    #     self._popup.open()

    # def load(self, path, filename):
    #     with open(os.path.join(path, filename[0])) as stream:
    #         self.text_input.text = stream.read()

    #     self.dismiss_popup()

    # def save(self, path, filename):
    #     with open(os.path.join(path, filename), 'w') as stream:
    #         stream.write(self.text_input.text)

    #     self.dismiss_popup()


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
        self.add_widget(MakodeditFileBrowser(name="file_browser"))


class MakodeditApp(App):
    def build(self):
        self.title = "Makodedit"
        self.icon = "images/makodedit.png"
        return MakodeditScreenManager()


if __name__ == "__main__":
    print(LabelBase.get_system_fonts_dir())
    MakodeditApp().run()
