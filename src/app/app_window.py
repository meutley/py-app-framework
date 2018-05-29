from core import message_dialog, window

class AppWindow(window.Window):
    def __init__(self, title, glade_manager):
        window.Window.__init__(self, title, glade_manager)

    def _init_window(self):
        window.Window._handlers = {
            "on_btn_login_clicked": self.__on_btn_login_clicked
        }

        window.Window._init_window(self)

    def __on_btn_login_clicked(self, e):
        parent = self._window
        message_dialog.info(parent, "Login clicked!")