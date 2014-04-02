'''
Created on 2 avr. 2014

@author: egor
'''
from engine.Card import Card


class CardSpell(Card):
    '''
    Carte Sort
    '''

    def __init__(self, ID, Type, name, description, dialog, cost, attack, damage, effect):
        '''
        Constructor
        '''
        Card.__init__(self, ID, Type, name, description, dialog, cost, attack, damage, effect)
        
    def fight(self):
        '''
        La CarteSpell inflige des degats
        '''
        print()
        
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[cost=" + str(self.cost) + " mana , degats=" + str(self.attack) + ", damage=" + str(self.damage) + ", effect=" + str(self.effect) + "]"
        #txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
