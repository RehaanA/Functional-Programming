#Rehaan Advani
#Chapter 3 Programming Assignments

import math

def proj3_1():
    print("This program will calculate the surface area and volume of a cylinder!")
    r = eval(input("The radius of the cylinder: "))
    h = eval(input("The height of the cylinder: "))
    sa = 2 * math.pi * r * (h+r)
    v = math.pi * r**2 * h
    print("The volume is: ", v,", and the surface area is: ", sa)

def proj3_2():
    print("This is a program that calculates the cost of a catered event")
    numberOfTacos = eval(input("How many tacos did you buy: "))
    numberOfToppings = eval(input("How many toppings did you add: "))
    distance = eval(input("How far away do you live in miles: "))

    tacoCost = 3.75 * numberOfTacos
    toppingCost = 0.50 * numberOfToppings
    deliveryCost = 0.50 * distance + 20

    totalCost = tacoCost + toppingCost + deliveryCost

    print("The total cost of the catered event is ", totalCost, " dollars")

def proj3_3():
    print("This is a program that will calculate the distance between 2 points in a 3 dimensional plane.")
    x1, y1, z1 = eval(input("Write the x, y, and z values of the first point separated by commas in that order: "))
    x2, y2, z2 = eval(input("Write the x, y, and z values of the second point separated by commas in that order: "))

    d = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print("The distance is ", d)

def proj3_4():
    print("This is a program that outputs the value of the epact of a 4-digit year.")
    year = eval(input("A four digit year: "))
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    print("The epact is ", epact, "days")

def proj3_5():
    print("This is a program that will calculate the sum of 5 numbers")
    n1, n2, n3, n4, n5 = eval(input("Input 5 numbers separated by commas: "))
    sum = n1 + n2 + n3 + n4 + n5
    print("The sum of the numbers is:", sum)

def proj3_6():
    print("This is a program that will approximate the value of pi / 4")
    numberOfTerms = eval(input("How many terms should be used for the approximation? "))
    expr = math.pi / 4
    roundedExpr = round(expr, numberOfTerms)
    error = math.pi - roundedExpr
    print("The approximation is: ", roundedExpr)
    print("The error would be: ", error)
proj3_6()


