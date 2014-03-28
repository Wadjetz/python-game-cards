'''
Package pour la gestion du jeu
Gestion des events

@version: 0.1
@author: quenti77
'''

import pygame

from game.Event import Event
from image.Loader import Loader
from scene.LoadScene import LoadScene

class Game(object):
    '''
    Class modélisant le jeu
    '''
    
    def __init__(self):
        '''
        construction du jeu
        '''
        self.event = Event()
        self.loader = Loader()
        self.mainWindow = pygame.display.set_mode((1152, 769), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.mainScene = LoadScene(self.loader)
        
        pygame.init()
        pygame.display.set_caption("Python Game Cards")
        
        self.loader.addFont("mainTitle", "../img/LSANS.ttf", 30)
    
    def play(self):
        '''
        Démarre le jeu
        '''
        laps = 20
        next_ = pygame.time.get_ticks() + laps
        
        while (self.mainScene is not None):
            self.event.update()
            
            if (self.event.resize == True):
                self.event.resize = False
                pygame.display.set_mode((self.event.width, self.event.height), pygame.HWSURFACE | pygame.DOUBLEBUF)
                self.mainScene.resizeWindow(self.loader, self.event.width, self.event.height)
            
            self.mainScene = self.mainScene.update(self.event, self.loader)
            
            tick = pygame.time.get_ticks()
            if tick > next_:
                next_ += laps
                if self.mainScene is not None:
                    self.loader.update(self.mainWindow)
                    
                pygame.display.flip()
    