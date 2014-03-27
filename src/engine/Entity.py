'''
Created on 26 mars 2014

@author: egor
'''

class Entity():
    '''
    Entite basique du jeux
    '''

    def __init__(self, ID, name, description, vie, mana, degats):
        '''
        Constructor
        @param name: Nom
        @param description: Description
        @param vie: Nombre total de point vie
        @param mana: Nombre de point de mana
        @param degats: Degats
        '''
        self.ID = ID
        self.name = name
        self.description = description
        self.vie = vie
        self.mana = mana
        self.degats = degats
        
    def attaque(self, jouer):
        '''
        L'entite attaque
        @param jouer: Le joueur a attaquer
        '''
        jouer.recevoirDegets(self.degats)
        print("J'attque" + jouer.name)
        return jouer.name + " prend " + self.degats + " degats"

    def recevoirDegets(self, degats):
        '''
        L'entite recois des degats
        @param degats: Les degats
        '''
        self.vie -= degats
        
    def toString(self):
        return str(self.ID) + "::" + self.name + " [vie=" + str(self.vie) + ", mana=" + str(self.mana) + ", degats=" + str(self.mana) + "]"
        