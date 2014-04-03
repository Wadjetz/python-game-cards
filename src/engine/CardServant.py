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


    def __init__(self, ID, Type, name, description, dialog, cost, attack, damage, health, effect):
        '''
        Constructor
        '''
        Card.__init__(self, ID, Type, name, description, dialog, cost, attack, damage, effect)
        self.health = health
    
    
    def invokeServant(self):
        #ID, Type, name, description, dialog, attack, damage, health, vulnerability
        return Servant(int(self.ID)+1000000+random.randrange(100000), self.Type, self.name, self.description, self.dialog, self.attack, self.damage, self.health, self.effect)
    
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name) + "\t"
        txt += ":[" + str(self.cost) + "pM, " + str(self.attack) + "dmg, " + str(self.damage) + ", " + str(self.health) + "pV, " + str(self.effect) + "]"
        #txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
