'''
Package pour la gestion des composants
Représentation d'un bouton à l'écran

@version: 0.1
@author: quenti77
'''
from image.Animation import Animation
from image.Sprite import Sprite


try:
    import pygame
    from random import randint
except:
    print("Import erronné")

class CardInfo(object):
    '''
    Une carte du jeu sur une scene
    '''
    
    def __init__(self, l, carte, level):
        '''
        Constructeur d'une carte affichable
        @param l: Le loader de ressource
        '''
        self.swidth = pygame.display.get_surface().get_width()
        self.sheight = pygame.display.get_surface().get_height()
        self.carte = carte
        self.name = str(self.carte.ID) + "-" + self.carte.name + "-" + str(randint(1, 1000000))
        self.loader = l
        self.type = "spell"
        self.visible = True
        self.showInfo = True
        self.select = False
        self.asyncSelect = False
        self.changeVisibility = False
        self.posX = 50
        self.posY = 50
        self.width = 75
        self.height = 105
        self.tick = 0
        self.func = None
        self.level = level
        
        self.loader.addAnimation(self.name, None, level)
        
        texts = self.loader.getFont('mainTitle')
        if len(texts) > 0:
            self.sp = Sprite(texts[0].render("" + str(self.carte.name) +  "", 1, (255, 0, 255)))
            self.animation = Animation(self.sp)
            self.animation.newPos(self.swidth / 2 - 75, self.sheight / 2 - 135, 0, 0, 0, None)
            self.loader.addAnimation('NOM_CARTE', self.animation, 6)
        
        self.updateModif(True)
    
    def setPosition(self, x, y, t = 0, func = None):
        '''
        Modifie la position de la carte
        @param x: position x
        @param y: position y
        @param t: le nombre de tick vers la nouvelle position (animation)
        @param func: Fonction de callback
        '''
        self.posX = x
        self.posY = y
        self.tick = t
        self.func = func
        self.updateModif()
    
    def setSize(self, w, h):
        '''
        Modifie la talle d'une carte 
        '''
        self.width = w
        self.height = h
        self.updateModif()
    
    def setResize(self, x, y, w, h, t = 0, func = None):
        '''
        Rassemble le setSize et le setPosition
        '''
        self.posX = x
        self.posY = y
        self.width = w
        self.height = h
        self.tick = t
        self.func = func
        self.updateModif()
    
    def setType(self, typeCard):
        '''
        Le type de la carte (servitor, spell)
        @param typeCard: type de la carte
        '''
        self.type = typeCard
        self.updateModif()
    
    def setVisible(self, visibility):
        '''
        La visibilité de la carte (retourné ou non)
        @param visibility: Boolean pour savoir si la carte est visible
        '''
        if self.visible != visibility:
            self.changeVisibility = True
            self.visible = visibility
            self.updateModif()
            
            if self.select == True:
                self.setSelect()
    
    def setSelect(self):
        '''
        Est-ce que la carte est sélectionné ?
        @param selected: Carte sélectionné ou pas
        '''
        if self.visible == True:
            self.select = not self.select
            self.updateModif()
    
    def updateModif(self, forceVisibility = False):
        '''
        On applique les modifications à l'image
        Les position, tailles, image à afficher
        '''
        imageSelect = ''
        addingSize = 0
        addingTime = self.tick
        
        if self.changeVisibility == True or forceVisibility == True:
            self.changeVisibility = False
            if self.visible == True:
                imageSelect = '../img/card/spellCard.jpg'
                # Show text on the card
                
            else:
                imageSelect = '../img/card/backSpellCard.jpg'
            
            self.loader.removeAnimation(self.name)
            self.loader.addAnimationByPath(self.name, imageSelect, level=1)
            
        if self.select != self.asyncSelect:
            self.asyncSelect = self.select
            
            if self.select:
                addingSize = 15
            
            if addingTime == 0:
                addingTime = 20
        
        anim = self.loader.getAnimation(self.name)
        if len(anim) > 0:
            anim[0].newPos(self.posX - addingSize, self.posY - addingSize, self.width + (addingSize * 2), self.height + (addingSize * 2), addingTime, self.func)
    
    def showInfoCard(self):
        if not self.showInfo:
            self.showInfo = True
            print("On montre la carte (ID:" + str(self.name) + ")")
            
            card = self.loader.getAnimation('showCard')
            if len(card) > 0:
                card[0].newPos(self.swidth / 2 - 100, self.sheight / 2 - 140, 200, 280, 8)
            
            self.loader.removeAnimation('NOM_CARTE')
            self.loader.removeAnimation('INFO_CARTE')
            
            texts = self.loader.getFont('mainTitle')
            if len(texts) > 0:
                self.sp = Sprite(texts[0].render("" + str(self.carte.name) +  "", 1, (127, 127, 255)))
                self.animation = Animation(self.sp)
                self.animation.newPos(self.swidth / 2 - 78, self.sheight / 2 - 125, self.width - 20, 25, 0, None)
                self.loader.addAnimation('NOM_CARTE', self.animation, 6)
                
                chaine = str(self.carte.cost)
                
                if self.isCarteServant(self.carte.ID):
                    chaine += "/" + str(self.carte.attack) + "/" + str(self.carte.health)
                    
                self.sp = Sprite(texts[0].render(chaine, 1, (127, 127, 255)))
                self.animation = Animation(self.sp)
                self.animation.newPos(self.swidth / 2 - 78, self.sheight / 2 - 95, self.width - 20, 25, 0, None)
                self.loader.addAnimation('INFO_CARTE', self.animation, 6)
    
    def isCarteServant(self, ID):
        '''
        Verifie si l'id correspond a une carte qui invoque un serviteur
        '''
        if int(ID) > 2000000 and int(ID) < 3000000:
            return True
        else:
            return False
    
    def hideInfoCard(self):
        if self.showInfo:
            self.showInfo = False
            print("On cache la carte (ID:" + str(self.name) + ")")
            
            card = self.loader.getAnimation('showCard')
            if len(card) > 0:
                card[0].newPos(self.swidth / 2, self.sheight / 2, 0, 0, 8)
            
            self.loader.removeAnimation('NOM_CARTE')
            self.loader.removeAnimation('INFO_CARTE')

    def mouseCheck(self, e, x, y, w, h):
        return (e.posX >= x and e.posX <= (x + w) and e.posY >= y and e.posY <= (y + h))
    
    def update(self, e, l):
        '''
        On regarde les événements sur la carte
        '''
        if not (e == None) and self.mouseCheck(e, self.posX, self.posY, self.width, self.height):
            if self.visible == True:
                self.showInfoCard()
            
            if e.button[1]:
                e.button[1] = False
                self.setSelect()
        else:
            self.hideInfoCard()
    
    def updateResize(self, w, h):
        self.swidth = w
        self.sheight = h