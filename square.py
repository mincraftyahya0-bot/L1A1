import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

num=4
len=int(input("enter size here"))
angle=360.0/num

for i in range(num):
    polygon.forward(len)
    polygon.right(angle)

turtle.done()