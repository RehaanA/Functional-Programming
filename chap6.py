#Rehaan Advani
#Chapter 6 Programming Assignments

def right_justify(s):
    print((70-len(s))*' '+s)
right_justify("allen")

def proj6_2():
    colCell = "+----+----+"
    rowCell = "|    |    |"
    print(colCell)
    for i in range(4):
        print(rowCell)
    print(colCell)
    for i in range(4):
        print(rowCell)
    print(colCell)
proj6_2()

#PROBLEM 3

def proj6_4():
    firstTerm = eval(input("Enter the first term of the series: "))
    comRatio = eval(input("Enter the common ratio: "))
    numTerms = eval(input("Enter the number of terms: "))

    expr = 1 - comRatio
    actConv = firstTerm/expr
    estimatedResult = estimate(firstTerm, comRatio, numTerms)
    err = actConv - estimatedResult

    print()
    print("The estimated result is", estimatedResult)
    print()
    print("Actual convergence is", actConv)
    print()
    print("The error is", err)
    print()
    
def estimate(f, c, n):
    initF = f
    resultArray = []
    for i in range(n-1):
        result = f*c
        f = result
        resultArray.append(result)
    finalEstimate = sum(resultArray) + initF

    return finalEstimate
proj6_4()

def calcArea():
    percL, percW = eval(input("Enter the perceived length and width separated by commas: "))
    actL, actW = eval(input("Wnter the actual length and width values separated by commas: "))

    percArea = percL * percW
    actArea = actL * actW
    percError = percentError(percArea, actArea)

    print()
    print("The perceived area is", percArea)
    print()
    print("The actual area is", actArea)
    print()
    print("The percent error is", percError, 9"%")
    print()

def percentError(p, a):

    diff = abs(p - a)
    decimal = diff / a
    perc = decimal * 100
    return perc
    
calcArea()
