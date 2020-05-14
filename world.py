#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2020 Tristan Nerson <tristan.nerson.etu@univ-lemans.fr>          #
# Creation Date: Monday, April 20th 2020, 4:21:56 pm                           #
# -----                                                                        #
# 'world.py' is part of the project 'elyscaper_game'.                          #
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
"""This file is made to create worlds and to generate introductions screens of
those worlds. It also creates lists of worlds and weapons in it.
"""

import json
import usual
import ascii_img
import characters
import weapons

with open('elyscaper_data.json') as json_file:
    data = json.load(json_file)

list_worlds = []

writer = usual.Writer()

def microcosme(w_name,dim,msg,deja,adj):
    """Configure an introduction's screen

    Arguments:
        w_name {str} -- name of the world
        dim {int} -- number of ligns/colummns to remove
        msg {str} -- the message to show
        deja {str} -- the text that will be shown according to the number of visits
        adj {str} -- an adjective to describe the world
    """
    writer.clear()
    exemple = min(writer.l-dim,writer.c-dim)     
    ascii = ascii_img.AsciiConverter(exemple,exemple)
    ascii.to_ascii_color("pictures/{}.jpg".format(w_name))
    writer.text(msg.format(deja,adj),color="\033[4m")
    writer.end(13) #13 is a small space bitween the text and the bottom


class world:
    """Create a world with its caracteristics
    """
    def __init__(self,w_name):
        """Initialisation

        Arguments:
            w_name {str} -- the name of your world
        """
        self.w_name = w_name
        self.already_went = 0
        self.deja = ""
        
        list_worlds.append(self.w_name)
        
        self.characters_in_world = []
        self.weapons_in_world = []
        
        for i in range(len(characters.list_characters)):
            if self.w_name == characters.list_characters[i].world:
                self.characters_in_world.append(characters.list_characters[i]) 
                # fill the list with all creatures of this world
                
        for i in range(len(weapons.list_weapons)):
            if self.w_name == weapons.list_weapons[i].world:
                self.weapons_in_world.append(weapons.list_weapons[i]) 
                # fill the list with all weapons of this world       
            

    def deja_def(self):
        """print the right text according to your number of visits in this world
        """
        if self.already_went == 1:
            self.deja = "encore "
        elif self.already_went == 2:
            self.deja = "encore et encore "
        elif self.already_went >= 3:
            self.deja = "pour la énième fois " 
        
    def intro_world(self):
        """Set up the introduction screen of the world (it also counts 
        the number of visits to make it match with the text)
        """
        self.deja_def()  
        self.msg="Vous vous réveillez {}dans un microcosme {}..."
        if self.w_name == "wate": 
            microcosme("water",10,self.msg,self.deja,"aquatique")
        if self.w_name == "stone":
            microcosme("stone",-3,self.msg,self.deja,"minéral")
        if self.w_name == "dark":
            microcosme("dark",10,self.msg,self.deja,"ténébreux")
        if self.w_name == "steel":
            microcosme("steel",5,self.msg,self.deja,"métallique")
        if self.w_name == "ice":
            microcosme("ice",5,self.msg,self.deja,"glaciaire")
        if self.w_name == "tree":
            microcosme("tree",9,self.msg,self.deja,"environnemental")
        if self.w_name == "normal":
            microcosme("normal",5,self.msg,self.deja,"normal")
        if self.w_name == "light":
            microcosme("light",10,self.msg,self.deja,"lumineux")
        if self.w_name == "vampire":
            microcosme("vampire",10,self.msg,self.deja,"vampirique")
        if self.w_name == "elec":
            microcosme("elec",10,self.msg,self.deja,"électrique")
        if self.w_name == "fire":
            microcosme("fire",10,data["world_fire_intro"],self.deja,"")
        
        self.already_went+=1        

water = world("water")      #0
stone = world("stone")      #1
dark = world("dark")        #2
steel = world("steel")      #3
ice = world("ice")          #4
tree = world("tree")        #5
normal = world("normal")    #6
light = world("light")      #7
vampire = world("vampire")  #8
elec = world("elec")        #9
fire = world("fire")        #10

for i in range(len(list_worlds)):
    list_worlds[i] = globals()[list_worlds[i]] #will be filled with all worlds, in the right order
