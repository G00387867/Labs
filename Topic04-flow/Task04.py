# Program that asks the user to input any positive integer and
#  outputs the successive value of the following calculation.
# It should at each step calculate the next value by taking the current value
# if the it is even, divide it by two, if it is odd, multiply
# it by three and add one
# the program ends if the current value is one.

numbers = []

# first number and then check if it has a positive value
number = int(input("please enter a number: " ))

while number > 0:

for value in numbers:
    print(value)

# checking if it is an even integer

if number%2:
    print(({}/2).format(number))
else:
    print(({} * 3 )+ 1).format(number)

while number ==1:
    for value in numbers:
        print (value)
