from core import window

class AppWindow(window.Window):
    _glade_object_name = "main_app_window"
    
    def __init__(self, title, glade_manager):
        window.Window.__init__(self, title, glade_manager)