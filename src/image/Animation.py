'''
Package pour la gestion des images
Animation d'un sprite

@version: 0.1
@author: quenti77
'''

class Animation(object):
    '''
    Class permettant d'animer un sprite
    '''
    
    def __init__(self, sp):
        '''
        Constructeur de la class Animation
        '''
        self.sprite = sp
        self.index = 1
        self.pos = [sp.x, sp.y, sp.w, sp.h]
        self.end = [sp.x, sp.y, sp.w, sp.h, 0]
        self.func = None
        self.callFunc = True
    
    def newPos(self, x, y, w, h, t, f = None):
        '''
        @param x: nouvelle position X
        @param y: nouvelle position Y
        @param w: nouvelle largeur
        @param h: nouvelle hauteur
        @param t: nombre de ticks
        Définit les nouvelles valeurs
        '''
        if not (f == None):
            self.func = f
            self.callFunc = False
        
        self.end[0] = x
        self.end[1] = y
        self.end[2] = w
        self.end[3] = h
        self.end[4] = t
        
        if self.end[4] <= 0:
            self.end[4] = 0
            for i in range(0,4):
                self.pos[i] = self.end[i]
    
    def setIndex(self, index):
        self.index = index
    
    def addPos(self, x, y, w, h, t, f = None):
        '''
        @param x: nouvelle position X
        @param y: nouvelle position Y
        @param w: nouvelle largeur
        @param h: nouvelle hauteur
        @param a: nouvelle angle
        @param t: nombre de ticks
        Ajoute les nouvelles valeurs
        '''
        
        if not (f == None):
            self.func = f 
            self.callFunc = False
        
        self.end[0] += x
        self.end[1] += y
        self.end[2] += w
        self.end[3] += h
        self.end[4] = t
    
    def calcul(self, start, end, tick):
        '''
        @param  start: La valeur de départ
        @param end: la valeur d'arrivée
        @param tick: le nombre de tick pour y arriver
        @return: ce qu'il faut rajouter
        Calcul sur un paramètre
        '''
        result = 0
        
        if tick == 0:
            return result
        
        if start < end:
            result = end - start
        elif start > end:
            result = start - end
            result *= -1
        
        result = (result * 1.0 / tick)
        return result
    
    def update(self, screen):
        '''
        @param screen: Permet au sprite de se poser dessus
        Update l'animation
        '''
        if self.end[4] > 0:
            for i in range(0,4):
                self.pos[i] += self.calcul(self.pos[i], self.end[i], self.end[4])
            
            self.end[4] -= 1
        elif self.callFunc == False:
            self.callFunc = True
            self.func(self)
        
        self.sprite.setPosition(self.pos[0], self.pos[1])
        self.sprite.setSize(self.pos[2], self.pos[3])
        
        self.sprite.update(screen)
