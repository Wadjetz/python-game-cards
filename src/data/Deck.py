'''
Created on 14 mars 2014

@author: quenti77
'''

class Deck(object):
    '''
    Un deck du jeu ou toute les cartes du jeu disponibles
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.name = ""
        self.desc = ""
        self.check = False
        self.cards = []
        
    def load(self, path):
        from game.Game import Game
        try:
            file = open(path, "r+", 1)
            
            for line in file:
                line = line.rstrip('\n')
                
                data = line.split('|')
                if len(data) == 7:
                    from data.Card import Card
                    carteAdd = Card()
                    setattr(carteAdd, "name", data[0])
                    setattr(carteAdd, "desc", data[1])
                    setattr(carteAdd, "type", data[2])
                    setattr(carteAdd, "mode", 0)
                    setattr(carteAdd, "attack", int(data[3]))
                    setattr(carteAdd, "defense", int(data[4]))
                    setattr(carteAdd, "cost", int(data[5]))
                    setattr(carteAdd, "cost", int(data[6]))
                    
                    Game.logger.showDebug("Ajout d'une carte " + carteAdd.type)
                    self.cards.append(carteAdd)
                elif len(data) == 2:
                    Game.logger.showDebug("Modification de la propriété " + data[0])
                    if data[0] == "deck.name":
                        self.name = data[1]
                    elif data[0] == "deck.desc":
                        self.desc = data[1]
                    elif data[0] == "deck.check":
                        self.check = (data[1] == "true")
            
        except:
            Game.logger.showCritic("Impossible d'ouvrir le fichier : '" + path + "'")
        else:
            Game.logger.showInfo("Deck " + self.name + " chargé !")