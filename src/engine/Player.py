'''
Created on 11 mars 2014

@author: egor
'''

from engine.Entity import Entity

class Player(Entity):
    '''
    classdocs
    '''

    def __init__(self, name, name, description, vie, mana, degats):
        '''
        Constructor
        '''
        
        Entity.__init__(self, name, description, vie, mana, degats)
        
        self.action = True
        self.vie = 30
        self.mana = 1
        
    def attaque(self, jouer, carte):
        jouer.degats(carte.degats)
        self.action = False

    def degats(self, degats):
        self.vie -= degats

    def display(self):
        print(self.toString())
        
    def toString(self):
        return self.name + ":[vie=" + str(self.vie) + ", mana=" + str(self.mana) + ", action=" + str(self.action) + "]"
