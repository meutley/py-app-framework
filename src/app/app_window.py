from core import message_dialog, window

class AppWindow(window.Window):
    def __init__(self, title, glade_manager):
        window.Window.__init__(self, title, glade_manager)