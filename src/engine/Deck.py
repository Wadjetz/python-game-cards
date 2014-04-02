'''
Created on 31 mars 2014

@author: egor
'''
from copy import copy
import json
import random

from engine.CardServant import CardServant
from engine.CardSpell import CardSpell
from engine.GameException import GameException


class Deck(object):
    '''
    Deck
    '''
    
    def __init__(self, name, cards):
        '''
        Constructor
        '''
        self.name = name
        self.cards = cards
        
    def getCarte(self):
        '''
        Recupere une carte au hasard dans le total des cartes
        '''
        try:
            keys = self.cards.keys()
            i = random.randrange(len(keys))
            tmp = copy(self.cards[keys[i]])
            del self.cards[keys[i]]
            return tmp
        except ValueError:
            raise GameException("Deck vide")
    
    def toString(self):
        txt = "Deck " + self.name + " :\n"
        for key in self.cards:
            txt += self.cards[key].toString() + "\n"
        return txt
    
    def __str__(self):
        return self.toString()
    

class Pioche(object):
    '''
    Contient tous les cartes du jeux
    '''
    
    def __init__(self):
        '''
        Constructor
        ''' 
        self.totalCards = {}
        self.__loadJson()
    
    def __loadJson(self):
        '''
        Carge les cartes dans les fichiers JSON
        '''
        #Load Serviteurs
        fileServants = open("../res/cards/serviteurs.json", "r")
        dumpServants = json.load(fileServants)
        for c in dumpServants:
            #ID, Type, name, description, dialog, cost, attack, damage, health, vulnerability
            carte = CardServant(c["id"], c["type"], c["name"], c["description"], c["dialog"], c["cost"], c["attack"], c["damage"], c["health"], c["effect"])
            self.totalCards[str(c["id"])] = carte
        fileServants.close()
        
        #Load Serviteur
        fileSorts = open("../res/cards/sorts.json", "r")
        dumpSorts = json.load(fileSorts)
        for c in dumpSorts:
            #self, ID, Type, name, description, dialog, cost, attack, damage, effect
            carte = CardSpell(c["id"], c["type"], c["name"], c["description"], c["dialog"], c["cost"], c["attack"], c["damage"], c["effect"])
            self.totalCards[str(c["id"])] = carte
        fileSorts.close()
    
    def getDecks(self, name):
        '''
        Construit le deck
        @param name: Nom du deck
        @return: dict des cartes du deck
        '''
        deck = {}
        ids = self.__loadJsonDeck(name)
        for c in ids:
            if self.totalCards.has_key(str(c)):
                deck[c] = self.totalCards[str(c)]
        return deck
        
    def __loadJsonDeck(self, name):
        '''
        Carge les ids des cartes dans les fichiers JSON
        @param name: Nom du deck
        @return: tableau d'ids des cartes du deck
        '''
        deckPlayer = []
        fileDeck = open("../res/cards/deck.json", "r")
        dumpServants = json.load(fileDeck)
        for c in dumpServants:
            if c["name"] == name:
                for i in c["cards"]:
                    deckPlayer.append(i)
        fileDeck.close()
        return deckPlayer
    
    def toString(self):
        '''
        '''
        txt = "Total des cartes " + str(len(self.totalCards)) + "\n"
        for key in self.totalCards:
            txt += self.totalCards[key].toString() + "\n"
        return txt
        
    def __str__(self):
        return self.toString()
        