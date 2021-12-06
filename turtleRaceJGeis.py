# Date Last Modified: 11/30/2021
# Date Created: 11/28/2021
# Author: Jack Geis
# Program Name: Turtle Club Racing Program
# Descrpition/Algorithm: This program uses three functions to create 10 turtles and race them.
## To do this, a list of all ten turtles is made with a for loop, this also gives each turtle a different color.
## Next, another for loop moves each turtle to it's starting position. Lastly, the startTurtles function
## moves each turtle forward a random amount between 1 and 6, and stops when one has crossed the finish line.
## The function then checks which turtle has won and passes it back to the main program, which prints out
## which turtle has won the race.

import turtle
import random
import time


#Name: generateTurtles
#create a turtle for each color in the input list that is the color given and return a list of all those turtles
#input: a list with colors in it
#return value: a list with turtles in it


def generateTurtles(colors):
    turtleList = []
    for i in colors:
        t1 = turtle.Turtle()
        t1.fillcolor(i)
        t1.shape('turtle')
        t1.penup()
        turtleList.append(t1)
        time.sleep(.1)
    return turtleList



#Name: placeTurtles
#move all the turtles passed in the list to their start positions with the track seperation between each
#input: a list of turtles, the start line location, how far each should be seperated
#return value: no return	


def placeTurtles(turtles, start_loc, track_separation):
    Ycord = start_loc[1]
    for selectedTurtle in turtles:
        selectedTurtle.goto(start_loc[0],Ycord)
        Ycord += track_separation
    
        

#Name: startTurtles
#starts the race and moves each turtle one at a time until a winner reaches the finish line
#input: a list of turtles, the finish line location, a forward increment 
#return value: the color of the winning turtle			


def startTurtles(turtles, finish_line, forward_incr):
    selectedTurtle = turtles[0]
    while selectedTurtle.xcor() <= finish_line:
        for selectedTurtle in turtles:
            selectedTurtle.forward(random.randint(1,forward_incr))
    for seletedTurtle in turtles:
        turtleXcor = seletedTurtle.xcor()
        if turtleXcor >= finish_line:
            winner = turtles.index(seletedTurtle)
            return winner



#~~~~~~~~~~MAIN~~~~~~~~~~~



#Initialize the number of turtles
num_turtles = 10

#Set window size
turtle.setup(700,700)

#Get turtle window
window = turtle.Screen()

#Set window title
window.title('The Great American Turtle Race!')

#Initialize screen layout parameters
start_loc = (-240, -200)
finish_line = 240
track_separation = 60
forward_incr = 6

#Set turtle colors
colors = ['dark red', 'red','orange','yellow','chartreuse', 'green', 'turquoise', 'blue','violet', 'purple']

#Generate and initialize turtles
turtles = generateTurtles(colors)

#Place turtles at starting line
tempVar = placeTurtles(turtles, start_loc, track_separation)

#Start turtles
winner = startTurtles(turtles, finish_line, forward_incr)

#Display winning turtle
print("The winner is the "+colors[winner]+" turtle!")

turtle.done()

#Terminate program when close window
turtle.exitonclick()