'''
Package pour la gestion des images
Chargement des ressources, vérifications, etc.

@version: 0.1
@author: quenti77
'''
import pygame

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
    
    def addAnimationByPath(self, name, path, x = 0, y = 0):
        '''
        @param name:Le nom de l'animation
        @param path: chemin du sprite
        '''
        ts = Sprite(path)
        ts.setPosition(x, y)
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
            
    def addFont(self, name, title, size):
        '''
        @param name: Le nom dans le tableau
        @param title: Le nom de la font
        @param size: la taille de la font
        Ajoute une font a la liste des fonts
        '''
        tempFont = { 'name': name, 'value': pygame.font.Font(title, size)}
        self.titles.append(tempFont)
    
    def removeAnimation(self, name):
        '''
        @param name: Le nom de l'animation à retirer
        '''
        for item in self.anim:
            if (item['name'] == name):
                self.anim.remove(item)
    
    def removeFont(self, name):
        '''
        @param name: Le nom de la font à retirer
        '''
        for item in self.titles:
            if (item['name'] == name):
                self.titles.remove(item)
    
    def clearAnimation(self):
        '''
        Efface toute les animations du tableau
        '''
        self.anim.clear()
        
    def clearFont(self):
        '''
        Efface toute les fonts du tableau
        '''
        self.titles.clear()
    
    def getAnimation(self, name):
        '''
        @param name: Le nom de l'animation à récupérer
        '''
        result = []
        
        for item in self.anim:
            if (item['name'] == name):
                result.append(item['value'])
        
        return result
    
    def getFont(self, name):
        '''
        @param name: Le nom de la font à récupérer
        '''
        result = []
        
        for item in self.titles:
            if (item['name'] == name):
                result.append(item['value'])
        
        return result
    
    def update(self, screen):
        '''
        Update all
        '''
        for animation in self.anim:
            animation['value'].update(screen)
    