# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:10:34 2021
Python Pets 
@author: louis
"""
#variables
game = 1

#Importing classes
from petsclasses import *

#Functions

game=command()
requestcommand = game.request()
checkcommand = game.check(requestcommand)

#main loop
pet1=pet()
pet1.startpet()

#This code will later be used to create a new pet
#pet2=pet()          
#pet2.copypet(pet1)

game.request()
game.check(requestcommand)
