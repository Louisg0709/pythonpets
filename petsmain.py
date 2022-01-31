# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:10:34 2021
Python Pets 
@author: louis
"""




myzoo=[]

#Importing classes
from petsclasses import *
import time


def threadFunc():
    status=1
    for i in range(1000000000):
        time.sleep(2)
        print("threadfunc", i)


# Create a Thread with a function without any arguments
th = threading.Thread(target=threadFunc)


# Start the thread
th.start()
# Print some messages on console
#for i in range(5):
#   print('Hi from Main Thread')
#   time.sleep(1)
# Wait for thread to finish
#th.join()



#mainloop
petgame=game()
#playgame(petgame)
myzoo=petgame.initgame(petgame)


#cycleloopt=threading.Thread(target=threadFunc())
#cycleloopt.setDaemon(True)
#cycleloopt.start()
print("leaving start thread")



print("call play game")
petgame.playgame(petgame)
#currentpet=petgame.allpets.getpeti(0)
#petgame.currentpet=currentpet

print("Game over!")
