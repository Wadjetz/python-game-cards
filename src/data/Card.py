'''
Created on 14 mars 2014

@author: quenti77
'''
from ihm.log import Log

class Card(object):
    '''
    Une carte du jeu (ou quelle soit dans le jeu)
    '''

    def __init__(self):
        '''
        Constructeur
        '''
        self.name = ""
        self.desc = ""
        self.type = ""
        self.mode = 0
        self.level = 1
        self.attack = 0
        self.life = 1
        self.shield = 0
        self.cost = 1
    
    