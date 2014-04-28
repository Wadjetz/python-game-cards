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
        return self.receive(conn)

        
    def receive(self, conn):
        '''
        Recoit les informations envoyé par le client
        '''
        import select
        ready = select.select([conn[0]],[] ,[], 50000)
        if  ready[0]:        
            data = bytes()
            while 1:
                paquet = conn[0].recv(1024)
                if not paquet: 
                    break
                data += paquet
            game = pickle.loads(data)
            return game

    def close(self, conn):
        '''
        Ferme le serveur
        '''
        conn[0].close()