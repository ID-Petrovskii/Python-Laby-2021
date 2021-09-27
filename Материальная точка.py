import turtle
import math

turtle.shape('circle')
turtle.speed(0)

v = 25
g = -1
k = 0.7
i = 0
dt = 0.1
alpha = 75
vx = v*math.cos(alpha*math.pi/180)
vy = v*math.sin(alpha*math.pi/180)
x = -300
y = 0
turtle.goto(-x*30, y)
turtle.goto(x, y)
turtle.pendown()

while i < 10:
    x += vx*dt
    vy += g*dt
    y += (vy*dt + dt*dt*g/2)
    turtle.goto(x, y)
    if y<0:
        y = -y
        vy = -k*vy
        i += 1

        
turtle.done()
