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

def proj9_3():
    print()
    print("This is a roulette program for $1 bets")
    numSpins = eval(input("Enter the number of spins: "))
    red = 0
    black = 0
    green = 0
    total = 0

    for i in range(numSpins):
        randNum = randrange(0, 38)
        if randNum >= 0 and randNum <= 17:
            red += 1
            total += 2
        elif randNum >= 18 and randNum <= 35:
            black += 1
            total += 2
        else:
            green += 1
            total += 35

    print("The results were: {0} greens, {1} reds, and {2} blacks".format(green, red, black))

proj9_3()
