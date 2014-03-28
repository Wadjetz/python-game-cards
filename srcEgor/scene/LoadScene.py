'''
Package pour la gestion des scenes
Gestion des scene du jeu

@version: 0.1
@author: quenti77
'''
from image.Animation import Animation
from image.Sprite import Sprite

try:
    import pygame
    from scene.Scene import Scene
except:
    print("Import erronné")

class LoadScene(Scene):
    '''
    Une scene pour le chargement des données
    '''
    
    def __init__(self, l):
        '''
        Constructeur de la class LoadScene
        '''
        
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        @return: Scene à renvoyer
        '''
        
        return self
        