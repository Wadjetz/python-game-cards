'''
Created on 11 mars 2014

@author: egor
'''
from engine.Entity import Entity

class Serviteur(Entity):
    '''
    Serviteur
    @param parent: Le maitre du serviteur
    @param autres: Voir la classe mere : Entity
    '''

    def __init__(self, ID, name, description, vie, mana, degats, parent):
        '''
        Constructor
        '''
        Entity.__init__(self, ID, name, description, vie, mana, degats)
        self.parent = parent
        
    def attaque(self, jouer):
        '''
        L'entite attaque si c'est un serviteur il s'inflige mutuellement les degats
        @param jouer: Le joueur a attaquer
        '''
        if self.action == True:
            if (isinstance(self.main, Serviteur) == True):
                jouer.recevoirDegets(self.degats)
                self.recevoirDegets(jouer.degats)
                self.action = False
            else:
                jouer.recevoirDegets(self.degats)
                self.action = False
        else:
            print("Tu peux pas attaquer")
            
    def toString(self):
        return Entity.toString(self)
