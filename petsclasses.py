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
class pet:
    def __init__(self):
        self.name="Bob"
        self.food=0
        self.clean=0
        self.fun=0
        self.love=0
        
    def startpet(self):
        pet = input('What would you like to name your pet?\n')
        print('Your pet is called',pet)
        #self.name = pet1 This line causes error int has no attribute name
        self.food = 5
        self.clean = 5
        self.fun = 5
        self.love = 5
        return self
    
    #starts an new pet which is the same as copypet
    def copypet(self,copypet):
        pet = input('What would you like to name your pet?\n')
        print('Your pet is called',pet)
        #self.name = pet1 This line causes error int has no attribute name
        self.food = copypet.food
        self.clean = copypet.clean
        self.fun = copypet.fun
        self.love = copypet.love
        return self

#Class that deals with commands
class command:
    def __init__(self):
        self.command="help" 
        
    #get command from user            
    def request(self):
        #print('command requested')
        self.command=input()
        return self.command
        
    #trigger an action        
    def check(self,command):
        event=0
        if self.command == 'help':
            help=1
            print('help')
        return event
        