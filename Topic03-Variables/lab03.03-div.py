# program that reads in two numbers and
# outputs the integer answer and remainder

x = int(input("Enter frst number: "))
y =  int(input("Enter second number"))
answer = int(x/y)
remainder = x%y


print("{} divided by {} is {} with remainder {}".format(x, y,
 answer, remainder))
 