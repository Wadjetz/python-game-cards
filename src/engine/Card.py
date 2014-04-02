'''
Created on 26 mars 2014

@author: egor
'''

class Card():
    '''
    Card
    '''

    def __init__(self, ID, Type, name, description, dialog, cost, attack, damage, effect):
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
        self.effect = effect
        
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[cost=" + str(self.cost) + " mana , degats=" + str(self.attack) + ", damage=" + str(self.damage)
        #txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
