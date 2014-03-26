'''
Created on 11 mars 2014

@author: egor
'''

class Pioche(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        
        file = open("Cartes", "r")
        
        for line in file:
            print(line)
        
        
    def dispaly(self):
        print(self.toString())
        
    def toString(self):
        return ""
        