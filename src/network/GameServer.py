# -*- coding : utf-8 -*-
'''
Created on 1 avr. 2014

@author: egor
'''
import socket


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
        hostaddr, port = serverSocket.getsockname()
        print("Server Run " + str(hostaddr) + " " + str(port))
        conn, addr = serverSocket.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
        conn.close()
    
    def run(self):
        '''
        
        '''
        
    def close(self):
        '''
        '''