import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    myTurtle.pencolor('green')
    if lineLen > 0:
        myTurtle.fd(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-2)


drawSpiral(myTurtle,100)
myWin.exitonclick()
