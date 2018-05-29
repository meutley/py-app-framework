import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Window:
    _glade_manager = None
    _window = None
    __title = "(Window)"

    _handlers = {}

    def __init__(self, title, glade_manager):
        if title != None:
            self.__title = title
        
        self._glade_manager = glade_manager
        self._init_window()

    def _init_window(self):
        self._window = self._glade_manager.get_object("main_app_window")
        self._window.set_title(self.__title)
        self._window.connect("destroy", Gtk.main_quit)
        self._glade_manager.connect_signals(self._handlers)

    def show(self):
        self._window.show_all()
        Gtk.main()