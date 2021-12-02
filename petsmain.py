# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:10:34 2021
Python Pets 
@author: louis
"""
#variables
status = 1
score = 5
timer = 0

#importing modules
import time
import threading

#Importing classes
from petsclasses import *

petgame=game()
petgame.startgame()

#main loop
petgame=game()
petgame.startgame()
while status == 1:
    print('game loop',timer)
    timer=petgame.gettime()
    commands=command()
    currentpet=petgame.getcurrentpet()
    requestcommand = commands.request(currentpet)
    triggercommand = commands.trigger(requestcommand)
    deplete = currentpet.deplete(timer, score)
    print('status is ',status)

#This code will later be used to create a new pet
#pet2=pet()          
#pet2.copypet(pet1)
