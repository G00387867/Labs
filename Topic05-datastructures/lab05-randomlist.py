# Program that puts 10 random numbers into
# a queue(list)
# should then output all the values in the q
# then take one number at a time print it
# and the current numbers still in the q

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print ("queue is {}".format(queue))

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print ("current Number is {} and the queue is {}".format(currentNumber, queue))

print("the queue is now empty")
