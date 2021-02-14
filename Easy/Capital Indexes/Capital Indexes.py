def capital_indexes(string):
    char_array = [ch for ch in string]
    index_array = []
    for x in range(0, len(char_array)):
        if (char_array[x].isupper()):
            index_array.append(x)
    return index_array
print(capital_indexes("HeLlO")) # Returns "HLO"