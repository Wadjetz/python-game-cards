'''
Package pour la gestion des scenes
Scene de chargement du jeu

@version: 0.1
@author: quenti77
'''
from image.Animation import Animation
from image.Sprite import Sprite
from scene.MainScene import MainScene

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
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        
        self.fileCheck = []
        self.counter = 0
        self.maxCounter = 0
        
        l.clearAnimation()
        
        l.addAnimationByPath('bg', '../img/background.jpg')
        self.resizeWindow(l, self.width, self.height)
        
        self.__load__()
    
    def __load__(self):
        title = 'Vérification des fichiers :'
        for i in range(123):
            i = i
            self.fileCheck.append({'title': title, 'file': 'img/background.jpg'})
            self.fileCheck.append({'title': title, 'file': 'img/solo.png'})
            self.fileCheck.append({'title': title, 'file': 'img/LSANS.TTF'})
            self.fileCheck.append({'title': title, 'file': 'save/db.txt'})
            self.fileCheck.append({'title': title, 'file': 'save/Cartes'})
        
        self.maxCounter = len(self.fileCheck)
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        @return: Scene à renvoyer
        '''
        
        if self.counter < self.maxCounter:
            texts = l.getFont('mainTitle')
            
            if len(texts) > 0:
                percent = (self.counter * 1.0 / self.maxCounter * 100)
                sprite = Sprite(texts[0].render(self.fileCheck[self.counter]['title'] + " {0:.0f}".format(percent) + " %", 1, (255, 255, 0)))
                animation = Animation(sprite)
                animation.newPos((self.width / 2 - sprite.w / 2), self.height - 50, sprite.w, sprite.h, 0)
                
                l.removeAnimation('infoTitle')
                l.addAnimation('infoTitle', animation)
            
            self.counter += 1
        else:
            nextScene = MainScene(l)
            return nextScene
        
        if (e.quit):
            return None
        
        return self
    
    def resizeWindow(self, l, w, h):
        self.width = w
        self.height = h
        
        backgrounds = l.getAnimation('bg')
        if len(backgrounds) > 0:
            backgrounds[0].newPos(0, 0, self.width, self.height, 0)