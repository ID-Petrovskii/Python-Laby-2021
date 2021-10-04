import turtle

turtle.speed(0)
turtle.shape('turtle')
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

def leuf(R, fi):
        for i in range(100):
                turtle.forward((fi/360)*(R/100))
                turtle.left(fi/100)

leuf(250, 180)
for i in range(6):
    leuf(50, 180)
    leuf(250, 180)

turtle.done()
