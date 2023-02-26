def check_userInput(s):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for c in range(0, len(s)):
        if s[c] not in lower_case and s[c] not in upper_case:
            return False
    return True

def change_string(s):
    changed = ''
    count = 1
    for c in range(0, len(s)):
        if s[c-1] == s[c].upper() or s[c-1] == s[c].lower():
            count +=1
        else:
            if count > 1:
                changed += s[c-1] + str(count)
                count = 1
            else:
                changed += s[c-1]
    #changed += s[c]
    
    # keep the changed string if it's changed, otherwise, keep userInput string
    if changed != s:
        return changed
    else:
        return s


# get user input
userInput = input("Enter a string to compress: ")
# check it only contains upper and lower case,
if check_userInput(userInput) == False:
    print("Enter permitted characters only")
else:
    #execute function and print the result
    changed_string = change_string(userInput)
    print(changed_string)

    
