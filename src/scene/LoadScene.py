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
        l.addAnimationByPath("bg", '../img/background.jpg')
        l.addAnimationByPath("arrow", "../img/arrows.png")
        
        l.addFont("mainTitle", "../img/LSANS.TTF", 15)
        
        self.counter = 0.0
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        @return: Scene à renvoyer
        '''
        self.counter += 0.1
        
        font = l.getFont("mainTitle")
        if font[0] is not None:
            l.removeAnimation("title")
            ts = Sprite(font[0].render("Compteur = " + str(self.counter), 1, (255,255,0)))
            ta = Animation(ts)
            l.addAnimation("title", ta)
        
        a = l.getAnimation('bg')
        if a is not None:
            a[0].newPos(0, 0, e.width, e.height, 0)
        
        if (e.quit):
            return None
        
        if (e.button[1]):
            a = l.getAnimation('arrow')
            
            for b in a:
                b.newPos(e.posX, e.posY, b.pos[2], b.pos[3], 20)
        
        if (e.keyboard[pygame.K_q]):
            from scene.TestScene import TestScene
            l.clearAnimation()
            newScene = TestScene(l)
            return newScene
        
        return self
        