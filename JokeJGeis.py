#Date Last Modified: 9/15/2021
#Author: Jack Geis
#Name: The Jokinator
#Discription: This is the Jokinator, It asks the user for their name, favorite
             #color, and favorite quote. Then it outputs a joke containing their name,
             #color, and quote.

#Greets user, tells them the programs name and what it does.
print('Hello! This is the Jokinator, I am going to make a joke using info you input.')

#Tells the user to input data and assigns data to a variable.
name = str(input('Input name here: '))

color = str(input('Input favorite color here: '))

Q = str(input('Input your favorite quote here: '))

#says the first part of the joke, waits for input, then says the second part,
#waits for input, then outputs the last part of the joke.
input('Knock knock. ')

print(color, name)

input()

print(Q)

#Thanks the user by name and says goodbye.
print('Thank you,', name,', for using the Jokinator, Goodbye! :D')

