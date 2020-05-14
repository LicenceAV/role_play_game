#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2020 Tristan Nerson <tristan.nerson.etu@univ-lemans.fr>          #
# Creation Date: Wednesday, April 15th 2020, 4:30:50 pm                        #
# -----                                                                        #
# 'ascii_img.py' is part of the project 'elyscaper_game'.                      #
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
"""This file is used to convert a jpeg image into an ASCII code.

Note: I put everything in a class because we could have plenty of other methods
inside the class AsciiConverter(). In fact, I didn't put any other type of coloration
in the class because in elyscaper_game I just had to convert images in color, using
the colorated ascii characters. 
"""


import numpy as np 
from PIL import Image 

import usual


class AsciiConverter:
    """Converts a jpeg image into an ASCII code
    """

    def __init__(self, l=30 , c=30):     
        """Initialisation
        
        Arguments:
            l {int} -- number of rows
            c {int} -- number of columns
        """
        self.l = l
        self.c = c
    
    def rgb2single(self,nom_img):
        """Converts colored pixels into b/w pixels: values of RGB correspond to a certain luminance.
        
        Arguments:
            nom_img {str} -- name of the .jpg image
        """

        self.nom_img = nom_img
        img = Image.open(self.nom_img)
        img.thumbnail((self.l,self.c), Image.ANTIALIAS)
        self.image = np.array(img)

        self.lumi = np.empty([self.l,self.c])
        self.R = np.empty([self.l, self.c])
        self.G = np.empty([self.l, self.c])
        self.B = np.empty([self.l, self.c])
        for i in range(self.l):
            for j in range(self.c):
                self.R[i][j] = self.image[i][j][0] # red values  
                self.G[i][j] = self.image[i][j][1] # green values
                self.B[i][j] = self.image[i][j][2] # blue values
        self.lumi = 1/255*(0.2126*self.R+0.7152*self.G+0.0722*self.B) # luminance values


    def to_ascii_color(self,nom_img):
        """Print colored ASCII characters to recreate an image. It centers the image in the screen
        
        Arguments:
            nom_img {str} -- name of the .jpg image
        """
        
        self.rgb2single(nom_img)
        self.new = """"""
        self.standard_scale = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`   """
        #I decided to put nothing at the end of the standard_scale to 
        #avoid white wallpapers that are not understood as white ones
        self.usual_l,self.usual_c = usual.screen()
        writer = usual.Writer()
        writer.size_condition()
        for i in range(self.l):
            for j in range(self.c):
                # We match the pourcentage of luminance with an ASCII character
                self.indice = (self.lumi[i][j])*(len(self.standard_scale)) 
                # We match the pourcentage of RGB with the color
                if 140 <= self.R[i][j] <= 255 and self.G[i][j] <= 150 and self.B[i][j] <= 50: # red
                    self.v = '\033[31m'+self.standard_scale[int(round(self.indice-1))]+'\033[0m'
                
                elif self.R[i][j] <= 170 and self.G[i][j] >= 120 and self.B[i][j] <= 160: # green
                    self.v = '\033[32m'+self.standard_scale[int(round(self.indice-1))]+'\033[0m'

                elif self.R[i][j] >= 100 and self.G[i][j] >= 100 and self.B[i][j] <= 120: # yellow
                    self.v = '\033[33m'+self.standard_scale[int(round(self.indice-1))]+'\033[0m'
                
                elif self.R[i][j] <= 100 and self.G[i][j] <= 150 and self.B[i][j] >= 100: # blue
                    self.v = '\033[34m'+self.standard_scale[int(round(self.indice-1))]+'\033[0m'

                elif self.R[i][j] >= 80 and self.G[i][j] <= 70 and self.B[i][j] >= 80: # purple
                    self.v = "\033[35m"+self.standard_scale[int(round(self.indice-1))]+'\033[0m'
                
                elif self.R[i][j] <= 70 and self.G[i][j] >= 100 and self.B[i][j] >= 100: # cyan
                    self.v = "\033[36m"+self.standard_scale[int(round(self.indice-1))]+'\033[0m'               

                elif 120 >= self.R[i][j] >= 20 and 120 >= self.G[i][j] >= 20 and 120 >= self.B[i][j] >= 20: # grey
                    self.v = "\033[37m"+self.standard_scale[int(round(self.indice-1))]+'\033[0m'

                else:    
                    self.v = self.standard_scale[int(round(self.indice-1))] 
                    # normal color (usualy black or white, but it depends on your terminal)
                
                self.new += self.v+" " 
            self.new += "\n"+int(round((self.usual_c/2-self.c)))*" " 
            # to center the AsciiArt in the screen
        print(self.new)



# ------------------------------------------- __main__ ------------------------------------------- #

if __name__ == '__main__':  
    writer=usual.Writer()
    writer.clear()
    exemple=min(writer.l-10,writer.c-10)     
    ascii=AsciiConverter(exemple,exemple)
    ascii.to_ascii_color("eau.jpg")
    writer.text("Vous vous réveillez dans un microcosme aquatique...")
    writer.end(13)
    #print(writer.l,writer.c)
    #ascii=AsciiConverter(30,30)
    #ascii.to_ascii_color("game_over.jpg")
    
