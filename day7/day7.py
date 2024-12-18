import itertools

f = open('day7\\input.txt')

operators = {'*','+'}
runningTotal = 0

for line in f:
    key, values = line[0:-1].split(':')
    key = key
    values = [val for val in values[1:].split(' ')]

    # create permutations
    for perm in itertools.product(operators, repeat=len(values) - 1):
        total = values[0]  # save the left-most value as the start of our total
        
        # create operation and value tuples, then evaluate
        for (op, val) in zip(perm, values[1:]):
            total = str(eval(''.join((total, op, val))))

        # compare the value of the equation to the key
        if total == key:
            runningTotal += int(key)
            break

print(runningTotal)