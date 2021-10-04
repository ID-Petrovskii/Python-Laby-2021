import turtle
import math

turtle.speed(0)
turtle.shape('turtle')

def circle(r, k):
    n = 100
    for j in range(n):
        turtle.forward(r/n)
        turtle.left(k*360/n)

turtle.left(90)
for i in range(7):
    R = (i+2)*50
    circle(R, 1)
    circle(R, -1)

turtle.done()
