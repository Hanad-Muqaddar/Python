import  turtle
import time
myturtle = turtle.Turtle()

def square():
    myturtle.width(5)
    myturtle.color('blue')
    myturtle.forward(150)
    myturtle.right(90)
    myturtle.forward(150)
    myturtle.right(90)
    myturtle.forward(150)
    myturtle.right(90)
    myturtle.forward(150)


square()
myturtle.forward(50)
square()

time.sleep(3)