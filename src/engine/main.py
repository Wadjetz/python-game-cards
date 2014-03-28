# -*- coding : utf-8 -*-
'''
Created on 11 mars 2014

@author: egor
'''
from engine.Terrain import Terrain

def main():
    print("Game Run")
    terrain = Terrain("Egor", "Quentin")
    terrain.gameLoop()

if __name__ == '__main__':main()