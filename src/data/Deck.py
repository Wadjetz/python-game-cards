'''
Created on 14 mars 2014

@author: quenti77
'''
from ihm.log import Log

class Deck(object):
    '''
    Un deck du jeu ou toute les cartes du jeu disponibles
    '''

    def __init__(self):
        '''
        Constructeur
        '''
        self.name = ""
        self.desc = ""
        self.check = False
        self.cards = []
        
    def load(self, path):
        from game.Game import Game
        from data.Card import Card
        try:
            file = open(path, "r+", 1)
            
            for line in file:
                line = line.rstrip('\n')
                
                data = line.split('|')
                if len(data) == 8:
                    carteAdd = Card()
    
                    setattr(carteAdd, "name", data[0])
                    setattr(carteAdd, "desc", data[1])
                    setattr(carteAdd, "type", data[2])
                    setattr(carteAdd, "mode", 0)
                    setattr(carteAdd, "level", int(data[3]))
                    setattr(carteAdd, "attack", int(data[4]))
                    setattr(carteAdd, "life", int(data[5]))
                    setattr(carteAdd, "shield", int(data[6]))
                    setattr(carteAdd, "cost", int(data[7]))
                    
                    self.cards.append(carteAdd)
                elif len(data) == 2:
                    if data[0] == "deck.name":
                        self.name = data[1]
                    elif data[0] == "deck.desc":
                        self.desc = data[1]
                    elif data[0] == "deck.check":
                        self.check = (data[1] == "true")
            
        except:
            pass
        else:
            pass
            
    def addCard(self, card):
        pass