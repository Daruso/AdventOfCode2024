# part 1
# import itertools
# from operator import add, mul

# f = open('day7\\input.txt')

# operators = {add,mul}
# runningTotal = 0

# for line in f:
#     key, values = line[0:-1].split(':')
#     key = int(key)
#     values = [int(val) for val in values[1:].split(' ')]

#     # create permutations
#     for perm in itertools.product(operators, repeat=len(values) - 1):
#         total = values[0]  # save the left-most value as the start of our total
        
#         # create operation and value tuples, then evaluate
#         for (op, val) in zip(perm, values[1:]):
#             total = op(total, val)

#         # compare the value of the equation to the key
#         if total == key:
#             runningTotal += key
#             break

# print(runningTotal)

# part 2
import itertools
from operator import add, mul

def concat(a, b):
    return int(f"{a}{b}")

f = open('day7\\input.txt')

operators = {add,mul, concat}
runningTotal = 0

for line in f:
    key, values = line[0:-1].split(':')
    key = int(key)
    values = [int(val) for val in values[1:].split(' ')]

    # create permutations
    for perm in itertools.product(operators, repeat=len(values) - 1):
        total = values[0]  # save the left-most value as the start of our total
        
        # create operation and value tuples, then evaluate
        for (op, val) in zip(perm, values[1:]):
            total = op(total, val)

        # compare the value of the equation to the key
        if total == key:
            runningTotal += key
            break

print(runningTotal)