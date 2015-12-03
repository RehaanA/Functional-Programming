#Rehaan Advani
#Chapter 11 Programming Assignments
#Period 2

import math

def proj11_1_a():
    n = eval(input("Enter the size of a square matrix: "))
    matrix = []
    subArray = []
    
    for i in range(n**2):
        val = eval(input("Enter in a value to be placed into the matrix: "))
        matrix.append(val)

        multCheck = mult(n, i)

        if multCheck == True:
            for j in matrix:
                subArray.append(j)
            del matrix[1:]
            matrix.append(subArray)
            del subArray[:]
    print(matrix)

def mult(a, b):
    if b % a == 0:
        return True
    else:
        return False
    
proj11_1_a()
