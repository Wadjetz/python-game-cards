# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''
from engine.Area import Area


def main():
    print("Game Run")
    area = Area("Egor", "Quentin")
    area.gameLoop()
if __name__ == '__main__':main()