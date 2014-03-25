'''
Package pour la gestion des scenes
Gestion des scene du jeu

@version: 0.1
@author: quenti77
'''

try:
    import pygame
    from scene.Scene import Scene
    from image.Animation import Animation
    from image.Sprite import Sprite
except:
    print("Import erronné")

class TestScene(Scene):
    '''
    Une scene de test
    '''
    
    def __init__(self, l):
        '''
        Constructeur
        '''
        l.addAnimationByPath('bg', '../img/background.png')
        l.addAnimationByPath('perso', '../img/test.png')
        
        a = l.getAnimation('bg')
        if a is not None:
            a.newPos(0, 0, 800, 600, 0, 0)
    
    def update(self, e, l):
        if (e.quit):
            return None
        
        if (e.keyboard[pygame.K_TAB]):
            a = l.getAnimation('perso')
            a.newPos(e.posX, e.posY, a.pos[2], a.pos[3], 0, 20)
        
        return self
