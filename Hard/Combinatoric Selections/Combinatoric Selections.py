def combinatory_selection():
    count = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            result = int(factorial(n) / (factorial(r) * factorial(n - r)))
            if result > 1000000:
                count += 1
    return count
        
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

print(combinatory_selection())