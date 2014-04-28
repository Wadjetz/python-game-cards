'''
Created on 1 avr. 2014

@author: egor
'''
import select
import socket
import pickle
from engine import Area
class GameClient(object):
    '''
    classdocs
    '''


    def __init__(self, HOST, PORT):
        '''
        Constructor
        '''
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((HOST, PORT))
        data = bytes()
        paquet = bytes()
        while 1:
            paquet = self.clientSocket.recv(8126)
            print(paquet)
            if paquet == b"fin":
                game=pickle.loads(data)
                game = game.gameLoopNetworkClient()
                data = pickle.dumps(game)
                self.clientSocket.send(data)
                self.clientSocket.send(b"fin")        
                data = None
                data = bytes()
            data += paquet