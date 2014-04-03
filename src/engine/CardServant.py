'''
Created on 2 avr. 2014

@author: egor
'''
import random

from engine.Card import Card
from engine.Servant import Servant


class CardServant(Card):
    '''
    CardServiteur
    '''

    def __init__(self, ID, Type, name, attack, damageType, effect, description, dialog, cost, health):
        '''
        Constructor
        @param health: Les points de vie
        '''
        Card.__init__(self, ID, Type, name, attack, damageType, effect, description, dialog, cost)
        self.health = health
    
    
    def invokeServant(self):
        #Iself, ID, Type, name, attack, damageType, effect, description, dialog, health
        ID = int(self.ID)+1000000+random.randrange(100000)
        return Servant(ID, self.Type, self.name, self.attack, self.damageType, self.effect, self.description, self.dialog, self.health)
    
    def toString(self):
        txt = str(self.ID) + " : " + str(self.name) + "\t"
        txt += ":[" + str(self.cost) + "pM, " + str(self.attack) + "dmg, " + str(self.damageType) + ", " + str(self.health) + "pV, " + str(self.effect) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
