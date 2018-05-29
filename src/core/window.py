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

    def _init_window(self, object_name):
        # Get the glade object, set the title and connect signals
        self._window = self._glade_manager.get_object(object_name)
        self._window.set_title(self.__title)
        self._window.connect("destroy", Gtk.main_quit)
        self._glade_manager.connect_signals(self._handlers)

    def initialize(self, object_name):
        self._init_window(object_name)

    def show(self):
        self._window.show_all()