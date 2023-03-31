import turtle

t = turtle.Turtle()
t.shape('turtle')

x = 0
y = 0

for i in range(1, 6):
    for j in range(0, i):
        t.circle(20)

        t.up()
        x += 50
        t.goto(x, y)
        t.down()
    
    x = 0
    y -= 50

    t.up()
    t.goto(x, y)
    t.down()

turtle.exitonclick()