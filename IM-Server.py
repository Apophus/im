#!usr/bin/python

#The server-side of the instant messenger

import threading
import socket
import re
import signal
import time

class Server():
    def __init__(self, port):
    #create a socket and bind it to a port
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind(('', port))
        self.listener.listen(1)
        print "listening on port{0}".format(port)

    #Used to store ll of the client sockets we have for echoing to them

        self.client_sockets = []

    #Run the function self.signal_handler when CTRL+C is pressed

        signal.signal(signal.SIGNIT, self.signal_handler)

    def run(self):

        #LIsten for client threads and create a ClientThread for each new client
        while True:

            print 'Listening for more clients'

            try:
                (client_socket, client_address) = self.listener.accept()
            except socket.error:
                sys.exit('Could not accept any more connections')

        self.client_sockets.append(client_socket)

        print 'Starting client thread for {0}'.format(client_address)

        client_thread = ClientListener(self, client_socket, client_address)

        client_thread.start()

        time.sleep(0.1)


    def echo(self, data):

        #Send a message to each socketin self.client socket
        print 'echoing: {0}'.format(data)

        for socket in self.client_sockets:

            #Try and echo to all clients
            try:
                socket.sendall(data)
            except socket.error:
                print 'Unable to send message'


    def remove(self, socket):

        #Remove specified socket from the client's socket's list

        self.client_sockets.remove(socket)
    def  signal_handler(self, signal, frame):

        print 'Tidying up'
        #Stop listening for new connections
        self.listener.close()

        #LET each client know that we're quitting
        self.echo('QUIT')

