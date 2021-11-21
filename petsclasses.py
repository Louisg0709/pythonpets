# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:12:38 2021
Python Pets classes
@author: louis
"""

#Main game class
class game:
    def __init__(self):
        self.status=1
        return self
#Main class that deals with your pets
#pets will have a energy,happiness,care and clean value.
class pet:
    def __init__(self):
        self.name="Bob"
        
    
    def startpet(self):
        pet1 = input('What would you like to name your pet? ')
        print('Your pet is called',pet1)
        #self.name = pet1 This line causes error int has no attribute name
        pet1food = 5
        pet1clean = 5
        pet1fun = 5
        pet1love = 5
        return self
        