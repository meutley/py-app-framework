import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GladeManager:
    __builder = None

    def __init__(self, filePath):
        self.__builder = Gtk.Builder()
        self.__builder.add_from_file(filePath)

    def get_object(self, name):
        return self.__builder.get_object(name)

    def connect_signals(self, handlers):
        self.__builder.connect_signals(handlers)