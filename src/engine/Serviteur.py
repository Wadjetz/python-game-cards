'''
Created on 11 mars 2014

@author: egor
'''
from engine.Entity import Entity

class Serviteur(Entity):
    '''
    Serviteur
    @param parent: Le maitre du serviteur
    @param autres: Voir la classe mere : Entity
    '''

    def __init__(self, ID, name, description, health, mana, degats, parent):
        '''
        Constructor
        '''
        Entity.__init__(self, ID, name, description, health, mana, degats)
        self.parent = parent
        
    def servAttaque(self, ID_cible, playerCible):
        '''
        L'entite attaque si c'est un serviteur il s'inflige mutuellement les degats
        @param jouer: Le joueur a attaquer
        '''
        if self.action == True:
            servCible = playerCible.getServiteur(ID_cible)
            self.attaque(servCible)
            servCible.attaque(self)
            self.action = False
        else:
            raise Exception("Tu peux pas attaquer")
            
    def toString(self):
        return Entity.toString(self)
