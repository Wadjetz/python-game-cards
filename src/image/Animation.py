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
        self.sprite = sp
        self.pos = [sp.x, sp.y, sp.w, sp.h, sp.a]
        self.end = [sp.x, sp.y, sp.w, sp.h, sp.a, 0]
    
    def newPos(self, x, y, w, h, a, t):
        self.end[0] = x
        self.end[1] = y
        self.end[2] = w
        self.end[3] = h
        self.end[4] = a
        self.end[5] = t
        
        if self.end[5] <= 0:
            self.end[5] = 0
            for i in range(0,4):
                self.pos[i] = self.end[i]
            
    
    def addPos(self, x, y, w, h, a, t):
        self.end[0] += x
        self.end[1] += y
        self.end[2] += w
        self.end[3] += h
        self.end[4] += a
        self.end[5] = t
    
    def calcul(self, start, end, tick):
        result = 0
        
        if start < end:
            result = end - start
        elif start > end:
            result = start - end
            result *= -1
        
        result = (result * 1.0 / tick)
        return result
    
    def update(self, screen):
        if self.end[5] > 0:
            for i in range(0,4):
                self.pos[i] += self.calcul(self.pos[i], self.end[i], self.end[5])
            
            self.end[5] -= 1
        
        self.sprite.setPosition(self.pos[0], self.pos[1])
        self.sprite.setSize(self.pos[2], self.pos[3])
        self.sprite.setAngle(self.pos[4])
        
        self.sprite.update(screen)