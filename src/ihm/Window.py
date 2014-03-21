'''
Created on 21 mars 2014

@author: quenti77
'''
import pygame

from pygame.constants import *
from ihm.log import Log

class MainWindow(object):
    '''
    Une fenetre du jeu
    '''

    def __init__(self):        
        '''
        Constructeur pour MainWindow
        '''
        self.window = None
        self.background = None
        self.test = None
    
    def load(self):
        from ihm.Image import Image
        
        self.window = pygame.display.set_mode((800, 600), RESIZABLE)
        
        self.background = Image("../res/background.png")
        self.background.scale(800, 600)
        self.background.rotate(0)
        
        self.test = Image("../res/test.png")
        self.test.rotate(20)
    
    def update(self, e):
        from game.Event import Event
        
        self.window.blit(self.background.asset, (0, 0))
        self.window.blit(self.test.asset, (e.posX, e.posY))
        
        pygame.display.flip()
        