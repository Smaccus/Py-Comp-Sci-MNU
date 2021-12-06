# Date Last Modified: 1/30/2021
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
    print(format('Hello! Welcome to a Class Exercise!',' ^45'))
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
    # Pushes all of the turtles in stack 1 into stack2 and shows each turtle as it is copied to stack2.
    for i in stack1:
        stacks.push(stack2, i)
        i.showturtle()
        time.sleep(.1)
        
    # Pops all of the turtles in stack1 and hides them as it is popped.

    for i in stack2:
        stacks.pop(stack1)
        i.hideturtle()
        time.sleep(.1)

    # Pushes all of the turtles in stack2 into stack2 and shows each turtle as it is copied to stack1.

    for i in stack2:
        stacks.push(stack1, i)
        i.showturtle()
        time.sleep(.1)

    # Pops all of the turtles in stack2 and hides them as it is popped.
    
    for i in stack1:
        stacks.pop(stack2)
        i.hideturtle()
        time.sleep(.1)


# Calls farewell function

farewell()