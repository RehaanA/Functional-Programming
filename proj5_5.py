import _tkinter
from graphics import *

def proj5_5():
    window = GraphWin('Almortization Calculator', 400, 400)
    window.setCoords(0,0,30,30)

    Text(Point(15,28), "This is an almortization calculator program.").draw(window)
    paymentsPerMonth = Entry(Point(5, 25), 10)
    paymentsPerMonth.draw(window)

    Text(Point(15, 25), "How many monthly payments?").draw(window)

    numberOfYears = Entry(Point(5,23), 10)
    numberOfYears.draw(window)

    Text(Point(17.5,23), "How many years for the monthly payments?").draw(window)

    loan = Entry(Point(5, 20), 10)
    loan.draw(window)

    Text(Point(14.5, 20), "The total amount of the loan.").draw(window)

    intRate = Entry(Point(5,18), 10)
    intRate.draw(window)

    Text(Point(15.5, 18), "Monthly interest rate as a decimal.").draw(window)

    numMonthlyPayments = eval(paymentsPerMonth.getText())
    numYears = eval(numberOfYears.getText())
    totalLoan = eval(loan.getText())
    monthlyIntRate = eval(intRate.getText())

    i = monthlyIntRate
    p = totalLoan
    n = numMonthlyPayments * 12 * numYears

    reusableExpr = (1+i)**n
    a = i * p * reusableExpr / reusableExpr - 1

    print(a)

    
    
proj5_5()
