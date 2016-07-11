#!usr/bin/python

import threading
import gtk
import gobject
import socket
import re
import time
import datetime


gobject.threads_init()

class MainWindow(gtk.Window):
    def __init__(self):
        #Initialize base gtk window class
        super(MainWindow, self).__init__()

        #Create controls
        self.set_title("IM CLient")
        vbox = gtk.VBox()
        hbox = gtk.HBox()
        self.username_label = gtk.Label()
        self.text_entry = gtk.Entry()
        send_button = gtk.Button("Send")
        self.text_buffer = gtk.TextBuffer()
        text_view = gtk.TextView(self.text_buffer)