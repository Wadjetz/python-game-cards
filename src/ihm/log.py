'''
Created on 14 mars 2014

@author: quenti77
'''

class Log(object):
    '''
    Permet de gérer les logs du jeu
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.level = 3
    
    def showLog(self, message, levelType):
        '''
        Affiche un log si le niveau est bon
        '''
        if (levelType <= self.level):
            print(message)
    
    def showInfo(self, message):
        self.showLog("[INFO]: " + message, 1)
    
    def showWarning(self, message):
        self.showLog("[WARNING]: " + message, 2)
        
    def showError(self, message):
        self.showLog("[ERROR]: " + message, 2)
        
    def showCritic(self, message):
        self.showLog("[CRITIC]: " + message, 1)
        
    def showDebug(self, message):
        self.showLog("[DEBUG]: " + message, 3)
        