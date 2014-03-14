'''
Created on 14 mars 2014

@author: quenti77
'''
import pygame

from ihm.log import Log


class Game(object):
    '''
    Il s'agit de la classe gérant les bases du jeu
    '''
    
    logger = Log()

    def __init__(self):
        '''
        Constructor
        '''
        pygame.init()