# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''
from engine.Entity import Entity
from engine.Pioche import Pioche
from engine.Player import Player


class Terrain:
    '''
    Terrain du jeux
    '''

    def __init__(self, pioche, player1, player2):
    def __init__(self, namePlayer1, namePlayer2):
        '''
        Constructor
        '''
        self.tour = 1
        self.pioche = Pioche()
        self.player1 = Player(1, namePlayer1)
        self.player2 = Player(2, namePlayer2)
        
        for i in range(4):
            self.player1.piocheCarte(self)
            self.player2.piocheCarte(self)
        
    
    def nextTour(self):
        self.tour = self.tour + 1
        
        print()
    
    
    def inputAction(self, message):
        '''
        Demande de saisie utilisateur
        @param message: prompt
        @return: int 
        '''
        ID = -1
        try:
            ID = input(message + "[int]#")
            ID = int(ID)
        except EOFError:
            print("Saisie incorrecte " + str(EOFError.message))
            ID = -1
        except SyntaxError:
            print("Saisie incorrecte " + str(SyntaxError.message))
            ID = -1
        except NameError:
            print("Saisie incorrecte " + str(NameError.message))
            ID = -1
        except ValueError:
            print("Saisie incorrecte " + str(ValueError.message))
            ID = -1
        return ID
        
    def toString(self):
        txt = "TOUR=" + str(self.tour)
        return txt
    
    def piocheCarte(self):
        carte = self.pioche.getCarte();
        return carte
        
        txt = "\n\n@@@@@@@@@@@@@@@ --------------- TOUR " + str(self.tour) + " --------------- @@@@@@@@@@@@@@@\n"
        txt += "ID=" + self.player1.toString()
        txt += "ID=" + self.player2.toString()
        return txt + "\n"
