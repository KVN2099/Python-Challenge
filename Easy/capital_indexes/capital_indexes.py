# ALGORITHM
# Import NumPy library
# 1. Split the string into a characters array
# 2. Iterate through the array, check if character is uppercase, and store
#    character array index inside a new array
# 3. Return the list

# CODE
def capital_indexes(string):
    char_array = [ch for ch in string]
    index_array = []
    for x in range(0, len(char_array)):
        if (char_array[x].isupper()):
            index_array.append(x)
    return index_array
print(capital_indexes("HeLlO"))