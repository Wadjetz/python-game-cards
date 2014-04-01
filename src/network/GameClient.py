'''
Created on 1 avr. 2014

@author: egor
'''
import socket

class GameClient(object):
    '''
    classdocs
    '''


    def __init__(self, HOST, PORT):
        '''
        Constructor
        '''

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((HOST, PORT))
        clientSocket.sendall(b'Hello, world')
        data = clientSocket.recv(1024)
        clientSocket.close()
        print('Received', repr(data))