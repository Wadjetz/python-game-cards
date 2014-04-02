'''
Package pour la gestion des scenes
Menu principale du jeu

@version: 0.1
@author: quenti77
'''
from image.Animation import Animation
from image.Button import Button
from image.Sprite import Sprite

try:
    import pygame
    from scene.Scene import Scene
except:
    print("Import erronné")

class TypePartieScene(Scene):
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
        l.addAnimationByPath('normal', '../img/normal.png', self.width / 2 - 140, 100)
        l.addAnimationByPath('union', '../img/union.png', self.width / 2 - 140, 100)
        l.addAnimationByPath('back', '../img/back.png', self.width / 2 - 140, 100)
        
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
        normal = l.getAnimation('normal')
        if len(normal) > 0:
            normal[0].newPos(self.width / 2 - 140, 100, 280, 50, 60)
        
        self.btnNormal = Button('normal', '../img/normal.png', '../img/normal_select.png', self.callbackButton)
        self.btnNormal.loadButton(self.width / 2 - 140, 100, 280, 50, self.width, self.height)
        
        union = l.getAnimation('union')
        if len(union) > 0:
            union[0].newPos(self.width / 2 - 140, 200, 280, 50, 60)
        
        self.btnUnion = Button('union', '../img/union.png', '../img/union_select.png', self.callbackButton)
        self.btnUnion.loadButton(self.width / 2 - 140, 200, 280, 50, self.width, self.height)
        
        back = l.getAnimation('back')
        if len(back) > 0:
            back[0].newPos(self.width / 2 - 140, 300, 280, 50, 60)
        
        self.btnBack = Button('back', '../img/back.png', '../img/back_select.png', self.retourCallBack)
        self.btnBack.loadButton(self.width / 2 - 140, 300, 280, 50, self.width, self.height)
    
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
        self.btnNormal.update(e, l)
        self.btnUnion.update(e, l)
        self.btnBack.update(e, l)
        
        if (e.quit):
            self.quitterCallBack()
        
        return self.ReturnScene
    
    def resizeWindow(self, l, w, h):
        self.width = w
        self.height = h
        
        backgrounds = l.getAnimation('bg')
        if len(backgrounds) > 0:
            backgrounds[0].newPos(0, 0, self.width, self.height, 0)
        
        self.btnNormal.resizeWindow(l, w, h)
        self.btnUnion.resizeWindow(l, w, h)
        self.btnBack.resizeWindow(l, w, h)
        
        animation = l.getAnimation('title')
        if len(animation) > 0:
            animation[0].newPos((self.width / 2 - animation[0].sprite.w / 2), 30, animation[0].sprite.w, animation[0].sprite.h, 0)
