# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''

from engine.LivingEntity import LivingEntity
from engine.GameException import GameException


class Player(LivingEntity):
    '''
    Joueur Principale
    @param main: Les cartes utilisable par le joueur
    '''
    def __init__(self, ID, name, deck):
        '''
        Constructor
        @param ID: id unique de la carte
        @param name: Nom
        @param deck: Les carte utilisable par le joueur
        '''
        LivingEntity.__init__(self, ID, "player", name, 1, "normal", "effect", "description", "dialog", 30)
        self.deck = deck
        self.mana = 1
        self.hand = {}
        self.fields = {}
        self.action = True
        for i in range(4):
            i
            self.piocheCarte()
    
    def isHasProvocation(self):
        '''
        Verifie si un serviteur possede la provocation
        @return: pair(Boolean, [Serviteur]) True si le joueur possede un serviteur avec provocation
                 Et le tableaux des serviteur qui le possede
        '''
        servProvoc = []
        flag = False
        for key in self.fields:
            servant = self.fields[key]
            if servant.effect == "provocation":
                servProvoc = servant
                flag = True
        return (flag, servProvoc)
    
    def invoke(self, ID):
        '''
        Invoque un serviteur
        '''
        carte = self.getCarte(ID)
        if int(self.mana) >= int(carte.cost):
            servant = carte.invokeServant()
            self.fields[str(servant.ID)] = servant
            self.mana = int(self.mana) - int(carte.cost)
            print(str(self.name) + " invoque " + str(servant))
            self.deleteCarte(ID)
        else:
            raise GameException("J'ai pas assais de mana pour invoker " + str(carte))
    
    def piocheCarte(self):
        '''
        Piche une nouvelle carte dans le deck
        @param terrain: Le terraint
        '''
        carte = self.deck.getCarte()
        self.hand[str(carte.ID)] = carte
    
    def getCarte(self, ID):
        '''
        Recupere la carte dans la main du joueur
        @param ID: Id de la carte
        '''
        try:
            return self.hand[str(ID)]
        except KeyError:
            raise GameException(self.name + " : j'ai pas cette carte " + str(ID))
    
    def deleteCarte(self, ID):
        if str(ID) in self.hand:
            del self.hand[str(ID)]
    
    def getServiteur(self, ID_serv):
        '''
        Recupere un serviteur dans le hand
        '''
        try:
            return self.fields[str(ID_serv)]
        except KeyError:
            raise GameException(self.name + " : j'ai pas ce serviteur " + str(ID_serv))
    
            
    def useCarteSpell(self, ID_card, ID_target, ennemy):
        '''
        Utilise une carte sort
        @param ID_card: Id de la carte a utiliser
        @param ID_target: Id de la cible (joueur ou serviteur)
        @param ennemy: Joueur ennemie
        '''
        
        carte = self.getCarte(ID_card)
        
        if int(self.mana) >= int(carte.cost):
            if carte.effect == "health":
                if int(ID_target) > 0 and int(ID_target) < 3:
                    carte.health(self)
                elif int(ID_target) > 3000000:
                    serv = self.getServiteur(ID_target)
                    carte.health(serv)
                self.consumeMana(carte.cost)
                self.deleteCarte(ID_card);
    
            else:
                isHasP, servTarget = ennemy.isHasProvocation()
                if isHasP == True:
                    print("Provocation " + self.name + " : attaque " + servTarget.name + " de " + str(carte.attack) + "dmg")
                    servTarget.domage(carte.attack, carte.damageType)
                else:
                    if int(ID_target) > 0 and int(ID_target) < 3:
                        print(self.name + " : attaque " + ennemy.name + " de " + str(carte.attack) + "dmg")
                        ennemy.domage(carte.attack)
                    else:
                        servant = ennemy.getServiteur(ID_target)
                        print(self.name + " attaque " + servant.name + " de " + str(carte.attack) + "dmg")
                        servant.domage(carte.attack, carte.damageType)
                self.mana = int(self.mana) - int(carte.cost)
                self.deleteCarte(ID_card)
        else:
            raise GameException("J'ai pas assais de mana pour utiliser " + str(carte))
    
    def fight(self, ID_target, ennemy):
        '''
        L'attaque du joueur
        '''
        if self.action == True:
            if int(self.mana) >= 2:
                isHasP, servTarget = ennemy.isHasProvocation()
                if isHasP == True:
                    for serv in servTarget:
                        if serv.ID == ID_target:
                            #si la cible de l'attaque possede la provocation
                            print("Provocation : " + self.name + " : attaque " + serv.name + " de " + str(self.attack) + "dmg")
                            serv.domage(self.attack, "normal")
                        else:
                            print(serv)
                else:
                    if int(ID_target) > 0 and int(ID_target) < 3:
                        print(str(self.name) + " inflige " + str(self.attack) + " dmg a" + str(ennemy.name))
                        ennemy.domage(self.attack)
                    if (int(ID_target) > 3000000):
                        servant = ennemy.getServiteur(ID_target)
                        servant.domage((int(self.attack) + 1), "")
                        print(self.name + " attaque " + servant.name + " de " + str(self.attack + 1) + "dmg")
                self.action = False
                self.consumeMana(2)
            else:
                raise GameException(self.name + " : Je n'ai pas suffisamment de mana")
        else:
            raise GameException(self.name + " : Je ne peux plus attaquer")
    
    def fight_v2(self):
        '''
        '''
    
    def war(self, ID_attack, ID_target, ennemy):
        '''
        '''
        print("THIS IS A SPARTA")
        if self.isPlayer(ID_attack):
            #le joueur attaque
            self.fight(ID_target, ennemy)
            
        if self.isSpell(ID_attack):
            #le joueur utilise une carte
            self.useCarteSpell(ID_attack, ID_target, ennemy)
            
        if self.isServant(ID_attack):
            #le joueur fait attaquer un serviteur
            servant = self.getServiteur(ID_attack)
            servant.fight(ID_target, ennemy)
            
    
    def consumeMana(self, pMana):
        self.mana -= pMana
    
    def enterrerServiteurs(self):
        '''
        Supprime les serviteur Morts
        '''
        servDeath = []
        
        for key in self.fields:
            if self.fields[key].health <= 0:
                print(self.fields[key].name + " est mort { " + self.fields[key].toString() + " }")
                servDeath.append(key)
        
        for i in servDeath:
            del self.fields[i]
            
    def nextTour(self, tour):
        '''
        Passe au tour suivant et augmente le mana en fonction du tour
        @param tour: Numero du tour
        '''
        if (tour > 10):
            self.mana = 10
        else:
            self.mana = tour
        
        LivingEntity.nextTour(self, tour)
        
        for key in self.fields:
            self.fields[key].nextTour(tour)
        
        if self.health <= 0:
            print(self.name + "Est mort " + self.toString())
            
    def isPlayer(self, ID):
        '''
        Verifie si l'id correspond un un joueur
        @param ID: Id du joueur
        '''
        if int(ID) > 0 and int(ID) < 3:
            return True
        else:
            return False
        
    def isSpell(self, ID):
        '''
        Verifie si l'id correspond a une carte sort
        '''
        if int(ID) > 1000000 and int(ID) < 2000000:
            return True
        else:
            return False
        
    def isCarteServant(self, ID):
        '''
        Verifie si l'id correspond a une carte qui invoque un serviteur
        '''
        if int(ID) > 2000000 and int(ID) < 3000000:
            return True
        else:
            return False
    
    def isServant(self, ID):
        '''
        Verifie si l'id correspond a un serviteur
        '''
        if int(ID) > 3000000:
            return True
        else:
            return False
    
    def toString(self):
        '''
        Affiche les informations joueur
        '''
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[" + str(self.mana) + "pm, " + str(self.health) + "pv, a=" + str(self.action) + "] "
        txt += "Hand = {\n"
        for key in self.hand:
            carte = self.hand[key]
            txt += "\t" + str(carte) + "\n"
        txt += "\t" + self.name + " Fields :\n"
        for key in self.fields:
            txt += "\t" + str(self.fields[key]) + "\n"
        return txt + "}\n"
    
    def __str__(self):
        return self.toString()