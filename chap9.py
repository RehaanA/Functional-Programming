#Rehaan Advani
#Chapter 9 Programming Assignments

from random import *

def proj9_1():
    n = eval(input("Enter in the number of darts: "))
    h = 0
    for i in range(n):
        x = 2 * random() - 1
        y = 2 * random() - 1
        if (x**2) + (y**2) <= 1:
            h += 1

    pi = 4 * h / n
    print("The estimation of pi is", pi)
proj9_1()

def proj9_2():
    numCoinFlips = eval(input("Enter in the number of times you want to flip a coin: "))
    
    stepsForward = 0
    stepsBack = 0
    totalSteps = 0
    
    for i in range(numCoinFlips):
        randNum = randrange(0, 2)
        if randNum == 0:
            stepsBack += 1
        else:
            stepsForward += 1

    totalSteps += stepsForward
    totalSteps -= stepsBack

    if totalSteps < 0:
        print("You are {0} steps away from the starting point".format(abs(totalSteps)))
    elif totalSteps == 0:
        print("You are right where you started")
    else:
        print("you are {0} steps away from the starting point".format(totalSteps))
proj9_2()
