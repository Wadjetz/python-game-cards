# -*- coding : utf-8 -*-
'''
Created on 1 avr. 2014

@author: egor
'''
import socket
import pickle
import select
from engine import Player
from engine import Deck
from engine.Deck import Pioche
from engine import Area
import asyncore
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
        serverSocket.listen(10)
        
        conn = serverSocket.accept()
        print(conn)
        game = Area('Damien', 'thib')
        game.gameLoopNetworkHost(self, conn)
    
    def run(self, game, conn):
        '''
        Permet d'envoyer au client les informations sur l'état de la game
        '''
        data = pickle.dumps(game)
        print(conn)
        conn.send(data)
        return self.receive(conn)

        
    def receive(self, conn):
        '''
        Recoit les informations envoyé par le client
        '''
        data = bytes()
        while 1:
            paquet = conn.recv(1024)
            if not paquet: break
            data += paquet
        game = pickle.loads(data)
        return game
    
    def close(self, conn):
        '''
        Ferme le serveur
        '''
        conn.close()