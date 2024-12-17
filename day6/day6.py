# part 1

# f = open('input.txt')

# grid = []

# guardPos = (0, 0) # x,y
# guardDirection = (0,-1) # x,y vector
# yCounter = 0 # determine height
# iter = 0 # debug loop counter
# runningTotal = 0

# for line in f:
#     grid.append(list(line[0:-1]))
#     if ('^' in line):
#         guardPos = (line.index('^'), yCounter)
#         grid[yCounter][line.index('^')] = 'X' # clear the starting position
#     yCounter +=1

# gridLength = len(grid[0])-1
# gridHeight = yCounter

# def rotate_counter_clockwise(direction):
#     return (-direction[1], direction[0])

# def move(position, direction):
#     newLocation = tuple(map(sum, zip(position, direction)))
#     # print("Newlocation, direction:", newLocation, direction)
#     # print("Obstacle? ", grid[newLocation[1]][newLocation[0]])
#     if not (0 <= newLocation[1] < gridHeight and 0 <= newLocation[0] <= gridLength): # return out of bounds location to stop while loop
#         grid[position[1]][position[0]] = 'X'
#         # grid[newLocation[1]][newLocation[0]] = 'X'
#         return newLocation, direction
    
#     if grid[newLocation[1]][newLocation[0]] == '#': # do not move, only rotate
#         print("Rotating")
#         direction = rotate_counter_clockwise(direction)
#         return position, direction
        
#     else: # only here should we move
#         grid[position[1]][position[0]] = 'X'
#         return newLocation, direction

# while 0 < guardPos[1] < gridHeight and 0 < guardPos[0] < gridLength:
#     print(iter)
#     guardPos, guardDirection = move(guardPos, guardDirection)
#     print(guardPos)
#     iter+=1

# for line in grid:
#     print(''.join(line))
#     runningTotal += line.count('X')
    
# print("Finished, final position: ", guardPos)
# print(runningTotal+1)

# part 2

def rotate_counter_clockwise(direction):
    return (-direction[1], direction[0])

def move(position, direction):
    visited.add((position, direction))
    newLocation = tuple(map(sum, zip(position, direction)))

    if not (0 <= newLocation[1] < gridHeight and 0 <= newLocation[0] < gridLength): # return out of bounds location to stop while loop
        return newLocation, direction
    
    if grid[newLocation[1]][newLocation[0]] == '#': # do not move, only rotate
        direction = rotate_counter_clockwise(direction)
        # loops start on a rotation
        return position, direction   

    else: # only here should we move
        return newLocation, direction

def movementLoop(guardPos, guardDirection):
    while 0 < guardPos[1] < gridHeight and 0 < guardPos[0] < gridLength and (guardPos, guardDirection) not in visited:
        guardPos, guardDirection = move(guardPos, guardDirection)
    return (guardPos, guardDirection) in visited

f = open('day6\\input.txt')

grid = []
originalGrid = []

visited = set()

guardPos = (0, 0) # x,y
originalGuardPos = (0,0)
guardDirection = (0,-1) # x,y vector
yCounter = 0 # determine height
iter = 0 # debug loop counter
runningTotal = 0

for line in f:
    grid.append(list(line[0:-1]))
    if ('^' in line):
        guardPos = (line.index('^'), yCounter)
        originalGuardPos = guardPos
        grid[yCounter][line.index('^')] = 'X' # clear the starting position
    yCounter +=1

originalGrid = grid.copy()

gridLength = len(grid[0])-1
gridHeight = yCounter

movementLoop(guardPos, guardDirection)

originalVisited = visited.copy()

for pos in originalVisited:
    if pos == originalGuardPos:
        break
    grid[pos[0][1]][pos[0][0]] = '#'
    path = movementLoop(guardPos, guardDirection)
    grid = originalGrid.copy()
    visited.clear()
    
print("Finished, final position: ", guardPos)
print(runningTotal)
print(len(visited))