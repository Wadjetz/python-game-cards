'''
Created on 11 mars 2014

@author: egor
'''
from engine.Pioche import Pioche
from engine.Player import Player
from engine.Serviteur import Serviteur


class Terrain:
    '''
    Terrain du jeux
    '''

    def __init__(self, namePlayer1, namePlayer2):
        '''
        Constructor
        '''
        self.tour = 1
        self.pioche = Pioche()
        self.player1 = Player(1, namePlayer1)
        self.player2 = Player(2, namePlayer2)
        self.serviteursPlayer1 = []
        self.serviteursPlayer2 = []
        
        for i in range(4):
            self.player1.piocheCarte(self)
            self.player2.piocheCarte(self)
        
    
    def nextTour(self):
        '''
        Fait passer le tour suivant
        '''
        self.tour = self.tour + 1
        
    
    def piocheCarte(self):
        '''
        Sert a rien pour l'instant
        '''
        return self.pioche.getCarte();
    
    def gameLoop(self):
        '''
        Boucle du jeux
        '''
        stop = False

        while stop == False:
            print(self.toString())
            self.playerAction(self.player1, self.player2, self.serviteursPlayer1)
            self.playerAction(self.player2, self.player1 ,self.serviteursPlayer2)
            
    def playerAction(self, player, playerTarget, playerServiteur):
        '''
        Action du joueur
        @param player: Joueur qui jou
        @param playerTarget: Joueur adverse
        @param playerServiteurparam: Les serviteurs du joueur qui jou
        '''
        ID_carte = input(player.name + ": Attaque entrer l'Id de la carte a utiliser")
        res = player.useCarte(player.getCarte(ID_carte), playerTarget)
        if isinstance(res, Serviteur) == True:
            playerServiteur.append(res)
        else:
            print(res)
        
    def toString(self):
        txt = "TOUR=" + str(self.tour) + "\n"
        txt += self.player1.toString()
        txt += "Les Serviteur de " + self.player1.name + "\n"
        for i in self.serviteursPlayer1:
            txt += i.toString() + "\n"
        txt += "\n================================\n"
        txt += self.player2.toString()
        txt += "Les Serviteur de " + self.player2.name + "\n"
        for i in self.serviteursPlayer2:
            txt += i.toString() + "\n"
        return txt