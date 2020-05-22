#I want to make a program that takes a list of stuff from a user, and can
#replace an index with a different input

def replace():
    items = input("please put the characters for your original list in (using spaces): ")
    #this will be what creates a list
    items = items.split()
    for i in range(len(items)):
            #This is to turn any numbers into integer format, since items.split() creates
            #a list of strings
            try:
                items[i] = int(items[i])
                #cannot directly integerfy the string of a float, so turn that into a float
            except ValueError:
                try:
                    items[i] = float(items[i])
                    #leaves it alone in case one of the elements is a word (string)
                except ValueError:
                    pass
    print(f"Your list is {items}")

    #This is to correct for if the index is negative or if it doesn't exist
    while True:
        #I turn index into an integer since indexes are always positive whole numbers
        #This is for the event that the user puts in a float for their index
        try:
            index = input("which index is the one you want to replace?")
            index = int(index)
        except ValueError:
            print("Please put in a positive whole number for your index")
            continue
        if len(items) <= index:
            print("Error, index doesn't exist, retype your list and/or index: ")
        elif index < 0:
            print("Error, your index must be positive, please re-enter your index: ")
        else:
            #This finally breaks the while loop
            break


    #this part is similar to what is in the code before to correct the elements of the list "items"
    #except it's for the replacement character in case what the user wants to replace with is not
    #a word
    replacement = input("What would you like the new character to be?")
    try:
        replacement = int(replacement)
    except ValueError:
        try:
            replacement = float(replacement)
        except ValueError:
            pass
    print("Your replacement is", replacement)

    #this second for loop actually replaces the index with the wanted character once the while loop is broken
    for i in range(len(items)):
        if i == index:
            items[i] = replacement
        else:
            pass
    return items

print("""
Hello! Welcome to list modifier 9000! This program will ask you for a list with any
characters you want, and will allow you to replace any index with a different character,
generating a new list!
""")
print("Your new list is", replace())

#Important note I learned: If I have a string of a float, for example;
#i = '1.0'
#trying i = int(i) will throw up a ValueError event though int(1.0) works fine
#In order to integerfy a string of a float, it first needs to be floated and then integerfied.
#This is why having a try/except within a try/except was necessary and possible
