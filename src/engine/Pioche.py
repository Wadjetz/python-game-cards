'''
Created on 11 mars 2014

@author: egor
'''
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
        file = open("../save/Cartes", "r")
        
        for line in file:
            line = line.rstrip("\n")
            tab = line.split("|")
            
            if (tab[0] == "Sort" and len(tab) == 6):
                carte = CarteServiteur.CarteServiteur(tab[1], tab[2], tab[3], tab[4], tab[5])
                self.decks.append(carte)
            if (tab[0] == "Serv"):
                carte = CarteSort.CarteSort(tab[1], tab[2], tab[3], tab[4], tab[5])
                self.decks.append(carte)
            
        file.close()
    
    def getCarte(self):
        return random.choice(self.decks)
        
    def dispaly(self):
        print(self.toString())
        
    def toString(self):
        return self.decks
        