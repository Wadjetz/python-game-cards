# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''
from engine.Deck import Pioche, Deck
from engine.GameException import GameException
from engine.Player import Player


class Area(object):
    '''
    Terrain du jeux
    '''

    def __init__(self, namePlayer1, namePlayer2):
        '''
        Constructor
        @param namePlayer1: Nom du joueur 1
        @param namePlayer2: Nom du joueur 2
        '''
        self.tour = 1

        self.pioche = Pioche()
        deckPlayer1 = Deck("deck1", self.pioche.getDecks("deck1"))
        deckPlayer2 = Deck("deck1", self.pioche.getDecks("deck2"))
        
        self.player1 = Player(1, namePlayer1, deckPlayer1)
        self.player2 = Player(2, namePlayer2, deckPlayer2)
        
    def toString(self):
        txt = "\n\n@@@@@@@@@@@@@@@ --------------- TOUR " + str(self.tour) + " --------------- @@@@@@@@@@@@@@@\n"
        txt += "ID=" + str(self.player1)
        txt += "ID=" + str(self.player2)
        return txt + "\n"
    
    def __str__(self):
        return self.toString()
    
    def inputAction(self, message):
        '''
        Demande de saisie utilisateur
        @param message: prompt
        @return: int 
        '''
        ID = -1
        try:
            ID = input(message + "[int]# ")
            ID = int(ID)
        except EOFError:
            print("Saisie incorrecte EOFError=")
            ID = -1
        except NameError:
            print("Saisie incorrecte NameError")
            ID = -1
        except ValueError:
            print("Saisie incorrecte ValueError")
            ID = -1
        return ID
    
    def gameLoop(self):
        '''
        Boucle du jeux
        '''
        stop = False

        while stop == False:
            self.playerTurn(self.player1, self.player2)
            self.playerTurn(self.player2, self.player1)
            
            self.tour = self.tour + 1
            
            self.player1.nextTour(self.tour)
            self.player2.nextTour(self.tour)
            
            print("Tous le monde Pioche une carte")
            
            try:
                self.player1.piocheCarte()
            except GameException as e:
                print(self.player1.name + " " + str(e))
            try:
                self.player2.piocheCarte()
            except GameException as e:
                print(self.player2.name + " " + str(e))
                
            if self.player1.health <= 0:
                print(self.player1.name + " a perdu et " + self.player2.name + " a GAGNER !!!!")
                stop = True
            if self.player2.health <= 0:
                print(self.player2.name + " a perdu et " + self.player1.name + " a GAGNER !!!!")
                stop = True 
    
    def playerTurn(self, player, ennemy):
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
                #Passer le tour
                validator = False
            elif int(ID) > 0 and int(ID) < 3:
                # Si le joueur a choisie lui meme
                if int(player.mana) >= 2:
                    ID_target = self.inputAction(player.name + " : entrer de la cible (0 pour passer) ")
                    player.fight(ID_target, ennemy)
                    validator = self.verifActionJoueur(player)
                else:
                    print(player.name + " : Je n'ai pas suffisamment de mana")
            elif int(ID) > 1000000 and int(ID) < 2000000:
                # Si le joueur choisie un sort
                try:
                    ID_target = self.inputAction(player.name + " : entrer de la cible (0 pour passer) ")
                    player.useCarteSpell(ID, ID_target, ennemy)
                    validator = self.verifActionJoueur(player)
                except GameException as e:
                    print(e)
            elif int(ID) > 2000000 and int(ID) < 3000000:
                # Si le joueur a choisie d'invoquer un serviteur
                try:
                    player.invoke(ID)
                    validator = self.verifActionJoueur(player)
                except GameException as e:
                    print(e)
            elif int(ID) > 3000000:
                try:
                    ID_target = self.inputAction(player.name + " : entrer de la cible (0 pour passer) ")
                    servant = player.getServiteur(ID)
                    servant.fight(ID_target, ennemy)
                    validator = self.verifActionJoueur(player)
                except GameException as e:
                    print(e)
            else:
                print("Saisie incorrecte ()")
                
            
            self.player1.enterrerServiteurs()
            self.player2.enterrerServiteurs()
            
    def verifActionJoueur(self, joueur):
        '''
        Verifie si l'utilisateur peut encore faire des actions
        @param joueur: Le joueur
        '''
        flag = False
        if int(joueur.mana) > 0: # Si le joueur n'a plus de mana
            if joueur.action == True:
                flag = True
            
        
        for key in joueur.fields:
            if joueur.fields[key].action == True:
                flag = True
        
        return flag
