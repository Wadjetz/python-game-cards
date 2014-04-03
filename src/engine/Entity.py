'''
Created on 3 avr. 2014

@author: egor
'''

class Entity(object):
    '''
    Entité basique du jeux
    '''


    def __init__(self, ID, Type, name, attack, damageType, effect, description, dialog):
        '''
        Constructor
        @param ID: id unique de la carte
        @param Type: Type de la carte
        @param name: Nom
        @param attack: Degats
        @param damageType: type de degats
        @param effect: Effet speciale de l'entité
        @param description: Description
        @param dialog: dialog de la carte
        '''
        self.ID = int(ID)
        self.Type = Type
        self.name = name
        self.attack = int(attack)
        self.damageType = damageType
        self.effect = effect
        self.description = description
        self.dialog = dialog
        