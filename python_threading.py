#learning threading in python
#import everthing from the TIME LIBRARAY to use functions that are related to time
#threading means trying to run different functions at the same time but dont interefere with one another
from time import *
from threading import Thread

#while True: 
    #print('My box is Open: ')
    #sleep(5) #waits 5 seconds before another code executes
    #print('My box is Closed: ')
    #sleep(5)
    #print('LED is ON: ')
    #sleep(1)
    #print('LED is OFF: ')
    #sleep(1)

#you can pass data inside the thread, example is a variable that contains an integer for the delay time. use a variable so the delay time is not hard coded

def myBox(delayA): #name the delay function to A and initialize the value inside 
    while True:
        print('My box is OPEN: ')
        sleep(delayA)
        print('My box is CLOSED: ')
        sleep(delayA)
def myLED(delayA):
    while True:
        print('My LED is ON: ')
        sleep(delayA)
        print('My LED is OFF: ')
        sleep(delayA)
delayBox = 5 #the variable name inside the thread method can be different from the variable you will be using
delayLED = 1

#boxThread = Thread(target=myBox) - normal syntax with no arguement
boxThread = Thread(target=myBox, args=(delayBox,)) #syntax for coding a thread and passing an #need the args= when passing an arguement inside 
LEDThread = Thread(target=myLED, args=(delayLED,))
boxThread.daemon = True #need to kill threads when stoping the program
LEDThread.daemon = True
boxThread.start() #start the thread
LEDThread.start()
while True: #for safe threading # you can code anything in this loop and it will not interfere with the threads
    pass
