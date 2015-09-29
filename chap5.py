#Rehaan Advani
#Chapter 5 Programming Assignments

def proj5_1():
    print("This is a program that calculates a student's letter grade based on a quiz score")
    quizScore = eval(input("Type in the student's score: "))
    gradeList = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
    print(gradeList[abs(quizScore - 13)])
proj5_1()
