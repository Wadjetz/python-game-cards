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
        '''
        Fait passer le tour suivant
        '''
        self.tour = self.tour + 1
        
    def enterrerServiteurs(self):
        self.player1.enterrerServiteurs()
        self.player2.enterrerServiteurs()
    
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
            #print(self.toString())
            self.playerAction(self.player1, self.player2)
            self.playerAction(self.player2, self.player1)
            
            self.tour = self.tour + 1
            
            self.player1.nextTour(self.tour)
            self.player2.nextTour(self.tour)
            
            print("Tous le monde Pioche une carte")
            
            #self.player1.piocheCarte(self)
            #self.player2.piocheCarte(self)
            
            
    def playerAction(self, player, playerTarget):
        '''
        Action du joueur
        @param player: Joueur
        @param playerTarget: Joueur adverse
        @param playerServiteurparam: Les serviteurs du joueur
        '''
        validator = True
        while validator:
            print(self.toString())
            ID = self.inputAction(player.name + " : entrer l'Id de la carte ou serviteur a utiliser (0 pour passer) ")
            if int(ID) == 0:
                validator = False
            elif int(ID) > 0 and int(ID) < 3:
                if int(player.mana) >= 2:
                    player.attaque(playerTarget)
                    player.mana = player.mana - 2 # L'attaque du joueur coute 2 mana
                    validator = False
                else:
                    print(player.name + " : Je n'ai pas suffisamment de mana")
            elif int(ID) > 10000 and int(ID) < 20000:
                try:
                    ID_cible = self.inputAction(player.name + " : entrer de la cible (0 pour passer) ")
                    player.useCarte(ID, playerTarget, ID_cible)
                    validator = False
                except Exception as e:
                    print(e)
            elif int(ID) > 20000:
                try:
                    ID_cible = self.inputAction(player.name + " : entrer de la cible (0 pour passer) ")
                    
                    player.useServiteur(ID, ID_cible, playerTarget)
                    validator = False
                except Exception as e:
                    print(e)
            else:
                print("Saisie incorrecte ()")
            self.enterrerServiteurs()

    def verifActionJoueur(self, joueur):
        '''
        Verifie si l'utilisateur peut encore faire des actions
        @param joueur: Le joueur
        '''
        if int(joueur.mana) == 0: # Si le joueur n'a plus de mana
            return False
        if joueur.action == False: # Si il a deja attaquer
            return False
        if self.verifActionServiteur(joueur) == False:
            return False
        return True
    
    def verifActionServiteur(self, joueur):
        '''
        Verifie si l'utilisateur peut utiliser un serviteur
        @return: True si l'utilisateur peut encore utiliser un serviteur. False si non
        '''
        flag = False
            
        for serv in joueur.serviteurs:
            if serv.action == True:
                flag = True
                
        return flag 
    
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
        txt = "\n\n@@@@@@@@@@@@@@@ --------------- TOUR " + str(self.tour) + " --------------- @@@@@@@@@@@@@@@\n"
        txt += "ID=" + self.player1.toString()
        txt += "ID=" + self.player2.toString()
        return txt + "\n"
