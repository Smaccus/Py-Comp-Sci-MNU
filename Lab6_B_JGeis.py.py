#Date Last Modified: 10/5/2021
#Date Created: 10/5/2021
#Author: Jack Geis
#Program Name: Payinator
#Descrpition/Algorithm: This Program uses for loops to calculate the total pay and salary of two payment options
#over ten years, option 1 with $20,000 with a $1000 raise every full year, 
#and option 2 $10,000 with a $250 dollar raise every half year. The for loop will run 20 times, 1 time for 
#every half year, It will print the current salary and total pay of each payment option each time it runs.

#Welcome the user
print(format('-','=^40'))
print(format('Hello! Welcome to the Payinator!',' ^40'))
print(format('-','=^40'))

#Sets Variables to their defaults.
o1 = 20000
 
o2 = 10000

totalo1 = 0

totalo2 = 0

#Prints out context for the following output.
print(' Option   Salary   Total Pay')
print('','\n')

#for loop that will run 20 times.
for year in range(1,21):
    #if statement to run whenever year is an odd nummber
    if year %2 == 1:
        print('\t''Half year')

        #Calculates the total
        totalo2 += o2
        #Calculates salary
        o2 += 250
        #prints out opt 1 and opt2 with their respective totals
        print('Option 1: ',o1,' ',totalo1,end=' ')
        print('','\n')
        print('Option 2: ',o2,' ',totalo2,end=' ')
        print('','\n')
    #if statement to run whenever year is an even nummber
    if year %2 == 0:
        print('\t''Year',year/2)
        #Calculates salary and total for opt 1 and opt 2
        totalo1 += o1
        o1 += 1000
        totalo2 += o2
        o2 += 250
        #prints out opt 1 and opt2 with their respective totals
        print('Option 1: ',o1,' ',totalo1,end=' ')
        print('','\n')
        print('Option 2: ',o2,' ',totalo2,end=' ')
        print('','\n')
