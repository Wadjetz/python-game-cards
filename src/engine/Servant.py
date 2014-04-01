'''
Created on 11 mars 2014

@author: egor
'''

class Servant():

    def __init__(self, ID, Type, name, description, dialog, attack, damage, health, vulnerability):
        '''
        Constructor
        @param ID: id unique de la carte
        @param Type: Type de la carte
        @param name: Nom
        @param description: Description
        @param dialog: dialog de la carte
        @param attack: Degats
        @param damage: type de degats
        '''
        self.ID = int(ID)
        self.Type = Type
        self.name = name
        self.description = description
        self.health = health
        self.dialog = dialog
        self.attack = int(attack)
        self.damage = damage
        self.vulnerability = vulnerability
    
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[health=" + str(self.health) + " pv, degats=" + str(self.attack) + ", damage=" + str(self.damage)
        txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + ", vulnerability=" + str(self.vulnerability) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
