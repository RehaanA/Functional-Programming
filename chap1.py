def classWork():
    print("This function illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1-x)
        print(x)

def proj1_4():
    print("This function illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 2.0 * x * (1-x)
        print(x)

def proj1_5():
    print("This function illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print?"))
    for i in range(n):
        x = 2.0 * x * (1-x)
        print(x)

def proj1_6_a():
    print("This function illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x * (1-x)
        print(x)

def proj1_6_b():
    print("This function illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * (x-x*x)
        print(x)

def proj1_6_c():
    print("This function illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9*x-3.9*x*x
        print(x)
proj1_6_c()
