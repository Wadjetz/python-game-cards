'''
Package pour la gestion des images
Chargement des ressources, vérifications, etc.

@version: 0.1
@author: quenti77
'''

from image.Animation import Animation
from image.Sprite import Sprite

class Loader(object):
    '''
    Class générique permettant de gérer des ressources
    (Ajout, Modification, Suppression, etc.)
    '''
    
    def __init__(self):
        self.anim = []
        self.titles = []
    
    def addAnimationByPath(self, name, path):
        '''
        @param name:Le nom de l'animation
        @param path: chemin du sprite
        '''
        ts = Sprite(path)
        ta = Animation(ts)
        self.addAnimation(name, ta)
    
    def addAnimation(self, name, animation = None):
        '''
        @param name:Le nom de l'animation
        @param animation: l'animation elle-meme 
        '''
        if animation is not None:
            tempAnim = { 'name': name, 'value': animation}
            self.anim.append(tempAnim)
    
    def removeAnimation(self, name):
        '''
        @param name: Le nom de l'animation à retirer
        '''
        for item in self.anim:
            if (item['name'] == name):
                self.anim.remove(item)
    
    def getAnimation(self, name):
        '''
        @param name: Le nom de l'animation à retirer
        '''
        for item in self.anim:
            if (item['name'] == name):
                return item['value']
        
        return None
    
    def update(self, screen):
        '''
        Update all
        '''
        for animation in self.anim:
            animation['value'].update(screen)
    