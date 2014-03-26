'''
Created on 11 mars 2014

@author: egor
'''

class Player(object):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.action = True
        self.name = name
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
