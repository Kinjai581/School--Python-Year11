q = 0
list = []
userInput = input("Enter your string here: ") # We enter the user input here
for m in userInput:
    list.append(m) # adds m to the list
for m in userInput: # nested for loop, as we didn't exit out of the loop
    x = list.count(m) # returns the number of times a specified value appears in m into the list
    
    if x == 1: # The word has to be exactly 1 character. It can be any letter or number
        q += 1 
        if q == len(userInput): 
            print("Output: True")
    else:
        print("Output: False")
        break # exits out of the loop
