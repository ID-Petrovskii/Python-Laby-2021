import turtle

turtle.shape('turtle')
N = 10
for i in range(1, N+1):
    turtle.penup()
    turtle.goto(-10*i, -10*i)
    turtle.pendown()
    turtle.forward(20*i)
    turtle.left(90)
    turtle.forward(20*i)
    turtle.left(90)
    turtle.forward(20*i)
    turtle.left(90)
    turtle.forward(20*i)
    turtle.left(90)
turtle.done()
