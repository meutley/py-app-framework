import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def info(parent, text, on_ok = None):
    dlg = Gtk.MessageDialog(parent,
        0,
        Gtk.MessageType.INFO,
        Gtk.ButtonsType.OK,
        "Login Clicked")
    dlg.run()
    __run_callback(on_ok)
    dlg.destroy()

def question(parent, text, on_yes = None, on_no = None, on_cancel = None):
    dlg = Gtk.MessageDialog(parent,
        0,
        Gtk.MessageType.QUESTION,
        Gtk.ButtonsType.YES_NO,
        text)

    result = dlg.run()
    if result == Gtk.ResponseType.YES:
        __run_callback(on_yes)
    elif result == Gtk.ResponseType.NO:
        __run_callback(on_no)

    dlg.destroy()

def __run_callback(callback):
    if callback != None and callable(callback):
        callback()