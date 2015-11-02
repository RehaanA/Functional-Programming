#Rehaan Advani
#Chapter 7 Programming Assignments

from decimal import *

def proj7_1():
    print()
    print("This program tells the you if you have a right triangle!")
    
    try:
        s1, s2, s3 = eval(input("Enter the three sides of a triangle separated by commas: "))
    except TypeError:
        print("\nOops! Make sure you enter 3 numbers!")
    except SyntaxError:
        print("\nMake sure the numbers are separated by commas!")
    except UnboundLocalError:
        print("\nSomething went wrong!")
    except:
        print("\nSomething went wrong.")


    if s1 > s2 and s1 > s3:
        check = s2**2 + s3**2
        result = s1**2

        if check == result:
            print("You have a right triangle")
        else:
            print("You don't have a right triangle")

    if s2 > s1 and s2 > s3:
        check = s1**2 + s3**2
        result = s2**2

        if check == result:
            print("You have a right triangle")
        else:
            print("You don't have a right triangle")

    if s3 > s1 and s3 > s2:
        check = s1**2 + s2**2
        result = s3**2

        if check == result:
            print("You have a right triangle")
        else:
            print("You don't have a right triangle.")
proj7_1()

def proj7_2():
    print()
    print("This program tests to see whether or not you have a valid triangle.")

    try:
        a, b, c = eval(input("Enter the three lengths of a triangle separated by commas: "))
    except TypeError:
        print("\nMake sure you only enter in numbers!")
    except:
        print("\nOops! Something went wrong.")

    if a + b > c:
        print("You have a valid triangle")
    elif b + c > a:
        print("You have a valid triangle")
    elif c + a > b:
        print("You have a valid triangle")
    else:
        print("You don't have a valid triangle")
    
proj7_2()

def proj7_3():

    try:
        length = eval(input("Enter in the total length of your phone call in minutes: "))
    except:
        print("\nOops, something went wrong.")

    cost = 0

    if length < 2:
        cost = 1.15
        print("The total cost of your call is", cost)
    else:
        addLength = length - 2
        addLengthCost = addLength * 0.5
        totalCost = addLengthCost + 1.15
        print("The total cost of your call is", totalCost)

proj7_3()

def proj7_4():
    print()
    print("This program calculates the letter grade for a given mat exam score.")

    try:
        score = eval(input("Please enter in the math score: "))
    except:
        print("\nOops, something went wrong.")

    if score >= 87.5 and score <= 100:
        print("A")
    elif score >= 76.5 and score <= 87.4:
        print("B")
    elif score >= 65.5 and score <= 76.4:
        print("C")
    elif score >= 54.5 and score <= 65.4:
        print("D")
    else:
        print("F")
proj7_4()

def proj7_5():
    print()

    try:
        numBagLitter = eval(input("Enter in the number of bags of litter: "))
    except:
        print("\nOops, something went wrong.")

    if numBagLitter <= 10:
        portFine = numBagLitter * 10
        totalFine = portFine + 75
        print("Your total fine is", totalFine)
    else:
        portFine = numBagLitter * 10
        portFine2 = 75
        totalFine = portFine + portFine2 + 500
        print("Your total fine is ${0}.".format(totalFine))
proj7_5()

def proj7_6():
    print()

    try:
        start = eval(input("Enter your starting time as a decimal: "))
        end = eval(input("Enter your end time as a decimal: "))
    except:
        print("\nOops, something went wrong.")


def proj7_7():
    print()

    try:
       x, y, z = eval(input("Enter in the dimensions of the prism separated by commas: "))
    except:
        print("\nOops, something went wrong.")

    estVol = x * y * z

    xErr = 0
    yErr = 0
    zErr = 0

    decX = abs(Decimal(str(x)).as_tuple().exponent)
    decY = abs(Decimal(str(y)).as_tuple().exponent)
    decZ = abs(Decimal(str(z)).as_tuple().exponent)

    if decX == 0:
       xErr = 0.5
    if decY == 0:
        yErr = 0.5
    if decZ == 0:
        zErr = 0.5

    minVol = (x-xErr)*(y-yErr)*(z-zErr)
    maxVol = (x+xErr)*(y+yErr)*(z+zErr)

    minMeasured = abs(minVol - estVol) / estVol
    maxMeasured = abs(maxVol - estVol) / estVol

    if minMeasured > maxMeasured:
        print("The greatest possible error is", minMeasured, "%")
    else:
        print("The greatest possible error is", maxMeasured, "%")
    
proj7_7()
    
