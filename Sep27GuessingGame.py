#Date Last Modified: 9/27/2021
#Author: Jack Geis
#Date Created: 9/27/2021
#Program Name: Guessinator
#Program Desscription/Algorithm: Tells user to guess a # between 1 and 100,
#     then tells them if they guessed it right or wrong.


print('Hello! This is the Guessinator!')

print(' ''\n')

print(format('-','-^60'))

print(' ''\n')

N = 7

guess = int(input('Guess a number between 1 and 100''\n''I will tell you if you get it right: '))

while guess != N and guess != 0:
    print('\n' 'Please try again')
    if guess > N:
        print('\n' 'Hint: Your guess is too high ;)')
    else:
        print('Hint: Your number is too low.')
    guess = int(input('\n' 'Guess a number between 1 and 100. Enter 0 to quit: '))

if guess == N:
    print('\n' 'Congratualations! You guessed the number!')
else:
    print('You guessed the incorrect number, the number was', N)

print(' ''\n')

print(format('-','-^60'))

print('Thank you for using the Guessinator! Have a great day!')
print(format('-','-^60'))
