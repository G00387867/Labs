# Adam Shaat
# program that outputs whether it is a weekday
# or a weekend

import datetime

now = datetime.datetime.now()
day = now.weekday()
weekend = (5, 7)
dayname ={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

# assigning to print the weekday 

print(dayname[day])
if day == weekend:
    print ("It is the weekend, yay!")
else:
    print("unfortunately today is a weekday.")
