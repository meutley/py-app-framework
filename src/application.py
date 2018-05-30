from core import glade_manager, initialize, message_dialog
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

    def run(self):
        # Show the window and run Gtk main
        message = "This is a test message dialog."

        self.__window.show()
        message_dialog.MessageDialog                                                      \
            .create(message_dialog.MessageType.INFO, self.__window.gtk_window(), message) \
            .add_button(message_dialog.ButtonType.OK)                                     \
            .add_button(message_dialog.ButtonType.CANCEL)                                 \
            .set_response_handler(message_dialog.ResponseType.OK, self.__on_ok)           \
            .set_response_handler(message_dialog.ResponseType.CANCEL, self.__on_cancel)   \
            .run()
        initialize.gtk_main()

    def __on_ok(self):
        print("Clicked OK button")

    def __on_cancel(self):
        print("Clicked Cancel button")