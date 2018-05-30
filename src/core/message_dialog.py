import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from enum import Enum

class MessageType(Enum):
    INFO = Gtk.MessageType.INFO
    QUESTION = Gtk.MessageType.QUESTION

class ButtonType(Enum):
    NONE = 0
    OK = 1
    CANCEL = 2
    YES = 3
    NO = 4

class ResponseType(Enum):
    NONE = -4
    OK = -5
    CANCEL = -6
    YES = -8
    NO = -9

class MessageDialogBase:
    __dlg = None

    __handlers = {
        ResponseType.NONE.value: None,
        ResponseType.OK.value: None,
        ResponseType.CANCEL.value: None,
        ResponseType.YES.value: None,
        ResponseType.NO.value: None
    }

    def __init__(self, parent, text, message_type):
        self.__dlg = Gtk.MessageDialog(parent,
            0,
            message_type.value,
            Gtk.ButtonsType.NONE,
            text)

    def add_button(self, button_type):
        # Add the button based on type
        if button_type == ButtonType.NONE:
            return self
        elif button_type == ButtonType.OK:
            self.__dlg.add_button("OK", Gtk.ResponseType.OK)
        elif button_type == ButtonType.CANCEL:
            self.__dlg.add_button("Cancel", Gtk.ResponseType.CANCEL)
        elif button_type == ButtonType.YES:
            self.__dlg.add_button("Yes", Gtk.ResponseType.YES)
        elif button_type == ButtonType.NO:
            self.__dlg.add_button("No", Gtk.ResponseType.NO)
        return self

    def set_response_handler(self, response_type, handler):
        if response_type.value in self.__handlers:
            self.__handlers[response_type.value] = handler
        return self

    def run(self):
        # Run the dialog and handle the response
        response = self.__dlg.run()
        self.__handle_response(response)
        self.__dlg.destroy()

    def __handle_response(self, response):
        # Run the response handler if it exists and it is callable
        if response in self.__handlers:
            handler = self.__handlers[response]
            if handler != None and callable(handler):
                handler()

class MessageDialog:
    @staticmethod
    def create(message_type, parent, text):
        try:
            return MessageDialogBase(parent, text, message_type)
        except KeyError:
            raise ValueError("message_type {0} is not supported".format(str(message_type)))