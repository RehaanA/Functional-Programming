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

