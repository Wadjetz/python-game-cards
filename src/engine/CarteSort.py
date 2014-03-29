'''
Created on 11 mars 2014

@author: egor
'''
from engine.Entity import Entity

class CarteSort(Entity):
    '''
    classdocs
    '''

    def __init__(self, ID, name, description, health, mana, degats):
        '''
        Constructor
        '''
        Entity.__init__(self, ID, name, description, health, mana, degats)
        

    def toString(self):
        return Entity.toString(self)
        