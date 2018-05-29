from core import glade_manager, initialize
from app import app_window

class Application:
    __name = ""
    __window = None
    __glade_manager = None
    
    def __init__(self, name):
        # Set up the application and initialize the main window
        self.__glade_manager = glade_manager.GladeManager("./resources/gtk/app_ui.glade")
        self.__name = name if name != None else "Application"
        self.__window = app_window.AppWindow(self.__name, self.__glade_manager)
        self.__window.initialize("main_app_window")

    def run(self):
        # Show the window and run Gtk main
        self.__window.show()
        initialize.gtk_main()