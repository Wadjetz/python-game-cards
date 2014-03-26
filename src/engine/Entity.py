'''
Created on 26 mars 2014

@author: egor
'''

class Entity():
    '''
    Entité basique du jeux
    '''


    def __init__(self, name, description, vie, mana, degats):
        '''
        Constructor
        '''
        self.name = name
        self.description = description
        self.vie = vie
        self.mana = mana
        self.degats = degats
        
        