import turtle
import random

colors=[ "blue" , "red" , "red" , "green" , "purple" , "black" , "green" ]
a= len(colors)
ninja = turtle.Turtle()

ninja.speed(2000)
ninja.color('red')
for i in range(180):
    c = random.randrange(a)
    ninja.color(colors[c])
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()
