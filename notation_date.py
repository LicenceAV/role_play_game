#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Copyright © 2020 Tristan Nerson <tristan.nerson.etu@univ-lemans.fr>          #
# Creation Date: Sunday, March 8th 2020, 10:14:53 pm                           #
# -----                                                                        #
# 'notation_date.py' is part of the project 'elyscaper_game'.                  #
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
"""This file is used to import the date in other language than english. The main purpose 
is to be able to write in letters the month, which is not possible with time.strftime().
We took here the french Tamriel calendar from The Elder Scrolls:
https://lagbt.wiwiland.net/index.php?title=Calendrier_tamrielien
"""

from datetime import datetime

class notation:
    def __init__(self):
        """Initialisation : use the method conversion()
        """
        self.conversion()
    
    def conversion(self):
        """Creates dates variables
        """
        self.date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.day = self.date_time[0:2]
        self.month = self.date_time[3:5]
        if self.month == "01":
            self.month = "primétoile"
        elif self.month == "02":
            self.month = "clairciel"
        elif self.month == "03":
            self.month = "semailles"
        elif self.month == "04":
            self.month = "ondepluie"
        elif self.month == "05":
            self.month = "plantaisons"
        elif self.month == "06":
            self.month = "mi-l'an"
        elif self.month == "07":
            self.month = "hautzénith"
        elif self.month == "08":
            self.month = "vifazur"
        elif self.month == "09":
            self.month = "âtrefeu"
        elif self.month == "10":
            self.month = "soufflegivre"
        elif self.month == "11":
            self.month = "sombreciel"
        elif self.month == "12":
            self.month = "soirétoile"            
        self.year = self.date_time[6:10]
        self.hour = self.date_time[12:14]
        self.minute = self.date_time[15:17]
        self.second = self.date_time[18:20]


# ------------------------------------------- __main__ ------------------------------------------- #

if __name__ == '__main__':
    
    a = notation()
    print("Le {} de {} {}. Il est exactement {}h {} minutes et {} secondes.".format(a.day,a.month,
                                                                                    a.year,a.hour,
                                                                                    a.minute,a.second))
    
    import time
    print(time.strftime("Le %d %B %Y. Il est exactement %Hh %M minutes et %S secondes."))
    # the month is in english!
