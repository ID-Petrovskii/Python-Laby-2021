import turtle
import math

turtle.speed(0)
turtle.shape('turtle')

def leuf(x0, y0, L, fi):
    turtle.penup()
    turtle.goto(x0, y0)
    turtle.pendown()
    for i in range(100):
        turtle.forward(L/100)
        turtle.left(fi/100)

turtle.begin_fill()
leuf(0, 0, 400, 360)
turtle.color('yellow')
turtle.end_fill()


turtle.color('black')
turtle.begin_fill()
leuf(30, 80, 50, 360)
turtle.color('blue')
turtle.end_fill()

turtle.color('black')
turtle.begin_fill()
leuf(-30, 80, 50, 360)
turtle.color('blue')
turtle.end_fill()

turtle.color('black')
turtle.right(90)
turtle.width(7)
leuf(0, 80, 25, 0)

turtle.color('red')
leuf(-32, 45, 100, 180)

turtle.done()
