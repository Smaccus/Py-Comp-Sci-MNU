#Date Last Modified: 10/4/2021
#Date Created:10/4/2021
#Author: Jack Geis
#Program Name: Populationator
#Descrpition/Algorithm: This program calculates the population growth from 2014 -  2020


#Welcome the user
print(format('-','=^40'))
print('Hello! Welcome to the Populationator!')
print(format('-','=^40'))

yrs = 0

pop = 300000

growth = 1.03

print('year','\t','population')

for yrs in range(2014,2021):
    print(yrs,'\t',format(pop,'8.0f'))
    pop *= growth
