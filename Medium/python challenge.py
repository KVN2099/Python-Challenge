# PYTHON CHALLENGE - Kevin Romero
# ALGORITHM:
  # 1 Define a number variable (random number) and array      with length 5
  # 2 Define a string array with the default responses
  # 3 Define functions
  # 3 Input 5 numbers and store them in the number array
  # 4 Generate random number
  # 5 Compare each array number to the random number
  # 6 If one number in the array is less than the random      number, break the loop and provide the                  corresponding response
  # 7 If the loop is complete and no number in the array      is less than the random number, provide the             corresponding response
import sys
import curses
# Define variables
curses.setupterm()
clear = str(curses.tigetstr('clear'), 'ascii') 

r_number = 0
array_numbers = []
pos = 5
array_texts = ["The list: ", 
"The random number: ", 
" All the values in the list are greater than the randomly generated number.", 
"Not all the values in the list are greater than the randomly generated number.", 
"Please enter the ", "first", "second", "third", "fourth","fifth", " number: ", 
"Please enter a number."]

# Define functions
def inputNumber(count):
  try:
    enteredNumber = int(input(array_texts[4] + array_texts[count] + array_texts[10]))
    return enteredNumber
  except ValueError:
    return False

def clearScreen():
    sys.stdout.write(clear) 

# Input 5 numbers
while pos < 10:
  validated = inputNumber(pos)
  if validated != False:
    clearScreen()
    array_numbers.append(validated)
    pos += 1
  else:
    clearScreen()
    print(array_texts[11])

