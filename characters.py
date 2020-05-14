#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2020 Tristan Nerson <tristan.nerson.etu@univ-lemans.fr>          #
# Creation Date: Wednesday, March 11th 2020, 8:54:48 pm                        #
# -----                                                                        #
# 'characters.py' is part of the project 'elyscaper_game'.                     #
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

class perso:
    
    def __init__(self,name,desc,world,power,dext,speed,stamina,life):
        
        self.name = name
        self.desc = desc
        self.world = world
        self.power = power
        self.dext = dext
        self.speed = speed
        self.stamina = stamina
        self.life = life
        self.full_life = life 

        self.dead = False
    
# --------------------------------------------- steel -------------------------------------------- #

golem_fer = perso("Golem de Fer","un golem de fer extrêmement lourd","steel",90,20,20,100,85)
hippogriffe_metal = perso("Hippogriffe métallique","un hippogriffe aux ailes métalliques","steel",30,100,100,70,75)
dragon_electrum = perso("Dragon d'électrum","un terrifiant dragon d'électrum, un alliage antique d'or et d'argent","steel",100,100,80,100,100)

# --------------------------------------------- water -------------------------------------------- #

kraken = perso("Kraken hadal","un kraken hadal aux vingt mille tentacules","water",80,80,80,60,100)
cheval_aqua = perso("Cheval aquatique","un cheval-aquatique humanoïde au charisme fou","eau",80,50,70,60,60)
soldat_requin = perso("Soldat-requin féroce","un soldat-requin qui utilise sa nageoire dorsale comme les meilleurs sabres de Hattori Hanzō","water",80,40,70,100,85)
leviathan = perso("Léviathan gargantuesque","un léviathan gargantuesque qui plonge ses proies dans les eau profondes pour les torturer","water",100,100,60,80,100)

# ------------------------------------------ electricity ----------------------------------------- #

kobold = perso("Kobold foudroyant","un kobold qui peut manier la foudre avec précision","elec",30,70,75,30,20)
oiseau_tonerre = perso("Oiseau-tonerre majestueux","un majestueux oiseau-tonerre capable de déchainer sa puissance électrostatique","elec",93,80,65,30,100)
raiju_elec = perso("Raiju électrique","un raiju surpuissant qui crée des champs électriques incroyablement puissants","elec",100,100,100,30,30)

# --------------------------------------------- fire --------------------------------------------- #

phenix = perso("Phénix fougueux","un phénix qui est à défaut d'être immortel, possède un désir de vie lui permettant d'être particulièrement vigoureux","fire",80,80,80,20,20)
haetae = perso("Haetae ardent","un haetae qui flambe d'un brasier ardent","fire",40,100,100,20,100)
cerbere = perso("Cerbère igné","un cerbère igné qui puise sa puissance des tréfonds du Styx","fire",100,100,100,100,100)

# ---------------------------------------------- ice --------------------------------------------- #

geant_glace = perso("Géant de glace","un immense géant de glace","ice",80,50,20,90,90)
yeti = perso("Yéti algide","un imposant yéti algide qui semble frigorifier tout ce qui l'entoure","ice",70,55,30,70,70)
djinn_glace = perso("Djinn glacé","un djinn glacé qui est capable de congeler le cerveau de ses proies de l'intérieur","ice",100,80,90,50,50)

# --------------------------------------------- light -------------------------------------------- #

chupacabra = perso("Chupacabra iridescent","un soyeux chupacabra au corps nacré","light",30,100,100,20,50)
pegase = perso("Pégase stellaire","un pégase doté d'ailes permettant de voler jusqu'aux étoiles","light",50,100,100,25,100)
manticore = perso("Manticore de lumière","une manticore qui brille de mille feux","light",75,75,75,80,80)

# -------------------------------------------- normal -------------------------------------------- #

centaure = perso("Centaure enragé","un centaure enragé, aux sabots écrasants","normal",60,60,70,60,80)
minotaure = perso("Minotaure effréné","un minotaure effréné qui beugle pour effrayer ses ennemis","normal",100,30,50,100,100)
succube = perso("Succube enivrant","un succube enivrant, qui prend la forme d'une femme callipyge pour profiter pleinement des la majorité des individus la rencontrant","normal",20,100,100,100,100)

# --------------------------------------------- stone -------------------------------------------- #

gargouille = perso("Gargouille minérale","une gargouille minérale, qui a effrayée des générations d'humains","stone",60,70,76,20,50)
gnoll_rocs = perso("Gnoll des rocs","un gnoll des rocs, ayant vécu des millénaires au fond d'une grotte calcaire","stone",70,40,40,95,95)
berserker_pierre = perso("Berserker de pierre","un berserker de pierre capable de briser des montagnes","stone",100,30,30,100,100)
gorgone = perso("Gorgone de métamorphose","une des trois célèbres gorgones, capables de transformer leurs ennemis en pierre à jamais","stone",60,100,100,60,50)

# --------------------------------------------- tree --------------------------------------------- #

dryade = perso("Dryade de la forêt","une dryade de la forêt qui trouve sa puissance phénoménale dans les racines des chênes","tree",60,80,80,40,40)
liechi = perso("Liechi sylvestre","un liéchi gardien des forêts","tree",70,70,70,70,70)
ent = perso("Ent ancestral","un vieil et puissant ent, arbre ambulant dont la ramure semble infinie","tree",100,30,30,100,100)

# --------------------------------------------- dark --------------------------------------------- #

esprit_racune = perso("Esprit rancunier","un esprit spectral qui ronge ses proies par la culpabilité","dark",20,100,100,50,40)
chamane_demon = perso("Chamane démoniaque","un étrange chamane qui semble possédé par des démons","dark",50,60,60,30,30)
croque_mitaine = perso("Croque-mitaine maléfique","un croque-mitaine maléfique qui est absolument effrayant","dark",60,70,60,90,100)
naga = perso("Naga enténébré","un naga qui rampe aussi vite que se propage autour de ses proies son aura ténébreux","dark",75,100,100,40,95)

# -------------------------------------------- vampire ------------------------------------------- #

vampire_assoife = perso("Vampire assoiffé","un vampire assoiffé qui n'hésite pas à aspirer le sang des personnes qui croisent son chemin","vampire",70,85,85,40,40)
poupee_vampire = perso("Poupée vampire","une poupée-vampire qui tentera de vous amadouer grâce à sa mignonnerie avant simplement de vous transperser la gorge","vampire",30,100,70,30,100)
ange_vampire = perso("Ange-vampire","un ange-vampire terrifiant qui utilise ses sombres ailes pour voler d'humain en humain","vampire",90,100,100,40,90)

# Eau > Pierre > Ténèbres > Acier > Glace > Plante > Normal > Lumière > Vampire > Electricité > Feu 

list_characters = [globals()[i] for i in dir() if i not in ('__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__','perso')]
# a list filled with all characters --> we don't have type all characters one by one!
