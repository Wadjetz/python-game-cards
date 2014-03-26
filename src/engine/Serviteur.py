'''
Created on 11 mars 2014

@author: egor
'''
from engine.Entity import Entity

class Serviteur(Entity):
    '''
    Serviteur
    '''

    def __init__(self, name, name, description, vie, mana, degats):
        '''
        Constructor
        '''
        Entity.__init__(self, name, description, vie, mana, degats)