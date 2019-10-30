import threading
import sys

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gio,Gdk,Gtk


def callGtk():
    print("gtk started")
    Gtk.main()

#*******************************************************************************
#                               gtk eventhandler
#*******************************************************************************

class EventHandler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")
        gtk_style()

#*******************************************************************************
#                               gtk winmain
#*******************************************************************************

class MainBuilder(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_from_file("./forms/winmain.glade")
        self.connect_signals(EventHandler())

    def get_mainwindow(self):
        return self.get_object("winMain")

def gtk_style():
    css = "./assets/css/style.css"
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path(css)

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )


#*******************************************************************************
#                               gtk mainthread
#*******************************************************************************

gtk_style()
mainBuilder = MainBuilder()
window = mainBuilder.get_mainwindow()
#self.style()
window.show_all()

gtkThread = threading.Thread(target=Gtk.main)
gtkThread.start()
#Gtk.main()
