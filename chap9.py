#Rehaan Advani
#Chapter 9 Programming Assignments
#Period 2

from random import *

'''def proj9_1():
    piArray = []
    piSum = 0
    h = 0
    hArray = []
    n = eval(input("Enter in the number of darts: "))
    for i in range(10000):
        x = 2 * random() - 1
        y = 2 * random() - 1
        if x**2 + y**2 <= 1:
            h += 1
            hArray.append(h)
            
        pi = (4 * len(hArray)) / n
        piArray.append(pi)

    for j in (piArray):
        piSum += piArray[j]
    averagePi = piSum / len(piArray)
    print("The estimates pi is", averagePi)
proj9_1()'''

def proj9_1():
    n = eval(input("Enter in the number of darts: "))
    x = 2 * random() - 1
    y = 2 * random() - 1
    h = 0
    for i in range(100000):
        if (x**2) + (y**2) <= 1:
            h += 1

    pi = 4 * h / n
    print(pi)
proj9_1()
