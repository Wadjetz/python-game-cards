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
            
            if self.player1.health <= 0:
                print(self.player1.name + " a perdu et " + self.player2.name + " a GAGNER !!!!")
                stop = True
            if self.player2.health <= 0:
                print(self.player2.name + " a perdu et " + self.player1.name + " a GAGNER !!!!")
                stop = True 
            
            self.playerTurn_v2(self.player1, self.player2)
            #self.playerTurnIA(self.player2, self.player1)
            self.playerTurnIA(self.player2, self.player1)
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
    
    def gameLoopNetworkHost(self, host, conn):
        '''
        Boucle du jeux en réseau pour l'host
        '''
        
        stop = False

        while stop == False:
            
            if self.player1.health <= 0:
                print(self.player1.name + " a perdu et " + self.player2.name + " a GAGNER !!!!")
                stop = True
            if self.player2.health <= 0:
                print(self.player2.name + " a perdu et " + self.player1.name + " a GAGNER !!!!")
                stop = True 
            
            self.playerTurn_v2(self.player1, self.player2)
            self = host.run(self, conn)
            
            
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
        host.close(conn)
    
    def gameLoopNetworkClient(self):
        self.playerTurn_v2(self.player2, self.player1)
        return self
    
    
    def playerTurn_v2(self, player, ennemy):
        '''
        Les interaction du joueur pendant le tour
        @param player: Joueur
        @param ennemy: Joueur adverse
        '''
        validator = True
        while validator:
            self.player1.enterrerServiteurs()
            self.player2.enterrerServiteurs()
            print(self)
            try:
                ID_attack = self.inputAction("<" + player.name + "> Id carte ou serviteur [passer=0]")
                
                if int(ID_attack) == 0:
                    # Si le joueur souhaite passer son tour
                    print(player.name + " passe son tour")
                    validator = False
                elif int(ID_attack) < 0:
                    print("Saisie incorrecte")
                else:
                    if player.isCarteServant(ID_attack):
                        # Si c'est une carte d'invocation des serviteur
                        player.invoke(ID_attack)
                        validator = self.verifActionJoueur(player)
                    else:
                        #Si ce n'est pas une carte sort
                        ID_target = self.inputAction(player.name + " : entrer de la cible [annuler=0]")
                        if int(ID_target) == 0:
                            pass
                        else:
                            player.war(ID_attack, ID_target, ennemy)
                            validator = self.verifActionJoueur(player)
                
            except GameException as e:
                print(e)
    
    def choiseTargetIA(self, ennemy):
        '''
        Choisie le cible a attaquer
        '''
        ID_Target = 2
        if len(ennemy.fields) > 0:
            for ID_serv in ennemy.fields:
                if ennemy.fields[ID_serv].camouflage != True:
                    ID_Target = ID_serv
        return ID_Target
    
    def playerTurnIA(self, player, ennemy):
        '''
        Action du joueur
        @param player: Joueur
        @param ennemy: Joueur adverse
        '''
        self.player1.enterrerServiteurs()
        self.player2.enterrerServiteurs()
        if len(player.fields):
            print("Attaques des serviteur")
            for ID_serv in player.fields:
                if player.fields[ID_serv].action == True:
                    ID_Target = self.choiseTargetIA(ennemy)
                    player.fields[ID_serv].fight(ID_Target, ennemy)
                    
        print("Attaques du joueur")
        ID_Carte = 0
        #go = False
        for carte in player.hand:
            if player.hand[carte].cost <= player.mana and player.isCarteServant(carte):
                print("IA choisie " + carte)
                ID_Carte = carte
                break
        if ID_Carte != 0:
            print("IA utilise " + carte)
            player.invoke(carte)
        
        ID_Carte = 0
        ID_Target = 0
        for carte in player.hand:
            if player.hand[carte].cost <= player.mana:
                #print(player.hand[carte])
                
                if player.isSpell(carte):
                    ID_Target = self.choiseTargetIA(ennemy)
                    ID_Carte = carte
        if ID_Target != 0:
            player.useCarteSpell(ID_Carte, ID_Target, ennemy)
            
            

            '''
            
            ID = self.inputAction("<" + player.name + "> Id carte ou serviteur [passer=0]")
            
            if int(ID) == 0:
                #Passer le tour
                validator = False
            elif self.isPlayer(ID):
                # Si le joueur a choisie lui meme
                if int(player.mana) >= 2:
                    ID_target = self.inputAction(player.name + " : entrer de la cible [passer=0]")
                    player.fight(ID_target, ennemy)
                    validator = self.verifActionJoueur(player)
                else:
                    print(player.name + " : Je n'ai pas suffisamment de mana")
            elif self.isSpell(ID):
                # Si le joueur choisie un sort
                try:
                    ID_target = self.inputAction(player.name + " : entrer de la cible [passer=0]")
                    player.useCarteSpell(ID, ID_target, ennemy)
                    validator = self.verifActionJoueur(player)
                except GameException as e:
                    print(e)
            elif player.isCarteServant(ID):
                # Si le joueur a choisie d'invoquer un serviteur
                try:
                    player.invoke(ID)
                    validator = self.verifActionJoueur(player)
                except GameException as e:
                    print(e)
            elif self.isServant(ID):
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
        '''
    
    def playerTurn(self, player, ennemy):
        '''
        Action du joueur
        @param player: Joueur
        @param ennemy: Joueur adverse
        '''
        validator = True
        
        while validator:

            print(self.toString())
            
            ID = self.inputAction("<" + player.name + "> Id carte ou serviteur [passer=0]")
            
            if int(ID) == 0:
                #Passer le tour
                validator = False
            elif self.isPlayer(ID):
                # Si le joueur a choisie lui meme
                if int(player.mana) >= 2:
                    ID_target = self.inputAction(player.name + " : entrer de la cible [passer=0]")
                    player.fight(ID_target, ennemy)
                    validator = self.verifActionJoueur(player)
                else:
                    print(player.name + " : Je n'ai pas suffisamment de mana")
            elif self.isSpell(ID):
                # Si le joueur choisie un sort
                try:
                    ID_target = self.inputAction(player.name + " : entrer de la cible [passer=0]")
                    player.useCarteSpell(ID, ID_target, ennemy)
                    validator = self.verifActionJoueur(player)
                except GameException as e:
                    print(e)
            elif player.isCarteServant(ID):
                # Si le joueur a choisie d'invoquer un serviteur
                try:
                    player.invoke(ID)
                    validator = self.verifActionJoueur(player)
                except GameException as e:
                    print(e)
            elif self.isServant(ID):
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
    
    def toString(self):
        txt = "\n\n@@@@@@@@@@@@@@@ --------------- TOUR " + str(self.tour) + " --------------- @@@@@@@@@@@@@@@\n"
        txt += "ID=" + str(self.player1)
        txt += "ID=" + str(self.player2)
        return txt + "\n"
    
    def toString_v2(self):
        txt = "\n\n@@@@@@@@@@@@@@@ --------------- TOUR " + str(self.tour) + " --------------- @@@@@@@@@@@@@@@\n"
        txt += "ID=" + str(self.player1)
        txt += "ID=" + str(self.player2.ID) + ":" + str(self.player2.name) + ":[" + str(self.player2.mana) + "pm, " + str(self.player2.health) + "pv, a=" + str(self.player2.action) + "] "
        txt += " Fields :\n"
        for key in self.player2.fields:
            txt += "\t" + str(self.player2.fields[key]) + "\n"
        return txt + "}\n"
    
    def __str__(self):
        return self.toString_v2()
    
    def setPlayer1(self, player1):
        self.player1 = player1
        
    def setPlayer2(self, player2):
        self.player2 = player2
        
    def getPlayer1(self):
        return self.player1
    
    def getPlayer2(self):
        return self.player2
    
    def getTour(self):
        return self.tour
