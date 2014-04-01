'''
Created on 11 mars 2014

@author: egor
'''
from engine.Player import Entity


class Servant(Entity):

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
        Entity.__init__(self, ID, name, health, attack)
        self.Type = Type
        self.description = description
        self.dialog = dialog
        self.damage = damage
        self.vulnerability = vulnerability
    
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[health=" + str(self.health) + " pv, degats=" + str(self.attack) + ", action=" + str(self.action) + ", damage=" + str(self.damage)
        #txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + ", vulnerability=" + str(self.vulnerability) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
