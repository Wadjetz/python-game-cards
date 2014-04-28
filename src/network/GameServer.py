# -*- coding : utf-8 -*-
'''
Created on 1 avr. 2014

@author: egor
'''
import socket
import pickle
from engine import Area
class GameServer():
    '''
    classdocs
    '''

    def __init__(self, HOST, PORT):
        '''
        Constructor
        '''   
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Serveur run " + str(HOST) + ":" + str(PORT))
        serverSocket.bind((HOST, PORT))
        serverSocket.listen(5)
        
        conn = serverSocket.accept()
        game = Area('Damien', 'thib')
        game.gameLoopNetworkHost(self, conn)
    
    def run(self, game, conn):
        '''
        Permet d'envoyer au client les informations sur l'état de la game
        '''
        data = pickle.dumps(game)
        conn[0].sendall(data)
        conn[0].sendall(b"fin")
        return self.receive(conn)

        
    def receive(self, conn):
        '''
        Recoit les informations envoyé par le client
        '''   
        data = bytes()
        while 1:
            paquet = conn[0].recv(8162)
            if paquet == b"fin": 
                break
            data += paquet
        game = pickle.loads(data)
        return game

    def close(self, conn):
        '''
        Ferme le serveur
        '''
        conn[0].close()