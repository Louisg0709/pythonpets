# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:10:34 2021
Python Pets 
@author: louis
"""
#Importing classes
from petsclasses import *

#mainloop
petgame=game()
#playgame(petgame)
petgame.playgame()
currentpet=petgame.allpets.getpeti(0)
petgame.currentpet=currentpet


