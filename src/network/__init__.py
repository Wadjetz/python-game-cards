# -*- coding : utf-8 -*-
'''
Gestion du reseau
'''
from network.GameServer import GameServer


def main():
    gameServer = GameServer("localhost", 9999)
    gameServer.run()
    

if __name__ == '__main__':main()