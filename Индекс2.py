import turtle
import math

turtle.shape('turtle')
turtle.color('blue')
turtle.width(2)
turtle.speed(10)
turtle.penup()

a = 50

numbers =[]
with open('font.txt', 'r') as f:
    for u in range(10):
        numbers.append(eval(f.readline()))

x0 = -300
y0 = 0
turtle.goto(x0, y0)

def draw(lis1):
    turtle.pendown()
    global x0
    global y0
    for j in lis1:
        x, y = j
        x = x
        y = y
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
