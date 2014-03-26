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
        @param path: le chemin vers le fichier
        Constructeur de la class Sprite
        '''
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        
        self.path = None
        self.image = None
        self.loadSprite(path)
    
    def loadSprite(self, path):
        '''
        @param path: le chemin vers le fichier
        Charge l'image
        '''
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
        '''
        @param x: position X de l'image
        @param y: position Y de l'image
        Définit les positions de l'image 
        '''
        self.x = x
        self.y = y
    
    def setSize(self, w, h):
        '''
        @param w: largeur de l'image
        @param h: hauteur de l'image
        Définit la taille de l'image 
        '''
        self.w = int(w)
        self.h = int(h)
        
        self.image = pygame.transform.smoothscale(self.image, (self.w, self.h))
    
    def update(self, screen):
        '''
        @param screen: Update a sprite on the screen
        '''
        screen.blit(self.image, (self.x, self.y))