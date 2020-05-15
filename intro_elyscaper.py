#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2020 Tristan Nerson <tristan.nerson@univ-lemans.fr>              #
# Creation Date: Sunday, March 8th 2020, 10:54:28 pm                           #
# -----                                                                        #
# 'intro_elyscaper.py' is part of the project 'elyscaper_game'.                #
#                                                                              #
# elyscaper_game is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# elyscaper_game is distributed in the hope that it will be useful,            #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with elyscaper_game.  If not, see <https://www.gnu.org/licenses/>.     #
################################################################################
"""This file is used to create methods that will be interesting for the introduction of the game
"""

import sys
import json

import time
import numpy as np
import random as rd

import usual

# ---------------------------------------- Initialisation ---------------------------------------- #

writer = usual.Writer()

with open('elyscaper_data.json') as json_file: # all long sentences are written here
    data = json.load(json_file)

# ------------------------------------------------------------------------------------------------ #
#                                               Class                                              #
# ------------------------------------------------------------------------------------------------ #

class Display_intro:
    """Many methods that will be interesting for the introduction
    """
    def __init__(self):
        """Initialisation
        """
        self.n = 50
        self.p = 50
        self.m = np.random.randint(10, size=(self.n, self.p))
                
                    
    def matrix(self,space):
        """Create a matrix to simulate a loading
        """
        i=0
        while i<1000000:
            print(rd.randint(0,9),end=space)
            i+=1
                        

    def point(self,n,s):
        """Add a centerd point each s seconds (n times)
        
        Arguments:
            n {int} -- number of points
            s {float} -- number of seconds
        """
        for i in range(n):
           time.sleep(s)
           writer.text(".")    
                       
    def menu(self,hero):
        """Show the menu
        """
        writer.text("- Si vous souhaitez lancer une partie, cliquez sur (P)")
        writer.jump()
        writer.text("- Si vous souhaitez regarder le fonctionnement du jeu, cliquez sur (F)")
        writer.jump()        
        writer.text("- Si vous souhaitez changer de nom, cliquez sur (N)")      
        writer.end()

        self.r = input("")
        
        if self.r == "F":
            writer.clear()
            writer.para_input(data["rules"])
            self.menu(hero)
        elif self.r == "P":
            pass

        elif self.r == "N":
            writer.clear()
            writer.text("Nom du joueur ?")
            writer.end()
            hero.name = input("")
            writer.clear()
            writer.para_time("Bonjour {}, votre partie est prête.".format(hero.name))
            self.menu(hero)     

        else:
            writer.clear()
            self.menu(hero)
            

# ------------------------------------------- __main__ ------------------------------------------- #

if __name__ == '__main__':
    pass