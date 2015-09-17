import _tkinter
from graphics import *

def main():
    win = GraphWin("Tic-Tac-Toe")
    win.setCoords(0.0, 0.0, 3.0, 3.0)
    Line(Point(1,0), Point(1,3)).draw(win)
    Line(Point(2,0), Point(2,3)).draw(win)
    Line(Point(0,1), Point(3,1)).draw(win)
    Line(Point(0,2), Point(3,2)).draw(win)

    for i in range(10):
        p = win.getMouse()
        print("You cliced at:", p.getX(), p.getY())

def shape():
    win = GraphWin("Mystery Shape")
    win.setCoords(0,0,10,10)
    message = Text(Point(5,0.5), "Click three points") #The point is where the text should be located in the coordinate system
    message.draw(win)
    p1 = win.getMouse();p1.draw(win)
    p2 = win.getMouse();p2.draw(win)
    p3 = win.getMouse();p3.draw(win)
    t = Polygon(p1, p2, p3) #Polygon Method
    t.setFill("peachpuff")
    t.setOutline("cyan")
    t.draw(win)

    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

def textInput():
    win = GraphWin('Converter', 400, 300)
    win.setCoords(0,0,3,4)
    Text(Point(1,3), "Celsius Temp:").draw(win)
    Text(Point(1,1), "F Temp:").draw(win)
    input = Entry(Point(2,3),5) #Entry object
    input.setText("0,0"); input.draw(win)
    output = Text(Point(2,1), ""); output.draw(win)
    button = Text(Point(1.5,2.0), "Convert it!"); button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)
    win.getMouse()
    c = eval(input.getText())
    f = 9.0/5.0 * c + 32
    output.setText(f)
    button.setText("Quit")
    win.close()

def animation():
    x,y = 100,100
    win = GraphWin('Animate')
    center = Point(x,y)
    for i in range(91):
        circle = Circle(center, i) #Center and Radius Parameter
        circle.draw(win)
        circle.undraw()
    for i in range(90, -1, -1):
        circle = Circle(center, i)
        circle.setFill('blue')
        circle.draw(win)
        circle.undraw()
animation()
