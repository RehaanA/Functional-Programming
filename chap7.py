#Rehaan Advani
#Chapter 7 Programming Assignments

def proj7_1():
    s1, s2, s3 = eval(input("Enter the three sides of a triangle separated by commas: "))

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
