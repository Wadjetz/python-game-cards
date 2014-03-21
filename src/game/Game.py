'''
Created on 14 mars 2014

@author: quenti77
'''
import pygame

class Game(object):
    '''
    Il s'agit de la classe gérant les bases du jeu
    '''
    from ihm.log import Log
    
    logger = Log()

    def __init__(self):
        '''
        Constructeur
        '''
        from data.Deck import Deck
        from ihm.Window import MainWindow
        from game.Event import Event
        
        pygame.init()
        
        self.globalDeck = Deck()
        self.window = MainWindow()
        self.event = Event()
        self.clock = pygame.time.Clock()
        
        self.globalDeck.load("../save/db.txt")
        
        self.loadGame()
    
    def loadGame(self):
        self.window.load()
        pygame.display.set_caption("PythonGameCards")
        
    def play(self):
        while (not self.event.quit):
            self.event.update()
            
            self.window.update(self.event)
            self.clock.tick(60)