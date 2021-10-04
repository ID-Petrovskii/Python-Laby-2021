import turtle
import random 

turtle.shape('turtle')
turtle.speed(0)

for i in range(666):
    L = 30*random.random()
    fi = 360*random.random()
    turtle.forward(L)
    turtle.left(fi)

turtle.done()
