'''
Package pour la gestion des scenes
Gestion des scene du jeu

@version: 0.1
@author: quenti77
'''

try:
    import pygame
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
        l.addAnimationByPath('bg', '../img/background.jpg')
        l.addAnimationByPath('perso', '../img/test.png')
    
    def update(self, e, l):
        '''
        @param e: le gestionnaire d'événement
        @param l: le gestionnaire d'image
        '''
        a = l.getAnimation('bg')
        if a is not None:
            a[0].newPos(0, 0, e.width, e.height, 0)
        
        if (e.quit):
            return None
        
        if (e.button[1]):
            a = l.getAnimation('perso')
            
            for b in a:
                b.newPos(e.posX, e.posY, b.pos[2], b.pos[3], 20)
        elif (e.button[3]):
            e.button[3] = False
            l.addAnimationByPath('perso', '../img/test.png', e.posX, e.posY)
        
        if (e.keyboard[pygame.K_a]):
            from scene.LoadScene import LoadScene
            l.clearAnimation()
            newScene = LoadScene(l)
            return newScene
        
        return self
