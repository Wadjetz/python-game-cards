'''
Created on 26 mars 2014

@author: egor
'''
import random

from engine.Servant import Servant


class Card():
    '''
    Card
    '''

    def __init__(self, ID, Type, name, description, dialog, cost, attack, damage):
        '''
        Constructor
        @param ID: id unique de la carte
        @param Type: Type de la carte
        @param name: Nom
        @param description: Description
        @param dialog: dialog de la carte
        @param cost: cout en mana de la carte
        @param attack: Degats
        @param damage: type de degats
        '''
        self.ID = int(ID)
        self.Type = Type
        self.name = name
        self.description = description
        self.dialog = dialog
        self.cost = int(cost)
        self.attack = int(attack)
        self.damage = damage
        
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[cost=" + str(self.cost) + " mana , degats=" + str(self.attack) + ", damage=" + str(self.damage)
        #txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    

class CardServant(Card):
    '''
    CardServiteur
    '''


    def __init__(self, ID, Type, name, description, dialog, cost, attack, damage, health, vulnerability):
        '''
        Constructor
        '''
        Card.__init__(self, ID, Type, name, description, dialog, cost, attack, damage)
        self.health = health
        self.vulnerability = vulnerability
    
    
    def invokeServant(self):
        #ID, Type, name, description, dialog, attack, damage, health, vulnerability
        return Servant(int(self.ID)+1000000+random.randrange(100000), self.Type, self.name, self.description, self.dialog, self.attack, self.damage, self.health, self.vulnerability)
    
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[cost=" + str(self.cost) + " mana , degats=" + str(self.attack) + ", damage=" + str(self.damage) + ", health=" + str(self.health) + ", vulnerability=" + str(self.vulnerability) + "]"
        #txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    

class CardSpell(Card):
    '''
    Carte Sort
    '''

    def __init__(self, ID, Type, name, description, dialog, cost, attack, damage, effect):
        '''
        Constructor
        '''
        Card.__init__(self, ID, Type, name, description, dialog, cost, attack, damage)
        self.effect = effect
        

    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[cost=" + str(self.cost) + " mana , degats=" + str(self.attack) + ", damage=" + str(self.damage) + ", effect=" + str(self.effect) + "]"
        #txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
