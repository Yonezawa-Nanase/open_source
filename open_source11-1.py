import turtle

T = turtle.Turtle()
default = T.heading()

def circle(color,start,end,x = 0,y = 0):
    T.penup()
    T.goto (x,y)
    T.setheading(default)
    T.circle (100,start)
    T.pendown()
    T.width (10)
    T.color (color)
    T.circle(100,end)


circle(color = "#000000",start = 0,end = 45)
circle(color = "red",start = 135,end = 180,x = 215,y = 0)
circle(color = "green",start = 0,end = 360,x = 115,y = -100)
circle(color = "red",start = 315,end = 180,x = 215,y = 0)
circle(color = "yellow",start = 0,end = 135,x = -115,y = -100)
circle(color = "#000000",start = 45,end = 315)
circle(color = "blue",start = 225,end = 180,x = -215,y = 0)
circle(color = "yellow",start = 135,end = 225,x = -115,y = -100)
circle(color = "blue",start = 45,end = 180,x = -215,y = 0)

turtle.done()