'''
Package pour la gestion des scenes
Gestion des scene du jeu

@version: 0.1
@author: quenti77
'''

try:
    from scene.Scene import Scene
except:
    print("Import erronné")

class TestScene(Scene):
    '''
    Une scene de test
    '''
    
    def __init__(self, l):
        '''
        Constructeur
        '''
        l.addAnimationByPath('bg', '../img/background.png')
        l.addAnimationByPath('perso', '../img/test.png')
        
        a = l.getAnimation('bg')
        if a is not None:
            a[0].newPos(0, 0, 800, 600, 0)
    
    def update(self, e, l):
        a = l.getAnimation('bg')
        if a is not None:
            a[0].newPos(0, 0, e.width, e.height, 0)
        
        if (e.quit):
            return None
        
        if (e.button[1]):
            a = l.getAnimation('perso')
            
            for b in a:
                b.newPos(e.posX, e.posY, b.pos[2], b.pos[3], 30)
        elif (e.button[3]):
            e.button[3] = False
            l.addAnimationByPath('perso', '../img/test.png', e.posX, e.posY)
        
        return self
