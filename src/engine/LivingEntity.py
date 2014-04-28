'''
Created on 2 avr. 2014

@author: egor
'''
from engine.Entity import Entity


class LivingEntity(Entity):
    '''
    Entite vivant dans le jeu
    '''
    def __init__(self, ID, Type, name, attack, damageType, effect, description, dialog, health):
        '''
        Constructor
        @param health: Les points de vie
        @param attack: Degats
        '''
        Entity.__init__(self, ID, Type, name, attack, damageType, effect, description, dialog)
        self.health = int(health)
        self.action = False
        
    def domage(self, attack):
        '''
        Enleve de la vie a l'entite
        '''
        self.health -= int(attack)
        
    def nextTour(self, turn):
        '''
        Tour suivant
        '''
        self.action = True
    
