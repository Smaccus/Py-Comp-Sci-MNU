#Date Last Modified: //
#Date Created: //
#Author: Jack Geis
#Program Name:
#Descrpition/Algorithm:

#Welcome the user
print(format('-','=^40'))
print('Hello! Welcome to the <program name>!')
print(format('-','=^40'))

r = 0

x = 0

ast = 0

while r != 999:
    r = int(input('enter number a of rows between 1 and 20, enter 999 to stop: '))
    while r < 1 or r > 20 and r != 999: 
        print('Error, input must be in range.')
        r = int(input('enter number a of rows between 1 and 20, or enter 999 to exit: '))
    if r != 999:
        for x in range(r):
            for ast in range(x+1):
                print("*",end='')
            print()
if r == 999:
    print('Goodbye!')
