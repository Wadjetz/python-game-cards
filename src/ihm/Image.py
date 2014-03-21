'''
Created on 21 mars 2014

@author: quenti77
'''
import pygame

from ihm.log import Log

class Image(object):
    '''
    Une image avec des traitements possibles
    '''

    def __init__(self, path):
        '''
        Constructeur
        '''
        self.asset = pygame.image.load(path).convert_alpha()
    
    def scale(self, width, height):
        pygame.transform.scale(self.asset, (width, height))
    
    def rotate(self, angle):
        pygame.transform.rotate(self.asset, angle)
