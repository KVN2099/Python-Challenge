def format_number(n):
    string = [ch for ch in str(n)]
    for i in range(0, len(string) + 1)[::-3]:
        if (i != 0 and i != len(string) - 1):
            string.insert(i, ",")
    string.pop()
    return "".join(string)
        
print(format_number(100000)) # Returns 100,000