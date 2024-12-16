# part 1
import re

f = open('input.txt')

lines = []
runningTotal = 0

# index, starting character
# def instanceFinder(y,x):
#     localTotal = 0

#     # find up, down, up-left, up-right, down-left and down-right
#     # up
#     if y >= 3:
#             if lines[y-1][x] == 'M' and lines[y-2][x] == 'A' and lines[y-3][x] == 'S':
#                 print(x,y, 'XMAS')
#                 localTotal += 1

#     # down
#     if y <= len(lines)-4:
#             if lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
#                 localTotal += 1
#                 print(x,y, 'XMAS')
           
#     # up-left
#     if y >= 3 and x >= 3:
#             if lines[y-1][x-1] == 'M' and lines[y-2][x-2] == 'A' and lines[y-3][x-3] == 'S':
#                 localTotal += 1
#                 print(x,y, 'XMAS')

#     # up-right
#     if y >= 3 and x <= len(lines[0])-4:
#             if lines[y-1][x+1] == 'M' and lines[y-2][x+2] == 'A' and lines[y-3][x+3] == 'S':
#                 localTotal += 1
#                 print(x,y, 'XMAS')

#     # down-left
#     if y <= len(lines)-4 and x >= 3:
#             if lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
#                 localTotal += 1
#                 print(x,y, 'XMAS')

#     # down-right
#     if y <= len(lines)-4 and x <= len(lines[0])-4:
#             if lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
#                 localTotal += 1
#                 print(x,y, 'XMAS')

#     return localTotal

# for line in f:
#     lines.append(line[0:-1])
    
# for line in lines:
#     runningTotal += len(re.findall("XMAS", line))
#     runningTotal += len(re.findall("SAMX", line))

# for y in range(0,len(lines)):
#     for x in range(0,len(lines[y])):
#         print(x,y)
#         if lines[y][x] == 'X':
#             runningTotal += instanceFinder(y,x)

# print(runningTotal)

# part 2

def instanceFinder(y,x):
    localTotal = 0

    if  1 <= y <= len(lines)-2 and 1 <= x <= len(lines)-2:
        if lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S' and lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S':
            localTotal += 1
# M . M
# . A .
# S . S
        if lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S' and lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M':
            localTotal += 1

# M . S
# . A .
# M . S
        if lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M' and lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M':
            localTotal += 1

# S . S
# . A .
# M . M

        if lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M' and lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S':
            localTotal += 1
# S . M
# . A .
# S . M
    return localTotal

for line in f:
    lines.append(line[0:-1])

for y in range(0,len(lines)):
    for x in range(0,len(lines[y])):
        if lines[y][x] == 'A':
            runningTotal += instanceFinder(y,x)

print(runningTotal)