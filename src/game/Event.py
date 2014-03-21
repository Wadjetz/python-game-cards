'''
Created on 21 mars 2014

@author: quenti77
'''
import pygame
from pygame.constants import *

from ihm.log import Log


class Event(object):
    '''
    Gestion des events
    '''

    def __init__(self):
        '''
        Constructeur
        '''
        self.quit = False
        self.keyboard = []
        self.posX = 0
        self.posY = 0
        self.posRelX = 0
        self.posRelY = 0
        self.button = []
        self.width = 800
        self.height = 600
        
        for i in range(512):
            self.keyboard.append(False)
        
        for i in range(8):
            self.button.append(False)
        
    
    def update(self):
        for event in pygame.event.get():
            if (event.type == QUIT):
                self.quit = True
            elif (event.type == KEYDOWN):
                self.keyboard[event.key] = True
            elif (event.type == KEYUP):
                self.keyboard[event.key] = False
            elif (event.type == MOUSEBUTTONDOWN):
                self.button[event.button] = True
            elif (event.type == MOUSEBUTTONUP):
                self.button[event.button] = False
            elif (event.type == MOUSEMOTION):
                self.posX = event.pos[0]
                self.posY = event.pos[1]
                self.posRelX = event.rel[0]
                self.posRelY = event.rel[1]
            elif (event.type == VIDEORESIZE):
                print("Resize : ", event.w, event.h)
                self.width = event.w
                self.height = event.h