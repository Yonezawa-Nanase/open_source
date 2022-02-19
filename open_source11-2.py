import turtle
import random
import time


T1 = turtle.Turtle()
T1.shape("turtle")
T1.penup()
T1.goto (0,20)
#T1.pendown()

T2 = turtle.Turtle()
T2.shape("turtle")
T2.penup()
T2.goto (0,-20)
#T2.pendown()

move = True
goal = 100

line = turtle.Turtle()
line.penup()
line.goto (goal,-50)
line.pendown()
line.left(90)
line.forward(100)

while move :
    T1.forward(random.randint(1,20))
    T2.forward(random.randint(1,20))
    if T1.xcor() > goal or T2.xcor() > goal:
        move = False
    time.sleep(0.5)

turtle.done()