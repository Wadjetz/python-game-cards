'''
Created on 11 mars 2014

@author: egor
'''

from engine.Entity import Entity

class Player(Entity):
    '''
    Joueur Principale
    @param main: Les cartes utilisable par le joueur
    '''
    def __init__(self, name):
        '''
        Constructor
        '''
        
        Entity.__init__(self, name, "description", 30, 1, 5)
        self.action = True
        self.main = []
        
    def attaque(self, jouer, carte):
        jouer.degats(carte.degats)
        self.action = False

    def degats(self, degats):
        self.vie -= degats

    def display(self):
        print(self.toString())
        
    def toString(self):
        return self.name + ":[vie=" + str(self.vie) + ", mana=" + str(self.mana) + ", action=" + str(self.action) + "]"
    
    def nextTour(self, tour):
        if (tour > 10):
            self.mana = 10
        else:
            self.mana = tour
        
            
    def piocheCarte(self, terrain):
        if (isinstance(self.main, "list") == True and isinstance(terrain, "Terrain")):
            self.main.append(terrain.piocheCarte())
            print("OK !!")
        
        
        
