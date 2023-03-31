import turtle


t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor('white')
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
