'''
Created on 11 mars 2014

@author: egor
'''
from copy import copy
import random

from engine import CarteServiteur, CarteSort


class Pioche(object):
    '''
    Contient tous les cartes du jeux
    '''
    def __init__(self):
        '''
        Constructor
        ''' 
        self.decks = []
        self.__load()
    
    def __load(self):
        '''
        Charge les cartes stocker dans un fichier
        '''
        fichier = open("../save/Cartes", "r")
        
        for line in fichier:
            line = line.rstrip("\n")
            tab = line.split("|")
            if (tab[0] == "Serv" and len(tab) == 7):
                carte = CarteServiteur.CarteServiteur(tab[1], tab[2], tab[3], tab[4], tab[5], tab[6])
                self.decks.append(carte)
            if (tab[0] == "Sort" and len(tab) == 7):
                carte = CarteSort.CarteSort(tab[1], tab[2], tab[3], tab[4], tab[5], tab[6])
                self.decks.append(carte)
            
        fichier.close()
    
    def getCarte(self):
        '''
        Recupere un carte au hasard dans le total des cartes
        '''
        i = random.randrange(len(self.decks))
        tmp = copy(self.decks[i])
        del self.decks[i]
        return tmp
        
    def toString(self):
        return self.decks
        