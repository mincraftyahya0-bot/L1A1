import turtle
import random
angle=360/21
for i in range(5):
    for i in range(21):
            len=random.randint(50,150)
            turtle.forward(len)
            turtle.up()
            turtle.goto(0,0)
            turtle.down()
            turtle.right(angle)
'''turtle.up
turtle.goto(random.randint(300,-300))  
turtle.down'''
turtle.done()