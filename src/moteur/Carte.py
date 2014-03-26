'''
Created on 11 mars 2014

@author: egor
'''

class Carte(object):
    '''
    classdocs
    '''

    def __init__(self, name, nbPointVie, degats, nbPointMana):
        '''
        Constructor
        '''
        self.name = name
        self.nbPointVie = nbPointVie
        self.degats = degats
        self.nbPointMana = nbPointMana

    def display(self):
        print(self.toString())
        
    def toString(self):
        return self.name + ":[vie=" + str(self.nbPointVie) + ", mana=" + str(self.nbPointMana) + ", degats=" + str(self.degats) + "]"
        