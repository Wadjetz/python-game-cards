'''
Created on 2 avr. 2014

@author: egor
'''


class Entity(object):
    '''
    Entite vivant dans le jeu
    '''
    def __init__(self, ID, name, health, attack):
        '''
        Constructor
        @param ID: id unique de la carte
        @param name: Nom
        @param health: Les points de vie
        @param attack: Degats
        '''
        self.ID = int(ID)
        self.name = name
        self.health = int(health)
        self.attack = int(attack)
        self.action = False
        
    def domage(self, domage):
        '''
        Enleve de la vie a l'entite
        '''
        self.health -= int(domage)
        
    def nextTour(self, tour):
        '''
        Tour suivant
        '''
        self.action = True
    
