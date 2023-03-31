import turtle
t = turtle.Turtle()
t.shape('turtle')
line = int(input('몇각형을 그리고 싶으신가요? '))
# angle = int(input('회전 각도를 입력하세요. '))

# length = int(input('전진 길이를 입력하세요. '))
for i in range(line):
    t.forward(100//line*5)
    t.left(360//line)
    
turtle.exitonclick()