from core import glade_manager
from app import app_window

class Application:
    __name = ""
    __window = None
    __glade_manager = None
    
    def __init__(self, name):
        self.__glade_manager = glade_manager.GladeManager("../resources/gtk/main_app_window.glade")
        self.__name = name if name != None else "Application"
        self.__window = app_window.AppWindow(self.__name, self.__glade_manager)

    def run(self):
        self.__window.show()