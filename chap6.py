#Rehaan Advani
#Chapter 6 Programming Assignments

def proj6_1():
    s = input("enter a word or phrase: ")
    formattedStr = right_justify(s)
    print(formattedStr)
    
def right_justify(s):
    format = (70-len(s))*' '+s
    return format
proj6_1()

def proj6_2():
    colCell = "+ - - - - + - - - - +"
    rowCell = "|         |         |"
    print(colCell)
    for i in range(4):
        print(rowCell)
        print()
    print(colCell)
    for i in range(4):
        print(rowCell)
        print()
    print(colCell)
proj6_2()

def proj6_3():
    animal = input("Enter an animal: ")
    str1 = "There was a farmer, had a dog,"
    str2 = "and Bingo was his name-o."
    str3 = "B-I-N-G-O"
    str4 = "(clap)-I-N-G-O"
    str5 = "(clap)-(clap)-N-G-O"
    str6 = "(clap)-(clap)-(clap)-G-O"
    str7 = "(clap)-(clap)-(clap)-(clap)-O"
    str8 = "(clap)-(clap)-(clap)-(clap)-(clap)"

    print()
    print(str1)
    print(str2)
    for i in range(3):
        print(str3)
    print(str2)
    print()
    print(str1)
    print(str2)
    for i in range(3):
        print(str4)
    print(str2)
    print()
    print(str1)
    print(str2)
    for i in range(3):
        print(str5)
    print(str2)
    print()
    print(str1)
    print(str2)
    for i in range(3):
        print(str6)
    print(str2)
    print()
    print(str1)
    print(str2)
    for i in range(3):
        print(str7)
    print(str2)
    print()
    print(str1)
    print(str2)
    for i in range(3):
        print(str8)
    print(str2)
    print()
    
proj6_3()

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
    actL, actW = eval(input("Enter the actual length and width values separated by commas: "))

    percArea = percL * percW
    actArea = actL * actW
    percError = percentError(percArea, actArea)

    print()
    print("The perceived area is", percArea)
    print()
    print("The actual area is", actArea)
    print()
    print("The percent error is", percError, "%")
    print()

def percentError(p, a):

    diff = abs(p - a)
    decimal = diff / a
    perc = decimal * 100
    return perc
calcArea()

