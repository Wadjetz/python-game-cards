'''
Package pour la gestion des scenes
Menu principale du jeu

@version: 0.1
@author: quenti77
'''
from engine.Deck import Pioche, Deck
from engine.Player import Player
from image.Animation import Animation
from image.CardInfo import CardInfo
from image.Sprite import Sprite


#from image.Button import Button
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
        self.action = 0
        
        self.tour = 1
        self.pioche = Pioche()
        deckPlayer1 = Deck("deck1", self.pioche.getDecks("deck1"))
        deckPlayer2 = Deck("deck2", self.pioche.getDecks("deck2"))
        
        self.player1 = Player(1, "Egor", deckPlayer1)
        self.player2 = Player(2, "Quentin", deckPlayer2)
        
        l.clearAnimation()
        l.addAnimationByPath('bg', '../img/background.jpg')
        
        self.cardTest = CardInfo(l, self.player1.deck.getCarte())
        
        self.resizeWindow(l, self.width, self.height)
        self.ReturnScene = self
        
        self.changeText(l, "INFO")
    
    def changeText(self, l, message):
        texts = l.getFont('mainTitle')
            
        if len(texts) > 0:
            sprite = Sprite(texts[0].render(message, 1, (255, 255, 0)))
            animation = Animation(sprite)
            animation.newPos((self.width / 2 - sprite.w / 2), (self.height / 2 - sprite.h / 2), sprite.w, sprite.h, 0)
                
            l.removeAnimation('info')
            l.addAnimation('info', animation)
    
    def quitterCallBack(self, nom):
        self.ReturnScene = None
    
    def retourCallBack(self, nom):
        from scene.MainScene import MainScene
        self.ReturnScene = MainScene(self.loader)
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        @return: Scene à renvoyer
        '''
        
        if self.action == 0:
            #Get name and random begin
            print("Choix du nom ...")
            print("Choix du joueur commençant ...")
            print("Joueur 1 à vous !")
            self.changeText(l, "Joueur 1 à vous !")
            self.action = 1
        elif self.action == 1:
            # Joueur 1 sur joueur 2
            pass
        elif self.action == 2:
            # Joueur 2 sur joueur 1
            pass
        elif self.action == 3:
            # reset
            pass
        elif self.action == 4:
            # Fin de partie
            pass
        elif self.action == 5:
            self.retourCallBack('')
            
        if e.keyboard[pygame.K_F1]:
            e.keyboard[pygame.K_F1] = False
            self.cardTest.setVisible(not self.cardTest.visible)
            
        self.cardTest.update(e, l)
            
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
