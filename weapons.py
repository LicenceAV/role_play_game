#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2020 Tristan Nerson <tristan.nerson.etu@univ-lemans.fr>          #
# Creation Date: Wednesday, March 11th 2020, 8:54:35 pm                        #
# -----                                                                        #
# 'weapons.py' is part of the project 'elyscaper_game'.                        #
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

import random

list_weapons = [] # a list that will be filled with all Weapons

class Weapon: 
    
    def __init__(self,name,desc,classe,command,usure=0): 
        
        self.name = name
        self.desc = desc
        self.classe = classe
        self.force = random.randint(1,50)
        self.command = command
        self.deja = False
        self.most = []
        self.less = []
        self.world = random.choice(["water","stone","dark","steel","ice",
                                    "tree","normal","light","vampire","elec","fire"])
        
        list_weapons.append(self.name)

        if self.classe == "water":
            self.most = ["steel","fire"]
            self.less = ["tree","elec"]
        if self.classe == "stone":
            self.most = ["ice","elec"]
            self.less = ["tree","steel"]
        if self.classe == "dark":
            self.most = ["normal","tree"]
            self.less = ["light","ice"]
        if self.classe == "ice":
            self.most = ["steel","water","tree"]
            self.less = ["stone","dark","fire"]            
        if self.classe == "steel":
            self.most = ["stone"]
            self.less = ["fire","water"]
        if self.classe == "tree":
            self.most = ["water","stone","light"]
            self.less = ["fire","ice","dark"]
        if self.classe == "normal":
            self.most = []
            self.less = [] 
        if self.classe == "light":
            self.most = ["dark"]
            self.less = ["elec"]
        if self.classe == "silver":
            self.most = ["vampire"]
            self.less = ["water"]            
        if self.classe == "elec":
            self.most = ["water","steel"]
            self.less = ["stone","ice","light"]      
        if self.classe == "feu":
            self.most = ["ice","steel","tree"]
            self.less = ["water","fire","elec"]
                    


cimeterre = Weapon("Cimeterre de feu","une cimeterre dont la lame semble être un brasero","fire","cim")
dague = Weapon("Dague des ténèbres","une dague qui dégage un aura de terreur noire","dakr","dag")
nunchaku = Weapon("Nunchaku en argent","un nunchaku en argent qui pourrait repousser certains ennemis","silver","nun")
rapiere = Weapon("Rapière de lumière","une rapière qui brille d'une lueur d'espoir","light","rap")
siangham = Weapon("Siangham aquatique","un siangham qui semble être lié à l'élement aquatique","water","sia")
lance = Weapon("Lance électrique","une lance qui semble projeter de la foudre","elec","lan")
bolas = Weapon("Bolas de pierre","un bolas en pierre qui peut être facilement projeté","stone","bol")
corseque = Weapon("Corsèque fleurie","une corsèque liée fondamentalement à la nature","tree","cor")
fleau = Weapon("Fléau d'armes de glace","un fléau d'armes glacé","ice","fle")
masse = Weapon("Masse en acier","une masse en acier très imposante","steel","mas")
fouet = Weapon("Fouet","un fouet, comme celui d'Indiana Jones","normal","fou")
gourdin = Weapon("Gourdin enflammé","un gourdin qui capable de brûler en plus d'assomer","fire","gou")
faux = Weapon("Faux de guerre ténébreuse","une faux de guerre qui a été utilisée pour de sombres executions","dalr","fau")
hache = Weapon("Hache en argent","une hache d'argent qui ne semble pas plaire à tout le monde","silver","hac")
flamberge = Weapon("Flamberge océanique","une flamberge conçue vingt mille lieues sous les mers","water","fla")
khepesh = Weapon("Khépesh de roc","un khépesh taillé dans la pierre antique","stone","khe")
sabre = Weapon("Sabre maléfique","un sabre maléfique, à l'allure effrayante","dark","sab")
marteau = Weapon("Marteau d'eau","un marteau constitué magiquement d'eau","water","mar")
sai = Weapon("Saï du soleil","un saï solaire, qui éblouit l'énnemi","light","sai")
serpe = Weapon("Serpe luminescente","une serpe qui illumine la vie","light","ser")
glaive = Weapon("Glaive de la forêt","un glaive qui a rattaché à la forêt","tree","gla")
bardiche = Weapon("Bardiche en pierre","une bardiche en pierre qui est très imposante","stone","bar")
scramasaxe = Weapon("Scramasaxe rocailleux","un scramasaxe rocailleux, pour tout trancher","stone","scr")
claymore = Weapon("Claymore en silex","une claymore lourde, fabriquée en silex","stone","cla")
lame = Weapon("Lame de rocher","une lame qui a été longtemps plantée dans un rocher, et s'est calcifiée","stone","lam")

list_weapons = [globals()[i] for i in dir() if i not in ('__annotations__', '__builtins__', 
                                                         '__cached__', '__doc__', '__file__', 
                                                         '__loader__', '__name__', '__package__', 
                                                         '__spec__','inv','list_Weapons','random',
                                                         'Weapon')]
# a list filled with all weapons --> we don't have type all weapons one by one!

