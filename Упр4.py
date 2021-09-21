import turtle

turtle.speed(0)
turtle.shape('turtle')
N=360
R=360
for i in range(N):
    turtle.forward(R/N)
    turtle.left(360/N)

turtle.done()
