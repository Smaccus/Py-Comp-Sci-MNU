# Date Last Modified: 11/16/2021
# Date Created: 11/9/2021
# Authors: Jack Geis, James Mwihaki, Stevo Fleuriot, Kellen Pickering, And Jacob Tegt.
# Program Name: The Guessinator V 3.0
# Descrpition/Algorithm: This program is a treasure hunting game, the user can pick one of three modes, easy, medium, or hard.
# The program has three different grids for each respective difficulty, 3x3 with 7 guesses, 4x4 with 10 guesses, and a 5x5 with
# 15 guesses. Each guess is counted and displayed when the user is finished playing. 
# If the user finds a treasure the spot they found it in will display a '♔', and if the spot they choose does not have a 
# treasure it will display a 'X'. When the user has run out of guesses the program tells them how many treasures 
# they found and asks them if they want to play again, if they guess all the treasures, it also asks if they want
# to play again.

#imports random from the python library
import random

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
    print(format('Hello! Welcome to The Guessinator V 3.0!',' ^45'))
    print(format('-','=^45'))
    print(' ', '\n')


# Function to explain the program
# Input/variables: null
# Return Value/Output: null

def explaination():
    print('This is a treasure hunting game, to win you must find all 5 of the treasures.')
    print('Forbeach difficulty you have a certain amount oof guesses to find all the treaures.')
    print('Easy is a 3x3 grid with 7 guesses.''\n'' Medium is a 4x4 grid with 10 guesses.')

# Function to ask for the level of dificulty
# Input/variables: nul
# Return Value/Output: level and the number of guess the usser has

def level():
    easy = 3
    medium = 4
    hard = 5

    ans = str(input("There are Three modes in Game. 1.Easy 2.Medium and 3.Hard \nTo start type either Easy, Hard or Medium to start: "))
    while (ans != 'easy' and ans != 'medium') and ans != 'hard':
            print("Try Again")
            ans = str(input("There are modes to the game. 1.Easy 2.Medium and 3.Hard \nChoose either Easy, Hard or Medium to start: "))
            
    if ans == 'easy':
        ans = 3
        guess = 7
    elif ans == 'medium':
        ans = 4
        guess = 10
    else:
        ans = 5
        guess = 15
    
    
    return ans, guess




# Function to create the needed grid according to the ans
# Input/variables: ans
# Return Value/Output: grid, grid2 

def grids(ans):
    if ans == 3:
        grid = [0] * (ans + 1)
    elif ans == 4:
        grid = [0] * (ans + 7)
    elif ans == 5:
        grid = [0] * (ans + 17)
    grid2 = ['O'] * (ans * ans)
    return grid, grid2


# Function to place the treasure randomly in the grid
# Input/variables: Grid, ans
# Return Value/Output: grid

def randomTreasurePlacement(grid, ans ):
    ans = ans * ans
    for x in range(5):
        grid.insert(random.randint(0, ans), 1)
        
    return grid


# Function to display the grid to the usset 
# Input/variables: grid2 and ans
# Return Value/Output: nul

def printGrid(grid2, ans):
    counter = 0
    for x in range(ans):
        print("\n")
        for y in range(ans):
            if counter < len(grid2):
                print(" ",format(counter, '2.0f')," [", grid2[counter], "]", end = " ")
                counter += 1
    print("\n")


# Function to get the position the usser has guessed 
# Input/variables:  nul 
# Return Value/Output: num  

def locationOfTreasure():
    position = input("Enter the number to the left of the spot you want to guess: ")
    alpha = position.isalpha()
    number = position.isdigit()
    while number == False or alpha == True:
        print("Your input must be a number!")
        position = input("Enter the number to the left of the spot you want to guess: ")
        alpha = position.isalpha()
        number = position.isdigit()
    num = int(position)
    return num


# Function to print the grids, wheather the usser found all the treausers or not
# Input/variables: grid, grid2, ans and guess
# Return Value/Output: null

def outputAndReplace(grid, grid2, ans, guess):
    counter = 0
    score = 0
    used_numbers = []

    
    while counter < guess and score < 5:
        position = locationOfTreasure()
        parameter = ans * ans -1
        if position <= parameter and position >= 0:
            if grid[position] == 1:
                print("You Found A Treasure!")
                grid2[position] = '♔'
                if position in used_numbers:
                    print("You Already Tried That Position")
                else:
                    used_numbers.append(position)
                    score += 1
                printGrid(grid2,ans)    
                
                guessLeft = (guess-1) - counter
                print('You have ',guessLeft,' guesses left.')
                counter += 1
                
            elif grid[position] != 1:
                grid2[position] = 'X'
                
                print("There is no treasure in that location\nTry Again!")
                printGrid(grid2,ans)
                
                guessLeft = (guess-1) - counter
                print('You have ',guessLeft,' guesses left.')
                counter += 1
            else:
                print("Try Again!")

    if score < 5:
        print("\nYou only found", score, "Treasure")
    else:
        print("\nYou Win!, You found all 5 of the the Treasures!")


###########################
###### Main Program #######
###########################

# Calls greeting function

greeting()

sentinel = 'y'

while sentinel == 'y':
    explaination()

    ans, guess = level()

    grid, grid2 = grids(ans)

    grid = randomTreasurePlacement(grid, ans)

    printGrid(grid2, ans)

    print()

    outputAndReplace(grid, grid2, ans, guess)

    sentinel = input('Would you like to play again, y/n?: ')


# Calls farewell function

farewell()
