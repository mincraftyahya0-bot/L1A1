import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.tracer(10)

t = turtle.Turtle()
t.color("black", "red")
t.speed(0)

t.up()
t.goto(0, -100)
t.down()

t.begin_fill()

t.left(45)
t.forward(116)

for i in range(180):
    t.forward(1)
    t.left(1)

t.right(90)

for i in range(180):
    t.forward(1)
    t.left(1)

t.forward(116)

t.end_fill()

screen.update()
turtle.done()
