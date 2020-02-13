# This program reads in a string and stips
# any leading or trailing spaces.
# it alsoconverts all the letters to lower case
# this program also outputs the length of the original string
# and the normalised one


rawString = input("please enter a string: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print("That string normalised is : {}".format(normalisedString))
print("We reduced the input string from {} to {}".format (lengthOfRawString, lengthOfNormalised))