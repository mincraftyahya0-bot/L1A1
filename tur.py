#activity1
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

num=int(input("enter sides here : "))
len=int(input("enter size here"))
angle=360.0/num

for i in range(num):
    polygon.forward(len)
    polygon.right(angle)
#activity2
turtle.clear
turtle.Screen().bgcolor("Auqa")
board=turtle.Turtle()

board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)
board.penup()
board.right(90)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()