def LongestCollatz(limit):
    steps = [0 for i in range(limit + 1)]
    steps[0] = 1
    steps[1] = 1

    for number in range(2,limit + 1):
        sequence = number
        count = 0
        shortCut = 0

        while(shortCut == 0):
            if sequence % 2 == 0:
                count += 1
                sequence = sequence >> 1
            else:
                count += 2
                sequence = (3 * sequence + 1) >> 1
            if sequence < limit:
                shortCut = steps[sequence]
        steps[number] = steps[sequence] + count


    return steps.index(max(steps))

print(LongestCollatz(999999))