x = ""
userInput = input('Enter string: ')
for a in range(len(userInput)):
    if userInput[a] == ' ': # if the string has a space, we are going to replace it with %20
        x += '%20' # this is the substring we are going to replace our spaces with
    else:
        x += userInput[a] # If the string does not have any spaces, it will print the string itself
print(x)
