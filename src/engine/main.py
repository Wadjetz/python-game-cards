# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''
from engine.Pioche import Pioche
from engine.Player import Player
from engine.Terrain import Terrain


def main():
    print("Game Run")
    
    pioche = Pioche()
    
    #On Cree les joueurs
    player1 = Player(1, "Egor")
    player2 = Player(2, "Quentin")
    
    terrain = Terrain(pioche, player1, player2)
    
    #les joueur pioches 4 cartes
    for i in range(4):
        player1.piocheCarte(terrain)
        player2.piocheCarte(terrain)
        

    print(player1.toString())
    print(player2.toString())
    
    ID_carte = input("Id de la carte a utiliser")
    player1.useCarte(player1.getCarte(ID_carte), player2)
    
    
    print(player1.toString())
    print(player2.toString())
    


if __name__ == '__main__':main()