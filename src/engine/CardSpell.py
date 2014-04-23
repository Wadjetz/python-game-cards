'''
Created on 2 avr. 2014

@author: egor
'''
from engine.Card import Card


class CardSpell(Card):
    '''
    Carte Sort
    '''

    def __init__(self, ID, Type, name, attack, damageType, effect, description, dialog, cost):
        '''
        Constructor
        '''
        Card.__init__(self, ID, Type, name, attack, damageType, effect, description, dialog, cost)
        
    def health(self, target):
        '''
        La CarteSpell inflige des degats
        '''
        if self.effect == "health":
            target.health += self.attack
            
        
    def toString(self):
        txt = str(self.ID) + " : " + str(self.name) + "\t"
        txt += ":[" + str(self.cost) + "pM, " + str(self.attack) + "dmg, " + str(self.damageType) + ", " + str(self.effect) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
