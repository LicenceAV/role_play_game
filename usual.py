#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2020 Tristan Nerson <tristan.nerson.etu@univ-lemans.fr>          #
# Creation Date: Thursday, April 16th 2020, 2:37:58 pm                         #
# -----                                                                        #
# 'usual.py' is part of the project 'elyscaper_game'.                          #
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
"""This module is created to write centered texts, and to add features
that facilitate the printing of strings, like colors and a colored table.
"""

import os
import time
import textwrap

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

def screen():
    """Get the size of the terminal
    
    Returns:
        int*2 -- l is the number of lines, c is the number of columns
    """
    l = os.get_terminal_size().lines
    c = os.get_terminal_size().columns
    return l, c

class Writer:
    """The core of the module
    """
    def __init__(self, size=60):
        """Initialisation

        Keyword Arguments:
            size {int} -- the minimum number of columns to show the text (default: {60})
        """
        self.size = size
        self.l, self.c = screen()
        self.size_condition()
    
    def color_choice(self,multiplication):
        """A function that will print the formated string, with a multiplicating factor due to 
        the space taken by ANSI escape codes

        Arguments:
            multiplication {float} -- a float that we have to add to adjust the width of the
            paragraph: we find the good argument depdning on the number of chararacters
            of the ANSI escape code by testing many floats
        """
        div = " "*int(round(self.c/5))
        print("{:^{}}".format(textwrap.TextWrapper(width=int(round(multiplication*self.c)),
                                                   subsequent_indent=END+div,
                                                   initial_indent=div).fill(self.msg),self.c)+END)
            
    
    def text(self, msg, color=END):
        """Write a text that will be centered, with a specified color

        Arguments:
            msg {str} -- the message to print

        Keyword Arguments:
            color {str} -- an ANSI escape code as created in this module (default: {END})
        """
        self.msg = msg
        if len(self.msg) >= 3/5*self.c:
            if color != END:
                msg2 = self.msg
                self.msg = ""
                for i in range(len(msg2)):
                    self.msg+=color+msg2[i] 
                if color in [BOLD,FAINT,ITALIC,UNDERLINE,BLINK,NEGATIVE,CROSSED]:
                    self.color_choice(62.7/20)
                else:
                    self.color_choice(48.5/10)
            else:
                self.color_choice(4/5)
        else:
            print("{:^{}}".format(color+msg+END, self.c))

    def size_condition(self):
        """Check that the screen is large enough:
        Wait till the screen is larger
        """
        if self.c <= self.size:
            self.clear()
            self.text("Merci d'élargir la fenêtre du jeu !")
            self.end()
        while self.c < self.size:
            self.c=os.get_terminal_size().columns
            if self.c >= self.size:
                time.sleep(0.4)
                self.clear()
                self.text("C'est bon ! Chargement dans 5 secondes !")
                self.end(2)
                time.sleep(5)
                self.l,self.c = screen()

    def clear(self):
        """Clear terminal
        """
        _ = os.system('clear')
        print("\n"*self.l)


    def jump(self,nb=1):
        """Jump lines
        
        Keyword Arguments:
            nb {int} -- number of lines (default: {1})
        """
        print('\n'*nb)
    
    def usr_input(self):
        """Go to next step by inputing someting
        """
        ans = input("Appuyez sur (↵) pour continuer...")
        
    def end(self, div=3):
        """Go to thw bottom of the terminal
        
        Keyword Arguments:
            div {float} -- number of division of the screen raws you may 
            jump to go to the bottom of the terminal (a huge number is for 
            a huge paragraphe, 2 is for a one-raw paragraph) (default: {3})
        """
        print("\n"*int(round(self.l/div)))
    
    def para_input(self,msg):
        """Input a paragraph that will disappear with a user input
        
        Arguments:
            msg {str} -- the paragraph
        """
        self.l, self.c = screen()
        self.size_condition()
        self.text(msg)
        self.end()
        self.usr_input()
        self.clear()

    def para_time(self,msg,time_secondes=2):
        """Input a paragraph that will disappear with time
        
        Arguments:
            msg {str} -- the paragraph
        
        Keyword Arguments:
            time_secondes {float} -- number of seconds to disappear (default: {2})
        """
        self.l, self.c = screen()
        self.size_condition()
        self.text(msg)
        self.end()
        time.sleep(time_secondes)
        self.clear()
        
    def table(self,stats):
        """Create a colored table

        Note: this table is made for being used with ansi escape codes composed of 10 characters
        We could'nt use the self.text() method, because the table was messed up with it (because
        of the characters of the ANSI escape code). Also, your must use one color per cell!
        
        Arguments:
            stats {list} -- the content : each cell must be a str
        """
        self.stats = stats
        margin = int(round((self.c-79)/2))*" "
        print(margin+79*"-")
        print(margin+"|{:^38}|{:^38}|".format(stats[0][0],stats[0][1]))
        print(margin+79*"-")
        for i in range(len(stats[1:][:])):
            print(margin+""*4+"|   {:^38}\033[0m    |    {:^38}\033[0m   |".format(stats[i+1][0],
                                                                                   stats[i+1][1]))
        print(margin+79*"-")



      
