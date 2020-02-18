# Program that asks the user to input any positive integer and
#  outputs the successive value of the following calculation.
# It should at each step calculate the next value by taking the current value
# if the it is even, divide it by two, if it is odd, multiply
# it by three and add one
# the program ends if the current value is one.


# first number and then check if it has a positive value

n = int(input("please enter a number: " ))
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(n/2)
    elif n != 0:
        print((n*3)+1)
    else:
         n == 2

    print(n)
    break