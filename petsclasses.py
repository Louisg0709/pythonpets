# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:12:38 2021
Python Pets classes
@author: louis
"""
import time
import threading

#Main game class
class game:
    def runcycle(self, timer):
        time.sleep(1)
        timer = timer+1
        print(timer)
        
    def __init__(self):
        self.status=1
        self.timer=0
        self.allpets=zoo()
        self.score=100
        self.currentpet=None
        return None
    def gettime(self):
        return self.timer
    def getcurrentpet(self):
        return  self.currentpet
    
    #cycle loop
    def cycleloop(self):
        ntimer=0
        while True:
            #ntimer=self.runcycle(ntimer)
            #self.timer=ntimer
            ntimer=ntimer+1
            print('cycleloop',ntimer)
            time.sleep(5)
            
    
    def startgame(self):
        print ('For help enter the command help.')
        pet1=pet()
        pet1.startpet()
        self.currentpet=pet1
        self.allpets.addpet(pet1)
        cycleloopt = threading.Thread(target=self.cycleloop)
        cycleloopt.start()
        
    
    
#Main class that deals with your pets
class pet:
    def __init__(self):
        self.food = 5
        self.clean = 5
        self.fun = 5
        self.love = 5

        
    def startpet(self):
        self.name = input('What would you like to name your pet?\n')
        print('Your pet is called',self.name)
        self.food = 5
        self.clean = 5
        self.fun = 5
        self.love = 5
        return self
    
    #starts an new pet which is the same as copypet
    def copypet(self,copypet):
        self.name = input('What would you like to name your pet?\n')
        print('Your pet is called',self.name)
        #self.name = pet1 This line causes error int has no attribute name
        self.food = copypet.food
        self.clean = copypet.clean
        self.fun = copypet.fun
        self.love = copypet.love
        return self
    def printstats(self):
        print('Pet stats')
        print('Name:',self.name)
        print('Energy:',self.food)
        print('Happiness:',self.fun)
        print('Cleanliness:',self.clean)
        print('Affection:',self.love)
    def feed(self):
        print('You have fed',self.name,'.')
        self.food = self.food + 6
        if self.food > 10:
            self.food=10
        print(self.name,'now has an energy of',self.food,'.')
    def cleanp(self):
        print('You have cleaned',self.name,'.')
        self.clean = self.clean + 6
        if self.clean > 10:
            self.clean=10
        print(self.name,'now has a cleanliness of',self.clean,'.')
    def play(self):
        print('You have played with',self.name,'.')
        self.fun = self.fun + 6
        if self.fun > 10:
            self.fun=10
        print(self.name,'now has a happiness of',self.fun,'.')
    def hug(self):
        print('You have hugged',self.name,'.')
        self.love = self.love + 6
        if self.love > 10:
            self.love=10
        print(self.name,'now has an affection of',self.love,'.')
    def deplete(self, score, timer):
        
        self.food = self.food - timer + score / 100
        self.clean = self.clean - timer + score / 100
        self.fun = self.fun - timer + score / 100
        self.love = self.love - timer + score / 100
    
        
#Class that deals with commands
class command:
    def __init__(self):
        self.command="help" 
        self.help = 'Python Pets \nTo view the stats of your pet enter the command stats.\nTo increase your pets energy enter the command feed.\nTo increase your pets happiness use the command play.\nTo increase your pets affection use the command hug.\n To increase your pets cleanliness use the command clean.' 
    #get command from user            
    def request(self,currentpet):
        #print('command requested')
        self.command=input()
        self.currentpet=currentpet
        return self.command
        
    #trigger an action        
    def trigger(self,command):
        event=0
        if self.command == 'help':
            print(self.help)
        if self.command == 'stats':
            currentpet=self.currentpet
            currentpet.printstats()
        if self.command == 'feed':
            currentpet=self.currentpet
            currentpet.feed()
        if self.command == 'clean':
            currentpet=self.currentpet
            currentpet.cleanp()
        if self.command == 'play':
            currentpet=self.currentpet
            currentpet.play()
        if self.command == 'hug':
            currentpet=self.currentpet
            currentpet.hug()
        return event
#collection class for pets    
class zoo:
    def __init__(self):
        self.n=0
        self.pets=list()
        
    def addpet(self, pet):
        self.pets.append(pet)
        self.n=len(self.pets)
        
    def getpeti(self,i):
        if i<=self.n:
            pet=self.pets[i]
            return pet
        
    def getpet(self,name):
        for pet in self.pets:
            if name == pet.name:
                return pet
        return None
        