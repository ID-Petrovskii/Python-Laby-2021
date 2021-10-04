import turtle
import math

def circle(r, k):
    n = 100
    for j in range(n):
        turtle.forward(r/n)
        turtle.left(360*k/n)
n = 100
turtle.shape('turtle')
for i in range(3):
    turtle.left(120*i)
    circle(360, 1)
    circle(360, -1)
    turtle.right(120*i)

turtle.done()
