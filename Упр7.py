import turtle
import math

turtle.shape('turtle')
n = 500
w=0.1
v=0.5
for t in range(n):
    x = v*t*math.cos(w*t)
    y = v*t*math.sin(w*t)
    turtle.goto(x, y)
turtle.done()
