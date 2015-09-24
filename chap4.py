#Rehaan Advani
#Chapter 4 Programming Assignments
#Period 2

import _tkinter
from graphics import *

def proj4_1():
    window = GraphWin('Checkerboard', 400, 400)
    window.setCoords(-0.5, -0.5, 8.5, 8.5)

    rect1 = Rectangle(Point(-0.5, -0.5), Point(8.5, 8.5))
    rect1.setFill(color_rgb(165, 42, 42))
    rect1.draw(window)
    
    for i in range(0, 8):
        rect = Rectangle(Point(i, i), Point(i+1, i+1))
        rect.setFill('red')
        rect.draw(window)

    dec = 0

    for i in range(8, 0, -1):
        dec += 1
        rect = Rectangle(Point(abs(i-8), i), Point(dec, i-1))
        rect.setFill('black')
        rect.draw(window)

    for i in range(2, 0, -1):
        x2 = 0
        if i == 2:
            x2 = 1
        if i == 1:
            x2 = 2
        
        rect = Rectangle(Point(abs(i-2), i), Point(x2, i-1))
        rect.setFill('black')
        rect.draw(window)

        for i in range(3, 1, -1):
            if i == 3:
                rect = Rectangle(Point(i-3, i), Point(i-2, i-1))
                rect.setFill('red')
                rect.draw(window)
            else:
                rect2 = Rectangle(Point(i, i-2), Point(i+1, i-1))
                rect2.setFill('red')
                rect2.draw(window)

        for i in range(4, 0, -1):
            x2 = 0
            y2 = 0
            if i == 4:
                x2 = 1
                y2 = 4
            if i == 3:
                x2 = 2
                y2 = 3
            if i == 2:
                x2 = 3
                y2 = 2
            if i == 1:
                x2 = 4
                y2 = 1
            
            rect = Rectangle(Point(abs(i-4), abs(i-1)), Point(x2, y2))
            rect.setFill('black')
            rect.draw(window)

        for i in range(5, 0, -1):
            rect = Rectangle(Point(abs(i-5), abs(i-1)), Point(abs(6-i), i))
            rect.setFill('red')
            rect.draw(window)

        for i in range(6, 0, -1):
            rect = Rectangle(Point(abs(i-6), abs(i-1)), Point(abs(7-i), i))
            rect.setFill('black')
            rect.draw(window)

        for i in range(7, 0, -1):
            rect = Rectangle(Point(abs(i-7), abs(i-1)), Point(abs(8-i), i))
            rect.setFill('red')
            rect.draw(window)

        for i in range(8, 1, -1):
            rect = Rectangle(Point(abs(i-9), abs(i-1)), Point(abs(10-i), i))
            rect.setFill('red')
            rect.draw(window)

        for i in range(8, 2, -1):
            blackRect = Rectangle(Point(abs(i-10), abs(i-1)), Point(abs(11-i), i))
            blackRect.setFill('black')
            blackRect.draw(window)

        for i in range(8, 3, -1):
            rect = Rectangle(Point(abs(i-11), abs(i-1)), Point(abs(12-i), i))
            rect.setFill('red')
            rect.draw(window)

        for i in range(8, 4, -1):
            rect = Rectangle(Point(abs(i-12), abs(i-1)), Point(abs(13-i), i))
            rect.setFill('black')
            rect.draw(window)

        for i in range(8, 5, -1):
            rect = Rectangle(Point(abs(i-13), abs(i-1)), Point(abs(14-i), i))
            rect.setFill('red')
            rect.draw(window)

        for i in range(8, 6, -1):
            rect = Rectangle(Point(abs(i-14), abs(i-1)), Point(abs(15-i), i))
            rect.setFill('black')
            rect.draw(window)
                                            
    #Vertical Lines
    borderLine = Line(Point(0,0), Point(0,8))
    borderLine.setOutline("red")
    borderLine.draw(window)
    Line(Point(1,0), Point(1,8)).draw(window)
    Line(Point(2,0), Point(2,8)).draw(window)
    Line(Point(3,0), Point(3,8)).draw(window)
    Line(Point(4,0), Point(4,8)).draw(window)
    Line(Point(5,0), Point(5,8)).draw(window)
    Line(Point(6,0), Point(6,8)).draw(window)
    Line(Point(7,0), Point(7,8)).draw(window)
    Line(Point(8,0), Point(8,8)).draw(window)

    #Horizontal Lines
    Line(Point(0,0), Point(8,0)).draw(window)
    Line(Point(0,1), Point(8,1)).draw(window)
    Line(Point(0,2), Point(8,2)).draw(window)
    Line(Point(0,3), Point(8,3)).draw(window)
    Line(Point(0,4), Point(8,4)).draw(window)
    Line(Point(0,5), Point(8,5)).draw(window)
    Line(Point(0,6), Point(8,6)).draw(window)
    Line(Point(0,7), Point(8,7)).draw(window)
    Line(Point(0,8), Point(8,8)).draw(window)
proj4_1()

def proj4_2():
    window = GraphWin('Halloween Scene', 400, 400)
    window.setCoords(0,0,10,10)

    face = Oval(Point(1.5, 3.5), Point(4.5, 5.5))
    face.setFill('green')
    face.draw(window)

    eye1 = Oval(Point(2, 4.5), Point(2.5, 5))
    eye1.setFill('yellow')
    eye1.draw(window)
    eye2 = eye1.clone()

    eye2.move(1.5,0)
    eye2.draw(window)

    hat = Polygon(Point(3,8), Point(4,6), Point(2,6))
    hat.setFill('black')
    hat.draw(window)

    oval = Oval(Point(1.5,5.2), Point(4.5,6.2))
    oval.setFill('black')
    oval.draw(window)

    mouth = Oval(Point(2.5, 3.75), Point(3.5, 3.75))
    mouth.setFill('black')
    mouth.setOutline('black')
    mouth.draw(window)
    
    nose = Oval(Point(2.75,3.5), Point(3.25,4.75))
    nose.setFill("green")
    nose.draw(window)
    
proj4_2()
    
