'''
Package pour la gestion des scenes
Menu principale du jeu

@version: 0.1
@author: quenti77
'''
from engine.Deck import Pioche, Deck
from engine.Player import Player
from image.Animation import Animation
from image.Button import Button
from image.CardInfo import CardInfo
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
        self.action = 0
        self.actionCallBack = False
        
        self.nt = False
        self.tour = 1
        self.pioche = Pioche()
        deckPlayer1 = Deck("deck1", self.pioche.getDecks("deck1"))
        deckPlayer2 = Deck("deck2", self.pioche.getDecks("deck2"))
        
        self.player1 = Player(1, "Egor", deckPlayer1)
        self.player2 = Player(2, "Quentin", deckPlayer2)
        
        self.lastAnimCard = None
        
        l.clearAnimation()
        l.addAnimationByPath('bg', '../img/background.jpg')
        l.addAnimationByPath('showCard', '../img/card/spellCard.jpg', self.width / 2 - 75, self.height / 2 - 105, level=4)
        l.addAnimationByPath('pioche1', '../img/card/backSpellCard.jpg', level=1)
        l.addAnimationByPath('pioche2', '../img/card/backSpellCard.jpg', level=1)
        l.addAnimationByPath('passerTourJoueur', '../img/passer.png', self.width / 2 - 140, self.height / 2 - 50, level=1)
        
        self.btnPasser = Button('passerTourJoueur', '../img/passer.png', '../img/passer_select.png', self.partieSolo)
        self.btnPasser.loadButton(self.width / 2 - 140, self.height / 2 - 50, 280, 50, self.width, self.height)
        
        selection = l.getAnimation('pioche1')
        if len(selection) > 0:
            selection[0].newPos(self.width - 200, self.height / 2 - 105 - 110, 75, 105, 0, None)
        
        selection = l.getAnimation('pioche2')
        if len(selection) > 0:
            selection[0].newPos(self.width - 200, self.height / 2 + 105, 75, 105, 0, None)
        
        self.levelMaxPlayer = 3
        self.levelMaxEnemy = 3
        
        self.cardPlayer = []
        for i in range(5, 8):
            self.cardPlayer.append(CardInfo(l, self.player1.deck.getCarte(), i))
        
        self.cardEnemy = []
        for i in range(5, 8):
            self.cardEnemy.append(CardInfo(l, self.player2.deck.getCarte(), i))
        
        self.resizeWindow(l, self.width, self.height)
        self.ReturnScene = self
        
        self.changeText(l, "INFO")
    
    def asyncAnimDeckPlayerFinal(self, anim):
        if not (self.lastAnimCard == None):
            self.actionCallBack = False
            self.lastAnimCard = None
    
    def asyncAnimDeckPlayer(self, anim):
        if not (self.lastAnimCard == None):
            self.lastAnimCard.setResize(self.width - 5 - (80 * len(self.cardPlayer)), self.height - 115, 75, 105, 40, self.asyncAnimDeckPlayerFinal)
    
    def animDeckPlayer(self):
        self.levelMaxPlayer += 1
        
        card = CardInfo(self.loader, self.player1.deck.getCarte(), self.levelMaxPlayer)
        card.setResize(self.width - 163 , self.height / 2 + 152, 0, 0, 0, None)
        card.setResize(self.width - 200, self.height / 2 + 105, 75, 105, 20, self.asyncAnimDeckPlayer)
        
        self.cardPlayer.append(card)
        self.lastAnimCard = card
        
    def asyncAnimDeckEnemyFinal(self, anim):
        if not (self.lastAnimCard == None):
            self.actionCallBack = False
            self.lastAnimCard = None
    
    def asyncAnimDeckEnemy(self, anim):
        if not (self.lastAnimCard == None):
            self.lastAnimCard.setResize(-70 + (80 * len(self.cardPlayer)), 10, 75, 105, 40, self.asyncAnimDeckEnemyFinal)
    
    def animDeckEnemy(self):
        self.levelMaxPlayer += 1
        
        card = CardInfo(self.loader, self.player2.deck.getCarte(), self.levelMaxPlayer)
        card.setResize(self.width - 163 , self.height / 2 - 53 - 110, 0, 0, 0, None)
        card.setResize(self.width - 200, self.height / 2 - 105 - 110, 75, 105, 20, self.asyncAnimDeckEnemy)
        
        self.cardEnemy.append(card)
        self.lastAnimCard = card
    
    def asyncChangeText(self, anim):
        anim.newPos((self.width / 2), (self.height / 2), 0, 0, 50, None)
        self.actionCallBack = False
    
    def changeText(self, l, message):
        texts = l.getFont('mainTitle')
            
        if len(texts) > 0:
            sprite = Sprite(texts[0].render(message, 1, (255, 255, 0)))
            animation = Animation(sprite)
            animation.newPos((self.width / 2 - sprite.w / 2), (self.height / 2 - sprite.h / 2) + 60, sprite.w, sprite.h, 0)
            animation.newPos((self.width / 2 - sprite.w / 2), (self.height / 2 - sprite.h / 2) + 60, sprite.w, sprite.h, 50, self.asyncChangeText)
                
            l.removeAnimation('info')
            l.addAnimation('info', animation)
    
    def partieSolo(self, e):
        self.nt = True
          
    def statusText(self, l):
        texts = l.getFont('mainTitle')
        
        # PLayer 1 ( Down )
        if len(texts) > 0:
            sprite = Sprite(texts[0].render("VIE: " + str(self.player1.health) +  "/30", 1, (255, 255, 0)))
            spriteBis = Sprite(texts[0].render("MANA: " + str(self.player1.mana) +  "/10", 1, (255, 255, 0)))
            spriteTer = Sprite(texts[0].render("" + str(self.player1.name) +  "", 1, (255, 255, 0)))
            
            animation = Animation(sprite)
            animationBis = Animation(spriteBis)
            animationTer = Animation(spriteTer)
            
            animation.newPos(self.width - (sprite.w / 2) - 10, (self.height / 2 - sprite.h / 2) - 10 - (sprite.h / 2), sprite.w / 2, sprite.h / 2, 0)
            animationBis.newPos(self.width - (sprite.w / 2) - 10, (self.height / 2 - sprite.h / 2), sprite.w / 2, sprite.h / 2, 0)
            animationTer.newPos(self.width - (sprite.w / 2) - 10, (self.height / 2 - sprite.h / 2) - (10 - (sprite.h / 2) * 2), sprite.w / 2, sprite.h / 2, 0)
            
            l.removeAnimation('infoVieP1')
            l.addAnimation('infoVieP1', animation, level=5)
            
            l.removeAnimation('infoManaP1')
            l.addAnimation('infoManaP1', animationBis, level=5)
            
            l.removeAnimation('infoNameP1')
            l.addAnimation('infoNameP1', animationTer, level=5)
        
        # PLayer 1 ( UP )
        if len(texts) > 0:
            sprite = Sprite(texts[0].render("VIE: " + str(self.player2.health) +  "/30", 1, (255, 255, 0)))
            spriteBis = Sprite(texts[0].render("MANA: " + str(self.player2.mana) +  "/10", 1, (255, 255, 0)))
            spriteTer = Sprite(texts[0].render("" + str(self.player2.name) +  "", 1, (255, 255, 0)))
            
            animation = Animation(sprite)
            animationBis = Animation(spriteBis)
            animationTer = Animation(spriteTer)
            
            animation.newPos(10, (self.height / 2 - sprite.h / 2) - 10 - (sprite.h / 2), sprite.w / 2, sprite.h / 2, 0)
            animationBis.newPos(10, (self.height / 2 - sprite.h / 2), sprite.w / 2, sprite.h / 2, 0)
            animationTer.newPos(10, (self.height / 2 - sprite.h / 2) - (10 - (sprite.h / 2) * 2), sprite.w / 2, sprite.h / 2, 0)
            
            l.removeAnimation('infoVieP2')
            l.addAnimation('infoVieP2', animation, level=5)
            
            l.removeAnimation('infoManaP2')
            l.addAnimation('infoManaP2', animationBis, level=5)
            
            l.removeAnimation('infoNameP2')
            l.addAnimation('infoNameP2', animationTer, level=5)
        
        selection = l.getAnimation('pioche1')
        if len(selection) > 0:
            selection[0].newPos(self.width - 200, self.height / 2 - 105 - 110, 75, 105, 0, None)
        
        selection = l.getAnimation('pioche2')
        if len(selection) > 0:
            selection[0].newPos(self.width - 200, self.height / 2 + 105, 75, 105, 0, None)
    
    def quitterCallBack(self, nom):
        self.ReturnScene = None
    
    def retourCallBack(self, nom):
        from scene.MainScene import MainScene
        self.ReturnScene = MainScene(self.loader)
    
    def updateMain(self, e, l):
        x = 10
        y = 10
        for cardUpdateEnemy in self.cardEnemy:
            if self.lastAnimCard != cardUpdateEnemy:
                cardUpdateEnemy.update(e, l)
                cardUpdateEnemy.updateResize(self.width, self.height)
                cardUpdateEnemy.setPosition(x, y, 0)
                x += cardUpdateEnemy.width + 5
        
        x = self.width - 85
        y = self.height - 115
        for cardUpdatePlayer in self.cardPlayer:
            if self.lastAnimCard != cardUpdatePlayer:
                cardUpdatePlayer.update(e, l)
                cardUpdatePlayer.updateResize(self.width, self.height)
                cardUpdatePlayer.setPosition(x, y, 0)
                x -= cardUpdatePlayer.width + 5
        
        self.statusText(l)
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        @return: Scene à renvoyer
        '''
        self.btnPasser.update(e, l)
        
        if (e.keyboard[pygame.K_ESCAPE]):
            e.keyboard[pygame.K_ESCAPE] = False
            self.retourCallBack('')
            self.loader.clearFont()
        
        if self.action == 0:
            #Get name and random begin
            print("Choix du nom ...")
            print("Choix du joueur commençant ...")
            self.changeText(l, "" + self.player1.name + " à vous !")
            self.actionCallBack = True
            self.action = 1
        elif self.action == 1:
            if self.actionCallBack == False:
                self.animDeckPlayer()
                self.action = 2
                self.actionCallBack = True
        elif self.action == 2:
            if self.actionCallBack == False:
                self.action = 10
                
        elif self.action == 10:
            # Joueur 1 sur joueur 2
            if e.keyboard[pygame.K_v] or self.nt:
                self.nt = False
                e.keyboard[pygame.K_v] = False
                self.changeText(l, "" + self.player2.name + " à vous !")
                self.action = 11
                self.actionCallBack = True
        elif self.action == 11:
            if self.actionCallBack == False:
                self.animDeckEnemy()
                self.action = 12
                self.actionCallBack = True
        elif self.action == 12:
            if self.actionCallBack == False:
                self.action = 20
                
        elif self.action == 20:
            # Joueur 2 sur joueur 1
            if e.keyboard[pygame.K_v] or self.nt:
                self.nt = False
                e.keyboard[pygame.K_v] = False
                self.changeText(l, "" + self.player1.name + " à vous !")
                self.actionCallBack = True
                self.action = 30
        elif self.action == 30:
            # reset
            
            self.tour += 1
            print("Tour passé : " + str(self.tour))
            self.player1.nextTour(self.tour)
            self.player2.nextTour(self.tour)
            
            self.changeText(l, "" + self.player1.name + " à vous !")
            self.actionCallBack = True
            self.action = 1
        elif self.action == 40:
            # Fin de partie
            pass
        elif self.action == 50:
            self.retourCallBack('')
            
        self.updateMain(e, l)
            
        if (e.quit):
            e.quit = True
            self.retourCallBack('')
            self.loader.clearFont()
        
        return self.ReturnScene
    
    def resizeWindow(self, l, w, h):
        self.width = w
        self.height = h
        
        backgrounds = l.getAnimation('bg')
        if len(backgrounds) > 0:
            backgrounds[0].newPos(0, 0, self.width, self.height, 0)
        
        self.btnPasser.resizeWindow(l, w, h)
        
        animation = l.getAnimation('title')
        if len(animation) > 0:
            animation[0].newPos((self.width / 2 - animation[0].sprite.w / 2), 30, animation[0].sprite.w, animation[0].sprite.h, 0)
        
        self.updateMain(None, l)