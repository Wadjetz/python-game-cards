'''
Package pour la gestion des images
Création affichage, transformation, animation etc.

@version: 0.1
@author: quenti77
'''

import pygame

class Sprite(object):
    '''
    Class modélisant une image
    '''
    
    def __init__(self, path):
        '''
        Constructeur de la class Sprite
        '''
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.a = 0
        
        self.path = None
        self.image = None
        self.loadSprite(path)
    
    def loadSprite(self, path):
        self.path = path
        self.image = pygame.image.load(path)
        
        if self.image.get_alpha() is None:
            self.image = self.image.convert()
        else:
            self.image = self.image.convert_alpha()
        
        taille = pygame.Surface.get_size(self.image)
        self.w = taille[0]
        self.h = taille[1]
        print(taille)
    
    def setPosition(self, x, y):
        self.x = x
        self.y = y
    
    def setSize(self, w, h):
        self.w = int(w)
        self.h = int(h)
        
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
    
    def setAngle(self, angle):
        self.a = angle
        
        self.image = pygame.transform.rotate(self.image, angle)
    
    def update(self, screen):
        screen.blit(self.image, (self.x, self.y))