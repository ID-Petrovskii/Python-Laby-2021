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

def signature():
    L = 50
    turtle.right(turtle.heading())
    #I
    turtle.forward(L/10)
    turtle.backward(L/5)
    turtle.forward(L/10)
    turtle.right(90)
    turtle.forward(L)
    turtle.left(90)
    turtle.forward(L/10)
    turtle.backward(L/5)
    turtle.forward(L/10)
    turtle.penup()
    turtle.forward(L/5)
    turtle.pendown()
    #D
    C = math.pi*L
    turtle.forward(L/10)
    for i in range(100):
        turtle.forward(C/200)
        turtle.left(1.8)
    turtle.forward(L/10)
    turtle.left(90)
    turtle.forward(L)
    turtle.left(90)
    turtle.penup()
    turtle.forward(8*L/10)
    turtle.left(90)
    turtle.forward(L/2)
    turtle.right(90)
    turtle.pendown()
    #-
    turtle.forward(L/5)
    turtle.penup()
    turtle.forward(L/5)
    #P
    turtle.pendown()
    turtle.forward(L/10)
    for i in range(100):
        turtle.forward(C/400)
        turtle.left(1.8)
    turtle.forward(L/10)    
    turtle.left(90)
    turtle.forward(L)
    turtle.left(90)
    turtle.penup()
    turtle.forward(4*L/10)
    turtle.forward(L/2)
    turtle.left(90)
    turtle.forward(L/4)
    turtle.pendown()
    #e
    turtle.left(90)
    turtle.forward(L/2)
    turtle.backward(L/2)
    turtle.right(90)
    C = L/2*math.pi
    for i in range(100):
        turtle.forward(0.75*C/100)
        turtle.left(2.7)
    turtle.forward(L/20)
    turtle.penup()
    turtle.forward(L/4+L/20+L/5)
    turtle.pendown()
    #t
    turtle.left(90)
    turtle.forward(L/2)
    turtle.right(90)
    turtle.forward(L/5)
    turtle.backward(2*L/5)
    turtle.forward(L/5)
    turtle.left(90)
    turtle.forward(L/2)
    turtle.backward(L)
    turtle.right(90)
    turtle.penup()
    turtle.forward(3*L/10)
    turtle.pendown()
    #r
    turtle.left(90)
    turtle.forward(L/2)
    turtle.backward(L/4)
    turtle.forward(L/15)
    for i in range(100):
        turtle.forward(C/400)
        if i == 50:
           turtle.forward(L/20) 
        turtle.right(1.8)
    turtle.forward(L/20)
    
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

turtle.penup()
turtle.goto(250, -305)
turtle.pendown()
turtle.color('black')
turtle.width(3)
signature()
turtle.hideturtle()

turtle.done()
