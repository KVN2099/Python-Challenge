'''
In this program, rows can be stored as:
- Strings: '123456789'
- Lists: ['1', '2', '3', '4', '5', '6', '7', '8', '9']
'''
# Stored as string: '295743861'
sample1 = ['295743861',
        '431865927',
        '876192543',
        '387459216',
        '612387495',
        '549216738',
        '763524189',
        '928671354',
        '154938672']
# Stored as list: ['1', '2', '3', '4', '5', '6', '7', '8', '9']
sample2 = [[char for char in '195743862'],
        [char for char in '431865927'],
        [char for char in '874192546'],
        [char for char in '387459216'],
        [char for char in '612387495'],
        [char for char in '549216738'],
        [char for char in '763524189'],
        [char for char in '928671354'],
        [char for char in '154938672']]
        
def repeated(array):
    for row in array: # Iterate each row
        found = []
        for digit in row: # Iterate each value
            if digit not in found: # Store found values
                found.append(digit) # Check if current value is already found
            else:
                return True
    return False

def check_sudoku(sud):
    # Check rows
    if repeated(sud):
        return 'No'
    # Check columns
    nth_digit = []
    for i in range(9):
        nth_digit.append([row[i] for row in sud]) # Extract and store i-th value of each column
    if repeated(nth_digit):
        return 'No'
    # Check sub-squares
    sub_square = []
    sub = []
    for k in range(0,7,3): # Iterate sub-squares vertically
        for p in range(0,7,3): # Iterate sub-squares horizontally
            for i in range(0+k,3+k): # Iterate sub-square column
                for j in range(0+p,3+p): # Iterate sub-square row
                    sub.append(sud[i][j])
            sub_square.append(sub)
            sub = []
    if repeated(sub_square):
        return 'No'
    return 'Yes'
        
print(check_sudoku(sample1)) # Yes
print(check_sudoku(sample2)) # No
