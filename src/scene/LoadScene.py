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
        self.__screen = pygame.display.get_surface().get_size()
        self.loader = []
        self.actual = 0
        self.file = ""
        
        for i in range(1, 10000):
            self.loader.append(i * 2)
        
        l.addAnimationByPath("bg", '../img/background.jpg')
        
        font = l.getFont("mainTitle")
        if font[0] is not None:
            l.removeAnimation("titleLoad")
            ts = Sprite(font[0].render("Loading file :" + str(self.file), 1, (255,255,0)))
            ta = Animation(ts)
            ta.newPos((self.__screen[0] / 2 - ts.image.get_size()[0]), 10, ts.image.get_size()[0], ts.image.get_size()[1], 1)
            l.addAnimation("titleLoad", ta)
        
        self.counter = 0.0
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        @return: Scene à renvoyer
        '''
        
        try:
            self.file = self.loader[self.actual]
            self.actual += 1
        except:
            self.file = "OK"
    
        a = l.getAnimation('bg')
        if a is not None:
            a[0].newPos(0, 0, e.width, e.height, 0)
            font = l.getFont("mainTitle")
            
            if font[0] is not None:
                l.removeAnimation("titleLoad")
                if (self.file == "OK"):
                    ts = Sprite(font[0].render("Loading file finished", 1, (255,255,0)))
                else:
                    ts = Sprite(font[0].render("Loading file :" + str(self.file), 1, (255,255,0)))
                ta = Animation(ts)
                ta.newPos((e.width / 2 - 100), 10, ts.image.get_size()[0], ts.image.get_size()[1], 0)
                l.addAnimation("titleLoad", ta)
        
        if (e.quit):
            return None
        
        if (e.button[1]):
            a = l.getAnimation('arrow')
            
            for b in a:
                b.newPos(e.posX, e.posY, b.pos[2], b.pos[3], 20)
        
        if (e.keyboard[pygame.K_a]):
            from scene.TestScene import TestScene
            l.clearAnimation()
            newScene = TestScene(l)
            return newScene
        
        return self
        