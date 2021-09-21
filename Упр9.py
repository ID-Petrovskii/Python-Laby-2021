import turtle
import math

def polygon(n, R):
    turtle.penup()
    turtle.goto(0, -R)
    turtle.pendown()
    a = 2*R*math.sin(math.pi/n)
    turtle.left(180/n)
    for j in range(n):
        turtle.forward(a)
        turtle.left(360/n)
    turtle.right(180/n)

turtle.shape('turtle')
for i in range(10):
    m = i+3
    r = (i+1)*25
    polygon(m, r)
turtle.done()
