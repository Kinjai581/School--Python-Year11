def getChessSquareColour(row, column):
    # If the row and colomn are out of the range (1, 8), return an empty string
    if (row < 1 or row > 8) or (column < 1 or column > 8):
        return ''
    
    # If the rows and columns match, return white
    if row % 2 == column % 2:
        return 'white'
    # Otherwise, return black if they don't match
    else: 
        return 'black'
print(getChessSquareColour(1,2)) # ---> black
print(getChessSquareColour(7,7)) # ---> white
print(getChessSquareColour(2,9)) # ---> ''
