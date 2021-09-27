import turtle
import math

turtle.shape('turtle')
turtle.color('blue')
turtle.width(2)
turtle.speed(10)
turtle.penup()

a = 50

zero = [(-a, 0), (-a, -2*a), (0, -2*a), (0,0)]
one = [(-a, -a), (0, 0), (0, -2*a), (0, 0)]
two = [(-a, 0), (0, 0), (0, -a), (-a, -2*a), (0, -2*a), (-a, -2*a), (0, -a), (0, 0)]
three = [(-a, 0), (0, 0), (-a, -a), (0, -a), (-a, -2*a), (0, -a), (-a, -a), (0, 0)]
four = [(0, -a), (-a, -a), (-a, 0), (-a, -a), (0, -a), (0, -2*a), (0, 0)]
five = [(-a, 0), (-a, -a), (0, -a), (0, -2*a), (-a, -2*a), (0, -2*a), (0, -a), (-a, -a), (-a, 0), (0, 0)]
six = [(-a, -a), (-a, -2*a), (0, -2*a), (0, -a), (-a, -a), (0, 0)]
seven = [(-a, 0), (0, 0), (-a, -a), (-a, -2*a), (-a, -a), (0, 0)]
eight = [(-a, 0), (-a, -a), (0, -a), (0, -2*a), (-a, -2*a), (-a, -a), (0, -a), (0, 0)]
nine = [(-a, 0), (-a, -a), (0, -a), (-a, -2*a), (0, -a), (0, 0)]
numbers = (zero, one, two, three, four, five, six, seven, eight, nine)


x0 = -300
y0 = 0
turtle.goto(x0, y0)

def draw(lis1):
    turtle.pendown()
    global x0
    global y0
    for j in lis1:
        x, y = j
        turtle.goto(x0 + x, y0 + y)     
    turtle.penup()
    x0 = x0 + a + 15
    turtle.goto(x0, y0)    

def index(lis):
    
    for i in lis:
        for k in range(10):
            if i == str(k):
                draw(numbers[k])

A = str(input())
index(A)

turtle.done()
            
        
