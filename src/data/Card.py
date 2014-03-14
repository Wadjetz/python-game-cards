'''
Created on 14 mars 2014

@author: quenti77
'''

class Card(object):
    '''
    Une carte du jeu (ou quelle soit dans le jeu)
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.name = ""
        self.desc = ""
        self.type = ""
        self.mode = 0
        self.attack = -1
        self.defense = -1
        self.cost = 0
        self.level = 1
        
    def debugInfo(self):
        from game.Game import Game
        Game.logger.showDebug("===== " + self.name + " =====")
        Game.logger.showDebug("> " + self.desc + "")
        Game.logger.showDebug("> " + self.type + "")
        Game.logger.showDebug("> " + str(self.mode) + "")
        Game.logger.showDebug("> " + str(self.attack) + "")
        Game.logger.showDebug("> " + str(self.defense) + "")
        Game.logger.showDebug("> " + str(self.cost) + "")
    