#Rehaan Advani
#Chapter 7 Programming Assignments

def proj7_1():
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

proj7_3()
