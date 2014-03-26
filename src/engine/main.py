# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''
from engine.Pioche import Pioche
from engine import Terrain
from engine.Player import Player
#from engine.Player import Player
#from engine.Terrain import Terrain


def main():
    print("Game Run")
    pioche = Pioche()
    
    
    player1 = Player("Egor")
    player2 = Player("Quentin")
    
    terran = Terrain(pioche, player1, player2)
    
    print(pioche.getCarte().toString())
    print(pioche.getCarte().toString())
    


if __name__ == '__main__':main()