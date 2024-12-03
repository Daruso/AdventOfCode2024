# Star 1:

# f = open('Day1/input.txt')



# linesLeft = []
# linesRight = []

# for line in f:
#     lines = line.split('   ')
#     linesLeft.append(lines[0])
#     linesRight.append(lines[1].split('\n')[0])

# linesLeft.sort()
# linesRight.sort()

# inputLength = len(linesLeft)
# runningTotal = 0

# for index in range(0,inputLength):
#     runningTotal += abs(int(linesLeft[index]) - int(linesRight[index]))

# print(runningTotal)



# Star 2:

f = open('Day1/input.txt')



linesLeft = []
linesRight = []

for line in f:
    lines = line.split('   ')
    linesLeft.append(int(lines[0]))
    linesRight.append(int(lines[1].split('\n')[0]))

linesRight.sort()

inputLength = len(linesLeft)
runningTotal = 0

for index in range(0,inputLength):
    runningTotal += linesLeft[index] * linesRight.count(linesLeft[index])

print(runningTotal)