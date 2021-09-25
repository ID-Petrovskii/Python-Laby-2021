import turtle
import random
import math

turtle.shape('turtle')
turtle.speed(0)
turtle.colormode(255)
r = 128
g = 128
b = 128
dr = 0
dg = 0
db = 0
width = 7
dwidth = -1
v = 5
turtle.color(r, g, b)

def changecol():
    global dr
    global db
    global dg
    dr = random.randint(-10, 10)
    if r+dr<0 or r+dr>255:
        dr = -dr
    dg = random.randint(-10, 10)
    if g+dg<0 or g+dg>255:
        dg = -dg
    db = random.randint(-10, 10)
    if b+db<0 or b+db>255:
        db = -db

for t in range(1111):
    fi = 100*(0.5 - random.random())  
    if math.fabs(turtle.xcor())>254 or math.fabs(turtle.ycor())>254:
        ynew = turtle.ycor()+ v*math.sin(turtle.heading())
        xnew = turtle.xcor()+ v*math.cos(turtle.heading())
        if math.fabs(xnew)>300:
            turtle.penup()
            turtle.hideturtle()
            xp = -300*(xnew/math.fabs(xnew))
            turtle.goto(xp, turtle.ycor())
            turtle.pendown()
            turtle.showturtle()
        elif math.fabs(ynew)>300:
            turtle.penup()
            turtle.hideturtle()
            yp = -300*(ynew/math.fabs(ynew))
            turtle.goto(turtle.xcor(), yp)
            turtle.pendown()
            turtle.showturtle()
    turtle.left(fi)
    turtle.forward(v)
    changecol()
    while r+g+b+dr+dg+db<255:
        changecol()
    r += dr
    g += dg
    b += db
    turtle.color(r, g, b)
    change = random.random()
    if width+dwidth<1 or width+dwidth>20 or change>0.9:
        dwidth = -dwidth
    width += dwidth
    turtle.width(width)


turtle.hideturtle()
turtle.done()
