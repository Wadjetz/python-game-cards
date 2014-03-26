# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''
from engine.Carte import Carte
from engine.Pioche import Pioche
from engine.Player import Player
from engine.Terrain import Terrain


def main():
    
    pioche = Pioche()
    
    
    laMainJouer1 = [Carte("Pion", 6, 10, 3), Carte("Pion", 6, 22, 3), Carte("Pion", 6, 22, 3), Carte("Pion", 6, 22, 3),Carte("Pion", 6, 22, 3)]
    laMainJouer2 = [Carte("Pion", 6, 22, 3), Carte("Pion", 6, 22, 3), Carte("Pion", 6, 22, 3), Carte("Pion", 6, 22, 3),Carte("Pion", 6, 22, 3)]
    
    jouer1 = Player("Egor")
    jouer2 = Player("Connard")
    
    terrain = Terrain(pioche, jouer1, jouer2)
    
    jouer1.display()
    jouer2.display()
    
    jouer1.attaque(jouer2, laMainJouer1[0])
    
    jouer1.display()
    jouer2.display()

if __name__ == '__main__':main()