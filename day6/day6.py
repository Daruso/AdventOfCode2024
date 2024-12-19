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
    new_location = tuple(map(sum, zip(position, direction)))

    if not (0 <= new_location[1] < grid_height and 0 <= new_location[0] < grid_length): # return out of bounds location to stop while loop
        return new_location, direction
    
    if grid[new_location[1]][new_location[0]] == '#': # do not move, only rotate
        direction = rotate_counter_clockwise(direction)
        # loops start on a rotation
        return position, direction   

    # only here should we move
    return new_location, direction

def movement_loop(guard_pos, guard_direction):
    visited = set()
    while (guard_pos, guard_direction) not in visited:
        guard_pos, guard_direction = move(guard_pos, guard_direction)
        if (guard_pos, guard_direction) in visited:
            break
        visited.add((guard_pos, guard_direction))
        
    return ((guard_pos, guard_direction) in visited), visited # return True if loop is found (visited location again), also return visited for original loop

f = open('day6\\input.txt')

grid = []
original_grid = []

visited = set()

guard_pos = (0, 0) # x,y
original_guard_pos = (0,0)
guard_direction = (0,-1) # x,y vector
y_counter = 0 # determine height
running_total = 0

for line in f:
    grid.append(list(line[0:-1]))
    if ('^' in line):
        guard_pos = (line.index('^'), y_counter)
        original_guard_pos = guard_pos
    y_counter +=1

original_grid = grid.copy()

grid_length = len(grid[0])-1
# grid_length = len(grid[0])
grid_height = y_counter

original_visited = movement_loop(guard_pos, guard_direction)[1]

for pos in original_visited:
    if pos == original_guard_pos:
        break
    grid[pos[0][1]][pos[0][0]] = '#'
    running_total += movement_loop(guard_pos, guard_direction)[0]
    grid = original_grid.copy()
    
print(running_total)