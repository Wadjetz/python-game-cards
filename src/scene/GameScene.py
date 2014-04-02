'''
Package pour la gestion des scenes
Menu principale du jeu

@version: 0.1
@author: quenti77
'''
from image.Animation import Animation
#from image.Button import Button
from image.Sprite import Sprite

try:
    import pygame
    from scene.Scene import Scene
except:
    print("Import erronné")

class GameScene(Scene):
    '''
    Une scene pour le chargement des données
    '''
    
    def __init__(self, l):
        '''
        Constructeur de la class LoadScene
        '''
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.loader = l
        
        l.clearAnimation()
        
        l.addAnimationByPath('bg', '../img/background.jpg')
        
        self.createButton(l)
        self.resizeWindow(l, self.width, self.height)
        self.ReturnScene = self
        
        texts = l.getFont('mainTitle')
            
        if len(texts) > 0:
            sprite = Sprite(texts[0].render("Partie solo :", 1, (255, 255, 0)))
            animation = Animation(sprite)
            animation.newPos((self.width / 2 - sprite.w / 2), 30, sprite.w, sprite.h, 0)
                
            l.removeAnimation('title')
            l.addAnimation('title', animation)
    
    def createButton(self, l):
        pass
    
    def callbackButton(self, nom):
        print('Nom : ' + nom)
    
    def retourCallBack(self, nom):
        from scene.MainScene import MainScene
        self.ReturnScene = MainScene(self.loader)
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        @return: Scene à renvoyer
        '''
        
        
        if (e.quit):
            self.quitterCallBack('')
        
        return self.ReturnScene
    
    def resizeWindow(self, l, w, h):
        self.width = w
        self.height = h
        
        backgrounds = l.getAnimation('bg')
        if len(backgrounds) > 0:
            backgrounds[0].newPos(0, 0, self.width, self.height, 0)
        
        animation = l.getAnimation('title')
        if len(animation) > 0:
            animation[0].newPos((self.width / 2 - animation[0].sprite.w / 2), 30, animation[0].sprite.w, animation[0].sprite.h, 0)
