'''
Package pour la gestion des composants
Menu principale du jeu

@version: 0.1
@author: quenti77
'''

class Button(object):
    '''
    Un bouton cliquable
    '''
    
    def __init__(self, imageName, imageBase, imageSelect, fonction):
        self.imageName = imageName
        self.imageBase = imageBase
        self.imageSelect = imageSelect
        self.info = None
        self.callback = fonction
        self.animationOFF = False
        self.dejaFait = False
    
    def loadButton(self, posX, posY, width, height, sw, sh):
        self.info = [posX, posY, width, height, sw, sh]
    
    def mouseCheck(self, e, x, y, w, h):
        return (e.posX >= x and e.posX <= (x + w) and e.posY >= y and e.posY <= (y + h))
    
    def update(self, e, l):
        if self.animationOFF:
            if self.mouseCheck(e, (self.info[4] / 2 - self.info[2] / 2), self.info[1], self.info[2], self.info[3]):
                if e.button[1] == True:
                    e.button[1] = False
                    self.callback(self.imageName)
                    
                if self.dejaFait != True:
                    self.dejaFait = True
                    l.removeAnimation(self.imageName)
                    l.addAnimationByPath(self.imageName, self.imageSelect, (self.info[4] / 2 - self.info[2] / 2), self.info[1])
            else:
                if self.dejaFait != False:
                    self.dejaFait = False
                    l.removeAnimation(self.imageName)
                    l.addAnimationByPath(self.imageName, self.imageBase, (self.info[4] / 2 - self.info[2] / 2), self.info[1])
                
        else:
            ta = l.getAnimation(self.imageName)
            if ta[0].end[4] == 0:
                self.animationOFF = True
    
    def resizeWindow(self, l, w, h):
        
        a = l.getAnimation(self.imageName)
        if len(a) > 0:
            self.info[4] = w
            self.info[5] = h
            
            
    