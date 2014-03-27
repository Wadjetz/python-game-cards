'''
Created on 11 mars 2014

@author: egor
'''

from engine.CarteServiteur import CarteServiteur
from engine.CarteSort import CarteSort
from engine.Entity import Entity
from engine.Terrain import Terrain


class Player(Entity):
    '''
    Joueur Principale
    @param main: Les cartes utilisable par le joueur
    '''
    def __init__(self, ID, name):
        '''
        Constructor
        '''
        
        Entity.__init__(self, ID, name, "description", 30, 1, 5)
        self.action = True
        self.main = {}

        
    def toString(self):
        '''
        Affiche les cartes que possede le joueur
        '''
        string = " Main = {\n"
        for key in self.main:
            carte = self.main[key]
            string += "\t"+ "ID=" + key + " " + carte.toString() + "\n"
        return Entity.toString(self) + string + "}\n"
    
    def nextTour(self, tour):
        '''
        Passe au tour suivant et augmente le mana en fonction du tour
        @param tour: Numero du tour
        '''
        if (tour > 10):
            self.mana = 10
        else:
            self.mana = tour
        
    def piocheCarte(self, terrain):
        '''
        Piche une nouvelle carte
        '''
        if (isinstance(self.main, dict) == True and isinstance(terrain, Terrain)):
            carte = terrain.piocheCarte()
            self.main[carte.ID] = carte
            
            
    def useCarte(self, carte, cible):
        '''
        Utilise une carte dans ca main
        @param carte: la carte a utiliser
        @param cible: Cible de l'utilisation soit le terrain ou un joueur ou un serviteur
        '''
        if (isinstance(carte, CarteServiteur) == True):
            return carte.getServiteur(self)
        if (isinstance(carte, CarteSort) == True):
            return carte.attaque(cible)
        self.__remouveCarte(carte)
            
    def getCarte(self, ID_carte):
        '''
        Recupere la carte dans la main du joueur
        @param ID_carte: Id de la carte
        '''
        if self.main.has_key(str(ID_carte)):
            return self.main[str(ID_carte)]
        else:
            print("J'ai pas cette carte")
    
    def __remouveCarte(self, ID_carte):
        '''
        Supprime un carte de la main du joueur
        @param ID_carte: Id de la carte
        '''
        if self.main.has_key(ID_carte):
            del self.main[ID_carte]
        
        
