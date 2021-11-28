# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:10:34 2021
Python Pets 
@author: louis
"""
#variables
status = 1

#Importing classes
from petsclasses import *
#main loop
print ('For help enter the command help.')

pet1=pet()
pet1.startpet()
currentpet=pet1

while status == 1:
    game=command()
    requestcommand = game.request(currentpet)
    triggercommand = game.trigger(requestcommand)

#This code will later be used to create a new pet
#pet2=pet()          
#pet2.copypet(pet1)

