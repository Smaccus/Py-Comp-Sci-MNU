# Date Last Modified: 12/7/2021
# Date Created: 11/30/2021
# Author: Jack Geis
# Program Name: Arrow Directionator
# Descrpition/Algorithm: This program uses two stacks to show/hide turtles to make an 'animated' turtle graghics 
# picture. It does so by moveing the turtles to a stack until it is full, then moving them back out of that stack
# into a different stack. As they move to and from a stack the turtles will be shown or hidden depending on the
# stack they are in.

import stacks
import time
import turtle

# Function to say goodbye
# Input: null
# Return Value/Output: Uses print and format statements to thank and say goodbye to the user.
def farewell():
    print(' ', '\n')
    print(format('-','=^45'))
    print(format('Thank you for using my program!',' ^45'))
    print(format('Have a woderful day! :D',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')



# Function to greet the user.
# Input: null
# Return Value/Output: Uses print and format statements to greet the user

def greeting():
    print(' ', '\n')
    print(format('-','=^45'))
    print(format('Hello! Welcome to the Arrow Directionator!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')



###########################
##### Main Program ########
###########################

# Calls greeting function

greeting()

# Sets a shape and color to two different variables

shape = 'classic'

color = 'yellow'

# Creates an empty list for all the turtle shapes

shapeList = []

# Hides the turtle

turtle.hideturtle()

# Sets a background shape

baseShape = turtle.Turtle(shape)

baseShape.turtlesize(16)

# Creates all the shapes and appends them to shapeList

for i in range(16,1,-2):
    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.shape(shape)
    t1.fillcolor(color)
    t1.penup()
    t1.turtlesize(i)
    shapeList.append(t1)

# Creates two stacks and assignes each to a variable

stack1 = stacks.getStack()

stack2 = stacks.getStack()

# Copies the list of turtles into stack1

for shapes in shapeList:
    stacks.push(stack1, shapes)

# For loop that runs through 10 times

for i in range(10):
    # While loop that runs until stack1 is empty, pops an item off stack1, pushes it to stack2, shows the popped turtle, then delays .1
    while not stacks.isEmpty(stack1):
        selectedTurtle = stacks.pop(stack1)
        stacks.push(stack2, selectedTurtle)
        selectedTurtle.showturtle()
        time.sleep(.1)
    # While loop that runs until stack2 is empty, pops an item off stack2, pushes it to stack1, shows the popped turtle, then delays .1
    while not stacks.isEmpty(stack2):
        selectedTurtle = stacks.pop(stack2)
        stacks.push(stack1, selectedTurtle)
        selectedTurtle.hideturtle()
        time.sleep(.1)

# Calls farewell function

farewell()
