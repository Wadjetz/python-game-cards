'''
Created on 11 mars 2014

@author: egor
'''
from engine.Entity import Entity
from engine.Serviteur import Serviteur


class CarteServiteur(Entity):
    '''
    classdocs
    '''


    def __init__(self, ID, name, description, health, mana, degats):
        '''
        Constructor
        '''
        Entity.__init__(self, ID, name, description, health, mana, degats)
    
    def getServiteur(self, parent):
        return Serviteur(int(self.ID)+10000, self.name, self.description, self.health, self.mana, self.degats, parent)
    
    def toString(self):
        return Entity.toString(self)