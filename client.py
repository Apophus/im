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

        #Connect events
        self.connect("destroy", self.graceful_quit)
        send_button.connect("clicked", self.send_message)
        #Activate when user presses enter
        self.text_entry.connect("activate", self.send_message)

         #Do layout
        vbox.pack_start(text_view)
        hbox.pack_start(self.username_label, expand=False)
        hbox.pack_start(self.text_entry)
        hbox.pack_end(hbox, expand=False)

        #Display
        self.add(vbox)
        self.show_all()

        #Configurations
        self.configure()

    def ask_for_info(selfself, question):

        dialog = gtk.MessageDialog(parent=self, type=gtk.MESSAGE_QUESTION)

