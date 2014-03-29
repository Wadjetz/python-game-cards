# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''
from engine.CarteServiteur import CarteServiteur
from engine.CarteSort import CarteSort
from engine.Entity import Entity

class Player(Entity):
    '''
    Joueur Principale
    @param main: Les cartes utilisable par le joueur
    '''
    def __init__(self, ID, name):
        '''
        Constructor
        '''
        
        Entity.__init__(self, ID, name, "description", 30, 1, 5)
        self.action = True
        self.main = {}
        self.serviteurs = {}
        
        
    def nextTour(self, tour):
        '''
        Passe au tour suivant et augmente le mana en fonction du tour
        @param tour: Numero du tour
        '''
        if (tour > 10):
            self.mana = 10
        else:
            self.mana = tour
        
        if self.health <= 0:
            print("Est mort " + self.toString())
    
    def enterrerServiteurs(self):
        servDeath = []
        
        for key in self.serviteurs:
            if self.serviteurs[key].health <= 0:
                print(self.serviteurs[key].name + " est mort { " + self.serviteurs[key].toString() + " }")
                servDeath.append(key)
        
        for id in servDeath:
            del self.serviteurs[id]
    
    def piocheCarte(self, terrain):
        '''
        Piche une nouvelle carte
        @param terrain: Le terraint
        '''
        carte = terrain.piocheCarte()
        self.main[str(carte.ID)] = carte
    
    def useCarte(self, ID_carte, cible, ID_cible):
        '''
        Utilise une carte de ca main
        @param ID_carte: la carte a utiliser
        @param cible: Cible de l'utilisation soit le terrain ou un joueur ou un serviteur
        '''
        carte = ""
        try:
            carte = self.getCarte(ID_carte)
        
            if int(self.mana) >= int(carte.mana):
            
                if (isinstance(carte, CarteServiteur) == True):
                    serviteur = carte.getServiteur(self)
                    print(self.name + " invoque " + serviteur.toString())
                    self.serviteurs[str(serviteur.ID)] = serviteur
                if (isinstance(carte, CarteSort) == True):
                    if int(ID_cible) > 0 and int(ID_cible) < 3:
                        carte.attaque(cible)
                    if int(ID_cible) > 20000:
                        print("Attaque Serviteur(bientot)")
                self.mana = int(self.mana) - int(carte.mana)
                self.deleteCarte(ID_carte)
                self.action = False
            else:
                raise Exception(self.name + " : Je n'ai pas suffisamment de mana")
        except Exception as e:
            raise Exception(e)
    
    def useServiteur(self, ID_serv, ID_cible, playerCible):
        '''
        Le joueur attaque avec un serviteur
        @param ID_serv: Id du serviteur
        @param ID_cible: Id de la cible
        @param cible: Joueur adverse
        '''
        try:
            serv = self.getServiteur(ID_serv)
            if int(ID_cible) > 0 and int(ID_cible) < 3: # On attaque un joueur
                serv = self.serviteurs[str(ID_serv)]
                serv.attaque(playerCible)
            else:
                serv = self.serviteurs[str(ID_serv)]
                serv.servAttaque(ID_cible, playerCible)
        except Exception as e:
            raise Exception(e)
    
    def getServiteur(self, ID_serv):
        '''
        Inflige les degats a un serviteur
        '''
        if self.serviteurs.has_key(str(ID_serv)):
            return self.serviteurs[str(ID_serv)]
        else:
            raise Exception(self.name + " : j'ai pas ce serviteur " + str(ID_serv))
            
    
    def getCarte(self, ID_carte):
        '''
        Recupere la carte dans la main du joueur
        @param ID_carte: Id de la carte
        '''
        if self.main.has_key(str(ID_carte)):
            return self.main[str(ID_carte)]
        else:
            raise Exception(self.name + " : j'ai pas cette carte " + str(ID_carte) )
    
    def deleteCarte(self, ID_carte):
        if self.main.has_key(str(ID_carte)):
            del self.main[str(ID_carte)]
    
    def recevoirDegetsServiteur(self, ID_serv, serviteurAttaquant):
        '''
        Le serviteur du joueur recois des degats
        @param ID_serv: Id du serviteur a attaquer
        @param serviteurAttaquant: serviteur qui attaque
        '''
    
    def toString(self):
        '''
        Affiche les cartes que possede le joueur
        '''
        string = " Main = {\n"
        for key in self.main:
            carte = self.main[key]
            string += "\t"+ "ID=" + carte.toString() + "\n"
        string += "\tLes Serviteur de " + self.name + "\n"
        for s in self.serviteurs:
            string += "\tID=" + self.serviteurs[s].toString() + "\n"
        return Entity.toString(self) + string + "}\n"
