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
