#Date Last Modified: 9/21/2021
#Author: Jack T. Geis
#Program Name: Tipinator 5000
#Description/Algorithm: This program takes input first, by
#     asking for the appetizer amount, then
#     the soft drink amount, the entree amount,
#     and finally, for the dessert amount.
#     It then calculates the sub-total and adds
#     the tax (%9.4 rate) to get the total.
#     The program then outputs the subtotal,
#     the tax amount, the total, and suggested
#     tip amounts, 15%, 18%, and 20%.

#first greet the user and welcomes them in a fancy format.

print(format('º','•^40'))
print(format('•','º^40'))

print(format('Hello! Welcome to the Tipinator 500!', '•^30'))

print(format('•','º^40'))
print(format('º','•^40'))

#Get the input for the amounts and assign them to a variable.

app = float(input('\n''Amount paid for your appetizer: '))

drk = float(input('\n''Amount paid for your soft drinks: '))

ent = float(input('\n''Amount paid for your entree?: '))

des = float(input('\n''Amount paid for your desserts?: '))

#More formatting for ultimate beauty

print('\n'' ')

print(format('∞','∞^40'))

print('\n'' ')

print(format('^','<^40'))
print(format('Geis Guys Cuisine™','º^40'))
print(format('^','>^40'))

print('\n'' ')
#Calculations for sub-total, taxes, and net total.

sub = app+drk+ent+des

tax = .094*sub

net = sub+tax

#Outputs subtotal, net total, and tax.

print('Subtotal',format('$','.>24'),format(sub,'3.2f'))
print('\n'' ')
print('Tax',format('$','.>30'),format(tax,'3.2f'))
print('\n'' ')
print('Total',format('$','.>27'),format(net,'3.2f'))

#Tip calculations and output

T15 = net*.15

T18 = net*.18

T20 = net*.20

print('\n'' ')
print(format('∞','∞^40'))
print('\n'' ')

print('Tip 15%',format('$','.>27'),format(T15,'3.2f'))
print('\n'' ')
print('Tip 18%',format('$','.>27'),format(T18,'3.2f'))
print('\n'' ')
print('Tip 20%',format('$','.>27'),format(T20,'2.2f'))

#Bye!

print('\n'' ')

print(format('∞','∞^40'))

print('\n'' ')

print(format('Thank you for using ','-^40'))
print(format('the Tipinator 5000™','-^40'))
print(format('Have An Amazing day!','♥^40'))
