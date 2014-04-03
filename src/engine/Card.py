'''
Created on 26 mars 2014

@author: egor
'''
from engine.Entity import Entity


class Card(Entity):
    '''
    Card
    '''
    def __init__(self, ID, Type, name, attack, damageType, effect, description, dialog, cost):
        '''
        Constructor
        @param cost: cout en mana de la carte
        '''
        Entity.__init__(self, ID, Type, name, attack, damageType, effect, description, dialog)
        self.cost = int(cost)

        
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[" + str(self.cost) + "pm, " + str(self.attack) + "dmg, " + str(self.damageType)
        return txt
    
    def __str__(self):
        return self.toString()
    
