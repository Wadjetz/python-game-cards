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
        self.levelMax = 0
    
    def addAnimationByPath(self, name, path, x = 0, y = 0, level = 0):
        '''
        @param name:Le nom de l'animation
        @param path: chemin du sprite
        '''
        ts = Sprite(path)
        ts.setPosition(x, y)
        ta = Animation(ts)
        self.addAnimation(name, ta, level)
    
    def addAnimation(self, name, animation = None, level = 0):
        '''
        @param name:Le nom de l'animation
        @param animation: l'animation elle-meme 
        '''
        if self.levelMax < level:
            self.levelMax = level
        
        if animation is not None:
            tempAnim = { 'name': name, 'value': animation, 'level': level}
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
        self.levelMax = 0
        for item in self.anim:
            if (item['name'] == name):
                self.anim.remove(item)
            else:
                if item['level'] > self.levelMax:
                    self.levelMax = item['level']
    
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
        self.levelMax = 0
        
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
        for i in range(0, self.levelMax + 1):
            for animation in self.anim:
                if animation['level'] == i:
                    animation['value'].update(screen)
    