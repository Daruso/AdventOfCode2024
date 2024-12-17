import itertools


f = open('day7\\input.txt')

lineDict = {}

for line in f:
    key, values = line[0:-1].split(':')
    # print(values.split(' '))
    lineDict[int(key)] = [int(val) for val in values[1:].split(' ')]

# print(lineDict)

operators = {'*','+'}

runningTotal = 0

for key, values in lineDict.items():
    # create permutations
    permutations = []
    for perm in itertools.product(operators, repeat=len(values) - 1):
        permutation = values[:]
        index = 0
        # Insert operators at specified positions
        for j, operator in enumerate(perm):
            permutation.insert(index + j + 1, operator)
            index +=1
        permutations.append(permutation)
    
    for perm in permutations:
        # print("Key: ", key, "Calculation:", eval(''.join(map(str,perm))))
        if (eval(''.join(map(str,perm)))) == key:
            print("Found permutation: ", perm)
            runningTotal += key


print(runningTotal)

