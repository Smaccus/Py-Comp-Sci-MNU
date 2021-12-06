# Date Created: 12/2/2021
# Last Modified: 12/2/2021
# Topic: stacks
# Psudocode Y/N?: N

import stacks
import turtle
import time

shape = 'classic'

color = 'yellow'

shapeList = []

turtle.hideturtle()

baseShape = turtle.Turtle(shape)
baseShape.turtlesize(16)

for i in range(16,1,-2):
    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.shape(shape)
    t1.fillcolor(color)
    t1.penup()
    t1.turtlesize(i)
    shapeList.append(t1)

stack1 = stacks.getStack()

stack2 = stacks.getStack()

for shapes in shapeList:
    stacks.push(stack1, shapes)


for i in range(10):
    for i in stack1:
        stacks.push(stack2, i)
        i.showturtle()
        time.sleep(.1)

    for i in stack2:
        stacks.pop(stack1)
        i.hideturtle()
        time.sleep(.1)
    
    for i in stack2:
        stacks.push(stack1, i)
        i.showturtle()
        time.sleep(.1)
    
    for i in stack1:
        stacks.pop(stack2)
        i.hideturtle()
        time.sleep(.1)





    
