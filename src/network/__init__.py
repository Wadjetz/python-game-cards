# -*- coding : utf-8 -*-
'''
Gestion du reseau
'''
from network.GameServer import GameServer
from engine.Area import Area


def main():
    
    GameServer('localhost', 9999)

if __name__ == '__main__':main()