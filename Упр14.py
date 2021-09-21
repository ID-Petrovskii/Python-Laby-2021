import turtle

turtle.speed(0)
turtle.shape('turtle')

def star(a, n):
    for i in range(n):
        turtle.forward(a)
        turtle.right(180 - 180/n)

star(250, 5)
turtle.left(180)
turtle.penup()
turtle.forward(50)
turtle.pendown()
star(250, 11)

turtle.done()
