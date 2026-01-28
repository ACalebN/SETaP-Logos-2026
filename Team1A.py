import turtle

t = turtle.Turtle()
x = 150

for i in range(2):
    t.forward(x)
    t.right(90)
    t.forward(x *2)
    t.right(90)

t.penup()
t.forward(x/6)
t.right(90)
t.forward(x/10)
t.left(90)
t.pendown()
for i in range(4)
    t.forward(2*x/3)
    t.right(90)

turtle.exitonclick()