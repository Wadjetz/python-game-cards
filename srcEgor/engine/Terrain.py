'''
Created on 11 mars 2014

@author: egor
'''

class Terrain(object):
    '''
    classdocs
    '''
    
    serviteursPlayer1 = []
    serviteursPlayer2 = []

    def __init__(self, pioche, player1, player2):
        '''
        Constructor
        '''
        self.tour = 1
        self.pioche = pioche
        self.player1 = player1
        self.player2 = player2
    
    def nextTour(self):
        self.tour = self.tour + 1
        
        print()
    
    
    def display(self):
        print(self.display())
        
    def toString(self):
        txt = "TOUR=" + str(self.tour)
        return txt
    
    def piocheCarte(self):
        carte = self.pioche.getCarte();
        return carte
        