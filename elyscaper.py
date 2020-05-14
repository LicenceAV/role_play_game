#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2020 Tristan Nerson <tristan.nerson.etu@univ-lemans.fr>          #
# Creation Date: Wednesday, March 11th 2020, 7:16:17 pm                        #
# -----                                                                        #
# 'elyscaper.py' is part of the project 'elyscaper_game'.                      #
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
"""This is the main file of a little RPG game. You can also use it as a module, 
a it has plenty of functions, classes and variables (most of them are for the 
usage of weapons, duels or worlds explorations).
"""

# ------------------------------------------------------------------------------------------------ #
import time
import os
import sys
import json
import random as rd
import subprocess
import numpy as np
import usual
import intro_elyscaper
import notation_date
import world

# ------------------------------------------------------------------------------------------------ #
#                                          Initialisation                                          #
# ------------------------------------------------------------------------------------------------ #

with open('elyscaper_data.json') as json_file: # all long sentences are written here
    data = json.load(json_file)
    
writer = usual.Writer()
writer.clear()
intro = intro_elyscaper.Display_intro()
date = notation_date.notation() 

FNULL = open(os.devnull, 'w') # not to see the outputs (stdout and stderr)

def kill_music():
    """If the variable music exists as a shell command, and if it is running, kill it 
    """
    try:
        if music.poll() == None:
            music.kill()
    except NameError:
        pass    
    
def next_music():
    """If the variable music exists as a shell command, and if it is not running, launch music
    """
    try: #it will be only achieved if elyscaper is used as __main__ 
        if globals()["music"].poll() != None: 
            music_number = rd.randint(2,9)
            music_name = "musics/Ofdream_{}.mp3".format(music_number)
            global music #not dangerous to use it here because used when __name__ = "__main__"
            music = subprocess.Popen(["mpg123", music_name], stdout=FNULL, 
                                     stderr=subprocess.STDOUT)            
    except KeyError: #it will be the case if elyscaper is not used as __main__
        pass 
    

# ------------------------------------------------------------------------------------------------ #
#                                            Create hero                                           #
# ------------------------------------------------------------------------------------------------ #

inv = [] # the inventary

class Hero:
    """To generate the hero
    """
    
    def __init__(self):
        """Initialisation
        """
        self.dead = False
        self.know = []
        
        writer.clear()
        writer.text("Nom du joueur ? ")
        writer.end()
        self.name = input("")
        writer.clear()

    def level(self):
        """Select the difficulty of the game
        """
        writer.text(data["level"])
        writer.jump()
        writer.text("- Rêve lucide ? (1)")
        writer.jump()
        writer.text("- Rêve ? (2)")
        writer.jump()
        writer.text("- Cauchemard ? (3)")
        writer.jump()
        writer.text("- Terreur nocturne ? (4)")
        writer.end(4.5)
        _ = input("")
        writer.clear()
        if _ == "1":
            self.conditions(100,100,100,100,120,10,data["level_choice"][0])
        elif _ == "2":
            self.conditions(90,90,90,90,110,7,data["level_choice"][1])
        elif _ == "3":
            self.conditions(80,80,80,80,100,4,data["level_choice"][2])
        elif _ == "4":
            self.conditions(70,70,70,70,90,0,data["level_choice"][3])
        else:
            self.level()
                    
    def conditions(self,power,dext,speed,stamina,life,joker,msg):
        """Creates important varibales related to hero

        Arguments:
            power {int} -- the power of hero
            dext {int} -- the dexterity of the hero (ability not to mess up his strikes)
            speed {int} -- the speed of the hero (to be the first to strike)
            stamina {int} -- the stamina of the hero (to be able to take the hit)
            life {int} -- the life bar of the hero
            joker {int} -- the number of time the hero can flee
            msg {str} -- the message to show depending on the difficulty
        """
        self.power = power
        self.dext = dext
        self.speed = speed
        self.stamina = stamina
        self.life = life
        self.joker = joker
        self.full_life = life 
        writer.para_input(msg)
            

# ------------------------------------------------------------------------------------------------ #
#                                             Fighting                                             #
# ------------------------------------------------------------------------------------------------ #
class Battle:
    """A class designed fo duels bitween hero and foe
    """

    def __init__(self,hero,foe):
        """Initialisation

        Arguments:
            hero {Hero obj} -- the hero 
            foe {characters.Ennemy obj} -- the foe
        """
        self.hero = hero
        self.foe = foe
        
    def green_red(self,hero_skill,foe_skill):
        """Print things in red or green depending on the highest values

        Arguments:
            hero_skill {int} -- the skill of the hero
            foe_skill {int} -- the skill of the foe

        Returns:
            str*2 -- the colored strings of the skills
        """
        if hero_skill < foe_skill:
            str_hero = usual.RED+str(hero_skill)
            str_foe = usual.GREEN+str(foe_skill)
        elif hero_skill > foe_skill:
            str_foe = usual.RED+str(foe_skill)
            str_hero = usual.GREEN+str(hero_skill)
        else:
            str_foe = usual.YELLOW+str(foe_skill)
            str_hero = usual.YELLOW+str(hero_skill)
        return str_hero,str_foe
    
    def stats(self):
        """Generates a table representing the stats of hero and foe 
        """    
        str_hero,str_foe = self.green_red(self.hero.life,self.foe.life)             
        content = [[self.hero.name,self.foe.name],
                   ["Vie = {}".format(str_hero),
                    "Vie = {}".format(str_foe)]]
        if "power" in self.hero.know:
            str_hero,str_foe = self.green_red(self.hero.power,self.foe.power)             
            self.green_red(self.hero.power,self.foe.power)    
            content.append(["Puissance = {}".format(str_hero),"Puissance = {}".format(str_foe)])
        if "dext" in self.hero.know:
            str_hero,str_foe = self.green_red(self.hero.dext,self.foe.dext)                        
            self.green_red(self.hero.dext,self.foe.dext)
            content.append(["Agilité = {}".format(str_hero),"Agilité = {}".format(str_foe)])
        if "speed" in self.hero.know:
            str_hero,str_foe = self.green_red(self.hero.speed,self.foe.speed)                        
            self.green_red(self.hero.speed,self.foe.speed)
            content.append(["Vitesse = {}".format(str_hero),"Vitesse = {}".format(str_foe)])
        if "stamina" in self.hero.know:
            str_hero,str_foe = self.green_red(self.hero.stamina,self.foe.stamina)                        
            self.green_red(self.hero.stamina,self.foe.stamina)
            content.append(["Endurance = {}".format(str_hero),"Endurance = {}".format(str_foe)])
        writer.table(content)
        
    def a_battle(self):
        """Show the message of the sight of a creature. 
        Say what to do if you decide to attack or flee.
        """
        writer.clear()
        writer.text(data["see_ennemy"].format(self.foe.desc))       
        self.stats()
        writer.end()
        writer.usr_input()
        choice = self.choice_battle()
        if choice == "attack":
            self.weapon = choose_weapon_fight() # we don't care about w_number
            writer.clear()
            self.round()
        elif choice == "flee":
            writer.clear()
            writer.para_input("Vous décidez de prendre la fuite !")
            self.foe.dead == True
            self.hero.joker -= 1
            
    def choice_battle(self):
        """Decide to attack or to flee

        Returns:
            str -- retrun the decision, "attack" or "flee".
        """
        writer.clear()
        if self.hero.joker != 0:        
            writer.text("Vous pouvez choisir de l'attaquer (A), comme de fuir (F).")
            writer.end()
            _ = input("")
            if _ == "A":
                return "attack"
            elif _ == "F":
                return "flee"
            else:
                self.choice_battle()
        else:
            writer.para_input(data["cant_flee"])   
            return "attack"
                   
    def round(self):
        """Decide who will move the first (depending on the speed of the hero and the foe).
        It does it until death of foe or hero.
        """
        while True:
            if self.foe.dead == True or self.hero.dead == True:
                break    
                      
            rd_move = {self.hero: rd.randint(self.hero.speed,self.hero.speed+self.foe.speed), 
                        self.foe: rd.randint(self.foe.speed,self.hero.speed+self.foe.speed)}
            first_mover = max(rd_move, key=rd_move.get) 
            #if the values are the same, the first mover will be the hero (the key is called first)
            hero_foe = [self.hero,self.foe]
            hero_foe.remove(first_mover)
            for k in hero_foe:
                last_mover = k
                               
            self.fight(first_mover,last_mover)
            if self.foe.dead == True or self.hero.dead == True:
                break 
            self.fight(last_mover,first_mover)
            if self.foe.dead == True or self.hero.dead == True:
                break 
        
    def fight(self,attack,defense):
        """Calculate the strength of the strike, if the strike is not messed up. It depends on 
        the dexterity (.dext), the power (.power) the endurance (.stamina), the weapon and the luck.

        Arguments:
            attack {Hero or characters.Ennemy obj} -- the one that attack
            defense {Heor or characters.Ennemy obj} -- the one that defend
        """
                    
        writer.clear()
        success = rd.randint(1,attack.dext)
        if success <= 5:
            writer.para_input("{} attaque mais le coup est râté !".format(attack.name))
            pass
        else:
            strike = rd.randint(int(round(attack.power/2)),attack.power)
            if attack == self.hero and self.weapon != False:
                if self.weapon.most == defense.world:
                    strike += rd.randint(int(round(self.weapon.force/2)),self.weapon.force)*2
                elif self.weapon.less == defense.world:
                    strike += rd.randint(int(round(self.weapon.force/2)),self.weapon.force)*0.5
                else:
                    strike += rd.randint(int(round(self.weapon.force/2)),self.weapon.force)
            strike -= rd.randint(int(round(defense.stamina/4)),int(round(defense.stamina/2)))
            if strike < 0:
                strike = 0
            defense.life -= strike
            writer.text("{} attaque de {} points".format(attack.name,strike))
            self.stats()
            writer.end()
            writer.usr_input()
            
            if defense.life <= 0:
                if defense == self.foe:
                    self.foe.dead = True
                    writer.clear()
                    writer.para_time("Vous avez affaibli l'ennemi !")
                else:
                    self.hero.dead = True
                    writer.clear()
                    writer.para_time("L'ennemi vous a affaibli !")            


# ------------------------------------------------------------------------------------------------ #
#                                       Traveling the worlds                                       #
# ------------------------------------------------------------------------------------------------ #

def visit_world(hero,w_number):
    """The core of the game's travels
    
    Note: Must have initialised this variable before using: start_chrono = time.time()

    Arguments:
        hero {Hero obj} -- the hero
        w_number {int} -- the number of the world (see world.py's module)
    """    
    
    breakable_core(hero,w_number)
    
    if hero.dead == False:
        next_music()
        switch_world(hero,w_number)

    # if you die in a world:
    elif w_number == 10 and hero.dead == True: # bad end (die in the fire world)
        bad_end()
        
    elif w_number != 10 and hero.dead == True: # die in another world
        next_music()
        writer.clear()
        writer.para_input(data["dead_world"])
        hero.dead = False
        hero.life = hero.full_life
        visit_world(hero,w_number+1)
        
        
def breakable_core(hero,w_number):
    """A loop for all ennemies in a world that breaks (return) if the hero die

    Arguments:
        hero {Hero obj} -- the hero
        w_number {int} -- the number of the world (see world.py)
    """
    world.list_worlds[w_number].intro_world() #launch the intro of the world
    writer.usr_input()
            
    foes = world.list_worlds[w_number].characters_in_world #just rename it, to use it easier
    list_weapons_this_world = world.list_worlds[w_number].weapons_in_world #same as above
    
    order_of_apparition, appear = finding_weapons(foes,list_weapons_this_world)
    
    for i in range(len(foes)):
        battle = Battle(hero,foes[i])
        battle.a_battle()            
        foes[i].dead = False    
        foes[i].life = foes[i].full_life 
        if hero.dead == True:
            return       
        apparition(appear,foes,w_number,i,order_of_apparition)
        
        
def switch_world(hero,w_number): # when you survive in a world
    """Switch bitween worlds when all the ennemis are killed

    Note: made to be used in a visit_world() function.    

    Arguments:
        hero {Hero obj} -- the hero
        w_number {int} -- the number of the world (see world.py's module)
    """
    foes_ameliorations()
        
    if w_number == 0: # good end (survive in water world)
        good_end()

    elif w_number == 10: # if you survive in the fire world
        writer.clear()
        writer.para_input(data["alive_fire_world"])
        visit_world(hero,9)
                
    else: # if you survive in another world   
        writer.clear()
        writer.para_input(data["alive_world"])
        
        writer.text("- Appuyez sur (M) pour monter...")
        writer.jump()
        writer.text("- Appuyez sur (D) pour descendre...")
        writer.end()

        _ = input("")
        
        if _ == "M":
            visit_world(hero,w_number-1)
        elif _ == "D":
            hero_ameliorations(hero)
            visit_world(hero,w_number+1)
        else:
            switch_world(hero,w_number)

def foes_ameliorations():
    plus = 3
    for i in range(len(world.list_worlds)):
        for j in range(len(world.list_worlds[i].characters_in_world)):
            foe = world.list_worlds[i].characters_in_world[j]
            foe.power += plus
            foe.dext += plus
            foe.speed += plus
            foe.stamina += plus
            foe.full_life += plus
            foe.life = foe.full_life


def hero_ameliorations(hero):
    if len(hero.know)<5:
        writer.clear()
        writer.text(data["know"][0])
        writer.jump()
        writer.text(data["just_amelioration".format("sinon")][0])
        writer.end()
        _ = input("")
        if _ == "C":
            know_amelioration(hero)
        elif _ == "A":
            just_amelioration(hero)
        else:
            hero_ameliorations(hero)
    else:
        writer.clear()
        writer.para_input(data["just_amelioration".format("")][0])
        just_amelioration(hero)

def know_amelioration(hero):
    writer.clear()
    writer.text(data["know"][1])
    writer.end()
    _ = input("")
    if _ == "P" and "power" not in hero.know:
        hero.know.append("power")
    elif _ == "A" and "dext" not in hero.know:
        hero.know.append("dext")
    elif _ == "V" and "speed" not in hero.know:
        hero.know.append("speed")
    elif _ == "E" and "stamina" not in hero.know:
        hero.know.append("stamina")
    else:
        know_amelioration(hero)
    
def just_amelioration(hero):
    writer.clear()
    writer.text(data["just_amelioration"][1])
    writer.end()   
    plus = 10
    _ = input("")
    if _ == "P":
        hero.power += plus
    elif _ ==  "A":
        hero.dext += plus
    elif _ == "V":
        hero.speed += plus
    elif _ == "E":
        hero.stamina += plus
    elif _ == "L":
        hero.life += plus
    else:
        just_amelioration(hero)
        
def good_end():
    """Show one the two ends: the good one
    """
    writer.clear()
    end_chrono = time.time()
    writer.para_input(data["date"].format(date.day,date.month,date.year,
                                            date.hour,date.minute,date.second))
    writer.para_input(data["good_end"].format(hero.name,float(end_chrono - start_chrono)))
    writer.clear()
    world.microcosme("win",10,"",0,"")
    credits()
    kill_music()
    sys.exit()

def bad_end():
    """Show one the two ends: the bad one
    """
    next_music()
    end_chrono = time.time()
    writer.para_input(data["date"].format(date.day,date.month,date.year,
                                            date.hour,date.minute,date.second))
    writer.text(data["bad_end"].format(float(end_chrono - start_chrono)))
    writer.end()
    writer.usr_input()
    writer.clear()
    world.microcosme("game_over","",0,"")
    credits()
    kill_music()
    sys.exit()

# ------------------------------------------------------------------------------------------------ #
#                                         Usage of weapons                                         #
# ------------------------------------------------------------------------------------------------ #
            
def apparition(appear,foes,w_number,number_of_this_foe,order_of_apparition):
    if order_of_apparition[number_of_this_foe] == True:
        this_weapon = rd.choice(world.list_worlds[w_number].weapons_in_world)
        writer.clear()
        writer.para_input("Vous trouvez une arme au sol !")
        writer.para_input("Cette arme est {} !".format(this_weapon.desc))
        writer.text(data["add_weapon"])
        if this_weapon.deja == True:
            writer.jump()
            writer.text("Vous l'aviez déjà vu dans ce monde !")
        else:
            this_weapon.deja == True
        writer.end()
        
        _ = input("")
        
        if _ == "A":
            if len(inv) <= 10:
                writer.clear()
                writer.para_input("Vous avez choisi de prendre l'arme !")
                inv.append(this_weapon)
                world.list_worlds[w_number].weapons_in_world.remove(this_weapon)
            else:
                writer.clear()
                writer.text(data["too_many_weapons"])
                writer.jump()
                writer.text(data["throw_weapon"])
                writer.end()
                _ = input("")
                writer.clear
                if _ == "D":
                    choose_weapon_remove(w_number)
                    inv.append(this_weapon)
                    world.list_worlds[w_number].weapons_in_world.remove(this_weapon)
                    writer.para_input(data["replace_weapon"])
                else:
                    writer.clear()
                    writer.para_input("Vous avez choisi de ne pas prendre l'arme...")
                
        else:
            writer.clear()
            writer.para_input("Vous avez choisi de ne pas prendre l'arme...")

def show_inv():
    for i in range(len(inv)):
        writer.text("{} ({})".format(inv[i].name,inv[i].command))

def choose_weapon(msg):
    writer.clear()
    writer.text(msg)
    writer.jump()
    show_inv()
    writer.end()
    _ = input("")
    return _
    
def choose_weapon_remove(w_number):
    if len(inv)>0:
        _ = choose_weapon("Tapez les trois premières lettres de l'arme souahitée")
        for i in range(len(inv)):
            if _ == inv[i-1].command:
                inv.remove(inv[i])
                world.list_worlds[w_number].weapons_in_world.append(inv[i])

def choose_weapon_fight():
    if len(inv)>0:
        _ = choose_weapon("Tapez les trois premières lettres de l'arme souahitée, sinon, passez.")
        for i in range(len(inv)):
            if _ == inv[i-1].command:
                return inv[i-1]
        else:
            return False
    else:
        writer.clear()
        writer.para_time("Vous n'avez pas d'arme !",1)
        return False     
    
def finding_weapons(foes,list_weapons_this_world):
    appear = rd.randint(0,len(foes))
    # randomly select the number of weapons that will be found for this visit of the world 
    if appear > len(list_weapons_this_world): 
        appear = len(list_weapons_this_world) 
        # reajust the number of weapons if there are less weapons that can appear in this world
    
    order_of_apparition = []
    number_weapons_to_distribute = appear
    number_of_foes_to_distribute = len(foes)
    while number_of_foes_to_distribute != 0:
        if number_weapons_to_distribute == number_of_foes_to_distribute:
            order_of_apparition.append(True)
            number_weapons_to_distribute-=1
        else:
            if number_weapons_to_distribute > 0:
                this_action = rd.choice([True,False])
                order_of_apparition.append(this_action)
                if this_action == True:
                    number_weapons_to_distribute-=1
        number_of_foes_to_distribute-=1

    if len(order_of_apparition) < len(foes):
        for i in range(len(foes)-len(order_of_apparition)):
            order_of_apparition.append(False)   
    
    return order_of_apparition, appear

# ------------------------------------------------------------------------------------------------ #
#                                              Credits                                             #
# ------------------------------------------------------------------------------------------------ #

def credits():
    """Create the credits
    """
    writer.text("~ Elyscaper ~")
    intro.point(3,1)
    writer.text("Créé par")
    intro.point(3,1)
    writer.text("Tristan NERSON")
    intro.point(3,1)
    writer.text("Le Mans Université")
    intro.point(3,1)
    writer.text("Merci d'avoir joué !")
    intro.point(3,1)
    writer.text("Playlist utilisée : Øfdream Legacy")
    for i in np.arange(1,40,0.5):
        time.sleep(1/i)
        print("")
    writer.clear()

# ------------------------------------------------------------------------------------------------ #
#                                             __main__                                             #
# ------------------------------------------------------------------------------------------------ #

if __name__ == "__main__":

# -------------------------------------------- No echo ------------------------------------------- #
    # The only part I didn't write: I decided to put the terminal in no echo because it had no echo
    # when music was playing, but the echo could come back when the music stopped inside a level
    # Source: <https://gist.github.com/kgriffs/5726314>
    import termios
    import atexit

    def enable_echo(enable):
        """Control echo mode of terminal

        Arguments:
            enable {Bool} -- Enable or disable echo mode
        """
        fd = sys.stdin.fileno()
        new = termios.tcgetattr(fd)
        if enable:
            new[3] |= termios.ECHO
        else:
            new[3] &= ~termios.ECHO

        termios.tcsetattr(fd, termios.TCSANOW, new)

    atexit.register(enable_echo, True)
    enable_echo(False)
    #End of the part that I didn't write

# -------------------------------------------- Launch -------------------------------------------- #

    music = subprocess.Popen(["mpg123", "musics/Ofdream_1.mp3"], stdout=FNULL, stderr=subprocess.STDOUT)
    writer.para_input(data["intro_warning"])
    writer.para_input(data["write_letters"])    
    writer.clear()
    hero = Hero()
    hero.level()

# --------------------------------------- Generate a matrix -------------------------------------- #
    
    writer.clear()
    writer.size_condition()
    writer.text("Paramétrage du système en cours")
    writer.jump()
    intro.point(6,0.7)
    intro.matrix("              ")
    writer.jump(2)
    writer.text("Initialisation des dimensions")
    writer.jump()
    intro.point(6,0.7)
    intro.matrix("    ")
    writer.clear() 

    writer.para_time("Bonjour {}, votre partie est prête.".format(hero.name))

# --------------------------------------------- Intro -------------------------------------------- #

    intro.menu(hero)
    next_music()
    writer.clear()
    writer.para_input(data["date"].format(date.day,date.month,date.year,date.hour,
                                          date.minute,date.second))
    writer.para_input(data["intro"][0])
    writer.para_input(data["intro"][1])
    writer.para_input(data["intro"][2])
    writer.para_input(data["intro"][3])
    
# ----------------------------------------- Phase of play ---------------------------------------- #

    start_chrono = time.time()
    visit_world(hero,5)
