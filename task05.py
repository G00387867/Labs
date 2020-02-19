# Adam Shaat
# program that outputs whether it is a weekday
# or a weekend

import datetime

now = datetime.datetime.now()
day = now.weekday
weekend = (5, 7)
# assigning to only print the weekday attribute

if day == weekend:
    print ("It is the weekend, yay!")
else:
    print("unfortunately today is a weekday.")
