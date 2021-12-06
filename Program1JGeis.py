# Date Last Modified:10/11/2021
# Author: Jack Geis
# Date Created: 10/11/2021
# Program Name: Guessinator v2.0
# Program Desscription/Algorithm: Generates a randome number, then tells user to guess a # between 1 and 100,
#     then tells them if they guessed it right or wrong. If they guess the number or leave the indented 
#     loop the program will ask if they want to play again, if they input 'y' the whole loop restarts,
#     if they input 'n' it leaves the program and says goodbye.

import random
from typing import Sequence

# greets the User
print(' ''\n')

print('Hello! This is the Guessinator v2.0!')

print(' ''\n')

print(format('-','-^60'))

print(' ''\n')

# Resets the guess total to 0

guessTot = 0

# sets a sentinel so that the while loop will run at least once.

sentinel = 'y'

# while loop that runs under the condition that the sentinel is not == 'n'

while sentinel != 'n' and sentinel != 'N':
    
    # sets a variable for the user to guess to a random number between 1 and 100
    
    N = random.randint(1,100)
    
    # Sets a variable equal to the users input
    
    guess = int(input('\n''Guess a number between 1 and 100''\n''I will tell you if you get it right: '))
    
    # while loop that compares the input and the random number to see if it should run, and
    # allows the user to exit by entering a '0'
    while guess != N and guess != 0:
        
        # decision structure that keeps the user from entering an incorrect number
        
        if guess < 1 or guess > 100 and guess != 0:
            
            print('The guess must be between 1 and 100.')
            
            # while loop to keep asking the user for the correct number 
            # if they continue to enter a number outside of 1-100.
            while guess < 1 or guess > 100 and guess != 0:
                
                guess = int(input('\n''Guess a number between ->1 and 100<-''\n''I will tell you if you get it right: '))
                
                # if the user enters a number that is between 1-100
                # makes sure that the program doesn't tell them that 
                # they need to enter a number between 1-100.

                if guess < 1 or guess > 100 and guess != 0:
                    
                    print('The guess must be between 1 and 100.')
        
        # Keeps track of the number of guesses, Will not count ones that
        # are outside of 1-100 because it goes after the error-catcher.
        
        guessTot += 1
    
        print('\n' 'Please try again')
        
        # gives the user a hint to make it easier to guess the number
        
        if guess > N:
            print('\n' 'Hint: Your guess is too high ;)')
        else:
            print('Hint: Your number is too low.')
        
        # Sets a variable equal to the users input
        
        guess = int(input('\n' 'Guess a number between 1 and 100. Enter 0 to quit: '))
    
    # checks if the user has guessed the number, if not, tells them the number.
    # in both situations asks the user if they want to restart the program after
    # telling them the amount of times that they guessed.
    
    if guess == N:
        
        print('\n' 'Congratualations! You guessed the number!')
        
        print('It took you ',guessTot, 'tries to guess the number.')

        sentinel = input('Would you like to play again y/n? ')
    else:
        
        print('You guessed the incorrect number, the number was', N)
        
        print('It took you ',guessTot, 'tries to guess the number.')

        sentinel = input('Would you like to try again y/n? ')

print(' ''\n')

print(format('-','-^60'))

# Goodbye :D

print('Thank you for using the Guessinator v2.0! Have a great day!')

print(format('-','-^60'))