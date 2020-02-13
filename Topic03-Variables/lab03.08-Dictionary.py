currentBook = {
    "title" : "Harry Potter eats his dinner",
    "author": "Just kidding Rowling",
    "price" : 12
}
# print dictionary object
print (currentBook)

# print jsut the author
print(currentBook["author"])

# create and set attribute ISBN
currentBook["ISBN"] = "12345"

# user for loop to iterate through the currentBook's values
# notice the order the for loop gives the values.
print ("the current book has these values:")
for value in currentBook.values() : 
    print (" =>{}".format(value))

