#Rehaan Advani
#Chapter 5 Programming Assignments

def proj5_1():
    print("This is a program that calculates a student's letter grade based on a quiz score.")
    quizScore = eval(input("Type in the student's score: "))
    gradeList = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
    print(gradeList[abs(quizScore - 13)])
proj5_1()

def proj5_2():
    print("This is a program that calculates a student's letter grade on an exam at Paly.")
    examScore = eval(input("Type in the students exam score: "))

    if examScore >= 88 and examScore <= 100:
        print("A")
    if examScore >= 77 and examScore <= 87:
        print("B")
    if examScore >= 66 and examScore <= 76:
        print("C")
    if examScore >= 55 and examScore <= 65:
        print("D")
    if examScore >= 0 and examScore <= 54:
        print("F")
proj5_2()

def proj5_3():
    print("This is an acronym program!")
    phrase = input("Type in your phrase here: ")
    
    phrase1 = phrase.replace("of", "").replace("and", "").replace("the", "") 

    for x in phrase1.split():
        outputList = []
        outputList.append(x[0].capitalize())

        for y in outputList:
            print(y, end = "")
proj5_3()

def proj5_4():
    file = input("enter your file: ")
    myFile = open(file, "r")

    characterArray = []

    for word in myFile:
        print("There are", len(word.split()), "words.")
        words = word.split()

        for char in words:
            for i in char:
                characterArray.append(i)

    print("There are", len(characterArray), "characters.")

    lines = myFile.readlines()
    print("There are", len(lines) + 1, "lines.")                     
proj5_4()

def proj5_5():
    print("This is an almortization calculator program!")
    numMonthlyPayments = eval(input("Enter the number of monthly payments: "))
    numYears = eval(input("Number of years: "))
    
    n = numMonthlyPayments * 12 * numYears

    print("Now we are going to determine the monthly payment.")
    print()

    p = eval(input("Enter the loan's initial amount: "))
    i = eval(input("Enter the monthly interest rate as a decimal: "))

    reusableExpr = 1+i
    a = i * p * reusableExpr**n / reusableExpr**n - 1

    totalCost = n * a
    interest = totalCost - p


    for i in range(n):
        x = p * i
        y = a - x
        z = p - y
        print(str(i + 1) + "|" + str(a) + "|" + str(y) + "|" + str(x) + "|" + str(z) + "|")
    
proj5_5()

