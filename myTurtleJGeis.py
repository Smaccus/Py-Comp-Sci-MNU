# Date Last Modified: 10/19/2021
# Date Created: 10/18/2021
# Author: Jack Geis
# Program Name: Turtlenator
# Descrpition/Algorithm: Uses Turtle Graphics to draw a car

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
    print(format('Hello! Welcome to the Turtlenator!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')





###########################
##### Main Program ########
###########################

greeting()

#Setup

turtle.setup(1000, 600)
turtle.hideturtle()
turtle.bgcolor('gray')
turtle.speed(0)

#Code to draw a car

turtle.shape('turtle')
turtle.penup()
turtle.goto(-250, 0)
turtle.showturtle()
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()


#Code to draw bottom

turtle.forward(500)
turtle.left(90)


#Code to draw front bumper

turtle.forward(75)
turtle.left(90)


#Code to draw hood

turtle.forward(120)
turtle.right(45)


#Code to draw windshield

turtle.forward(80)
turtle.left(45)


#Code to draw roof

turtle.forward(180)
turtle.left(45)


#Code to draw rear window

turtle.forward(80)
turtle.right(45)


#Code to draw top of trunk

turtle.forward(87)
turtle.left(90)


#Code to draw rear bumper

turtle.forward(75)
turtle.end_fill()
turtle.penup()


#Code to draw headlights

turtle.goto(225, 50)
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()


#Code to draw brakelights
turtle.goto(-245, 50)

turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()


#Code to draw left wheel

turtle.goto(-150, -10)
turtle.right(90)
turtle.showturtle()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(33)
turtle.end_fill()


#Code to draw right wheel

turtle.goto(150, -10)
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(33)
turtle.end_fill()
turtle.hideturtle()


#Code to draw a road

turtle.goto(-500, -70)
turtle.showturtle()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.right(180)
turtle.forward(995)
turtle.right(90)
turtle.forward(222)
turtle.right(90)
turtle.forward(995)
turtle.right(90)
turtle.forward(222)
turtle.end_fill()


#Code to draw lane lines

turtle.right(90)
turtle.goto(-500, -100)
for y in range(4):
    turtle.fillcolor('white')
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(125)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(300)


#Code to draw a speed limit sign

turtle.goto(400, -70)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
for x in range(2):
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
turtle.end_fill()
turtle.forward(150)
turtle.left(90)
turtle.forward(19)
turtle.right(90)

turtle.begin_fill()
for x in range(2):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
turtle.end_fill()

fontsize = 13

FONT = ('Arial', fontsize, 'normal')

turtle.penup()
turtle.forward(14)
turtle.right(90)
turtle.forward(15)
turtle.write('45', font=FONT)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(11)
fontsize = 7
FONT = ('Arial', fontsize, 'normal')
turtle.write('Speed limit', font=FONT)
turtle.hideturtle()

turtle.done()


farewell()