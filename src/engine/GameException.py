'''
Created on 1 avr. 2014

@author: egor
'''

class GameException(Exception):
    '''
    GameException
    '''
    
    def __init__(self, message):
        '''
        Constructor
        '''
        Exception.__init__(self, message)
        self.message = message
    
    def __str__(self):
        return self.message     