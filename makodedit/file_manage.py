from abc import ABCMeta, abstractmethod

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


class FileBrowserDialogLayout(RelativeLayout):
    file_manage_user = ObjectProperty(None)
    file_manager = ObjectProperty(None)
    popup = ObjectProperty(None)

    def __init__(self, file_manage_user, file_manager, popup,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_manage_user = file_manage_user
        self.file_manager = file_manager
        self.popup = popup


class FileSaveDialogLayout(FileBrowserDialogLayout):
    pass


class FileLoadDialogLayout(FileBrowserDialogLayout):
    pass


class FileBrowserDialog(Popup):
    def __init__(self, file_manage_user, file_manager,
                 dialog_layout,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint = (0.9, 0.9)
        self.title = " "
        self.content = dialog_layout(file_manage_user, file_manager, self)


class FileSaveDialog(FileBrowserDialog):
    def __init__(self, file_manage_user, file_manager,
                 dialog_layout=FileSaveDialogLayout,
                 *args, **kwargs):
        super().__init__(file_manage_user, file_manager, dialog_layout,
                         *args, **kwargs)


class FileLoadDialog(FileBrowserDialog):
    def __init__(self, file_manage_user, file_manager,
                 dialog_layout=FileLoadDialogLayout,
                 *args, **kwargs):
        super().__init__(file_manage_user, file_manager, dialog_layout,
                         *args, **kwargs)


class FileManager(metaclass=ABCMeta):
    """
    Example:

    class ExampleFileManager(FileManager):
        def load_file(self):
            pass

        def save_file(self):
            pass

    class ExampleFileManageUser(Widget):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.file_manager = ExampleFileManager(self)
    """

    def __init__(self, file_manage_user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_manage_user = file_manage_user

    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass

    def save_dialog(self):
        popup = FileSaveDialog(self.file_manage_user, self)
        popup.open()

    def load_dialog(self):
        popup = FileLoadDialog(self.file_manage_user, self)
        popup.open()
