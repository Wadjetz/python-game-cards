'''
Package pour la gestion des composants
Représentation d'un bouton à l'écran

@version: 0.1
@author: quenti77
'''

class CardInfo(object):
    '''
    Une carte du jeu sur une scene
    '''
    
    def __init__(self, l, carte):
        '''
        Constructeur d'une carte affichable
        @param l: Le loader de ressource
        '''
        self.carte = carte
        self.name = str(self.carte.ID) + "-" + self.carte.name
        self.loader = l
        self.type = "spell"
        self.visible = True
        self.select = False
        self.asyncSelect = False
        self.changeVisibility = False
        self.posX = 50
        self.posY = 50
        self.width = 50
        self.height = 70
        self.tick = 0
        
        self.loader.addAnimation(self.name, None)
        
        #TODO: Ajouter les textes
        
        self.updateModif(True)
    
    def setPosition(self, x, y, t = 0):
        '''
        Modifie la position de la carte
        @param x: position x
        @param y: position y
        @param t: le nombre de tick vers la nouvelle position (animation)
        '''
        self.posX = x
        self.posY = y
        self.tick = t
        self.updateModif()
    
    def setSize(self, w, h):
        '''
        Modifie la talle d'une carte 
        '''
        self.width = w
        self.height = h
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
            else:
                imageSelect = '../img/card/backSpellCard.jpg'
            
            self.loader.removeAnimation(self.name)
            self.loader.addAnimationByPath(self.name, imageSelect, 1)
            
        if self.select != self.asyncSelect:
            self.asyncSelect = self.select
            
            if self.select:
                addingSize = 15
            
            if addingTime == 0:
                addingTime = 20
        
        anim = self.loader.getAnimation(self.name)
        if len(anim) > 0:
            anim[0].newPos(self.posX - addingSize, self.posY - addingSize, self.width + (addingSize * 2), self.height + (addingSize * 2), addingTime)
    
    def mouseCheck(self, e, x, y, w, h):
        return (e.posX >= x and e.posX <= (x + w) and e.posY >= y and e.posY <= (y + h))
    
    def update(self, e, l):
        '''
        On regarde les événements sur la carte
        '''
        
        if self.mouseCheck(e, self.posX, self.posY, self.width, self.height):
            if e.button[1]:
                e.button[1] = False
                self.setSelect()
        
    