from random import randint
import turtle

turtle.shape('square')
turtle.penup()
turtle.speed(10)

L = 300

turtle.goto(-L, L)
turtle.pendown()
turtle.goto(-L, -L)
turtle.goto(L, -L)
turtle.goto(L, L)
turtle.goto(-L, L)
turtle.hideturtle()

nturt = 23
t = 1000
v = 10
R = 5
    
pool = [turtle.Turtle(shape='circle') for i in range(nturt)]
for turt in pool:
    turt.penup()
    turt.speed(1000)
    turt.goto(randint(-L, L), randint(-L, L))
    turt.left(randint(0, 360))


for i in range(t):
    for turt in pool:
        turt.forward(v)
                    
        if turt.xcor() > L:
            turt.left(180-2*turt.heading())
            turt.forward(v)
        elif turt.xcor() < -300:
            turt.left(180-2*turt.heading())
            turt.forward(v)
        if turt.ycor() > L:
            turt.right(2*turt.heading())
            turt.forward(v)
        elif turt.ycor() < -300:
            turt.right(2*turt.heading())
            turt.forward(v)

        
