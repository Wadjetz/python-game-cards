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

class MainScene(Scene):
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
        l.addAnimationByPath('solo', '../img/solo.png', self.width / 2 - 140, 100)
        l.addAnimationByPath('multi', '../img/multi.png', self.width / 2 - 140, 100)
        l.addAnimationByPath('options', '../img/option.png', self.width / 2 - 140, 100)
        l.addAnimationByPath('quitter', '../img/quitter.png', self.width / 2 - 140, 100)
        
        self.createButton(l)
        self.resizeWindow(l, self.width, self.height)
        self.ReturnScene = self
        
        texts = l.getFont('mainTitle')
            
        if len(texts) > 0:
            sprite = Sprite(texts[0].render("Menu principale :", 1, (255, 255, 0)))
            animation = Animation(sprite)
            animation.newPos((self.width / 2 - sprite.w / 2), 30, sprite.w, sprite.h, 0)
                
            l.removeAnimation('title')
            l.addAnimation('title', animation)
    
    def createButton(self, l):
        solo = l.getAnimation('solo')
        if len(solo) > 0:
            solo[0].newPos(self.width / 2 - 140, 100, 280, 50, 60)
        
        self.btnSolo = Button('solo', '../img/solo.png', '../img/solo_select.png', self.partieSolo)
        self.btnSolo.loadButton(self.width / 2 - 140, 100, 280, 50, self.width, self.height)
        
        multi = l.getAnimation('multi')
        if len(multi) > 0:
            multi[0].newPos(self.width / 2 - 140, 200, 280, 50, 60)
        
        self.btnMulti = Button('multi', '../img/multi.png', '../img/multi_select.png', self.callbackButton)
        self.btnMulti.loadButton(self.width / 2 - 140, 200, 280, 50, self.width, self.height)
        
        options = l.getAnimation('options')
        if len(options) > 0:
            options[0].newPos(self.width / 2 - 140, 300, 280, 50, 60)
        
        self.btnOptions = Button('options', '../img/option.png', '../img/option_select.png', self.callbackButton)
        self.btnOptions.loadButton(self.width / 2 - 140, 300, 280, 50, self.width, self.height)
        
        quitter = l.getAnimation('quitter')
        if len(quitter) > 0:
            quitter[0].newPos(self.width / 2 - 140, 400, 280, 50, 60)
        
        self.btnQuitter = Button('quitter', '../img/quitter.png', '../img/quitter_select.png', self.quitterCallBack)
        self.btnQuitter.loadButton(self.width / 2 - 140, 400, 280, 50, self.width, self.height)
    
    def callbackButton(self, nom):
        print('Nom : ' + nom)
    
    def quitterCallBack(self, nom):
        self.ReturnScene = None
    
    def partieSolo(self, nom):
        from scene.TypePartieScene import TypePartieScene
        self.ReturnScene = TypePartieScene(self.loader)
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        @return: Scene à renvoyer
        '''
        self.btnSolo.update(e, l)
        self.btnMulti.update(e, l)
        self.btnOptions.update(e, l)
        self.btnQuitter.update(e, l)
        
        if (e.quit):
            self.quitterCallBack()
        
        return self.ReturnScene
    
    def resizeWindow(self, l, w, h):
        self.width = w
        self.height = h
        
        backgrounds = l.getAnimation('bg')
        if len(backgrounds) > 0:
            backgrounds[0].newPos(0, 0, self.width, self.height, 0)
        
        self.btnSolo.resizeWindow(l, w, h)
        self.btnMulti.resizeWindow(l, w, h)
        self.btnOptions.resizeWindow(l, w, h)
        self.btnQuitter.resizeWindow(l, w, h)
        
        animation = l.getAnimation('title')
        if len(animation) > 0:
            animation[0].newPos((self.width / 2 - animation[0].sprite.w / 2), 30, animation[0].sprite.w, animation[0].sprite.h, 0)
