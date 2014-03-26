'''
Created on 26 mars 2014

@author: egor
'''

class Entity():
    '''
    Entite basique du jeux
    '''

    def __init__(self, name, description, vie, mana, degats):
        '''
        Constructor
        @param name: Nom
        @param description: Description
        @param vie: Nombre total de point vie
        @param mana: Nombre de point de mana
        @param degats: Degats
        '''
        self.name = name
        self.description = description
        self.vie = vie
        self.mana = mana
        self.degats = degats
        
    def toString(self):
        return self.name + ":[description=" + str(self.description) + ", vie=" + str(self.vie) + ", mana=" + str(self.mana) + ", degats=" + str(self.mana) + "]"
        