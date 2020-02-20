# function prints out menu of commands
# function should retun what the user chose

def displayMenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/q):").strip()

    return choice
# main program
choice = displayMenu()
while(choice != "q"):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
        print("\n\nplease select either a,v or q")
    choice = displayMenu()
    
    

