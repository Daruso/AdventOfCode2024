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

def original_move(position, direction, visited):
    newLocation = tuple(map(sum, zip(position, direction)))
    # print("Newlocation, direction:", newLocation, direction)
    # print("Obstacle? ", grid[newLocation[1]][newLocation[0]])
    if not (0 <= newLocation[1] < grid_height and 0 <= newLocation[0] <= grid_length): # return out of bounds location to stop while loop
        grid[position[1]][position[0]] = 'X'
        # grid[newLocation[1]][newLocation[0]] = 'X'
        # visited.add((newLocation, direction))
        return newLocation, direction
    
    if grid[newLocation[1]][newLocation[0]] == '#': # do not move, only rotate
        direction = rotate_counter_clockwise(direction)
        visited.add((position, direction))

        return position, direction
        
    else: # only here should we move
        grid[position[1]][position[0]] = 'X'
        visited.add((newLocation, direction))

        return newLocation, direction

def original_movement_loop(guardPos, guardDirection):
    visited = set()
    while 0 < guardPos[1] < grid_height and 0 < guardPos[0] < grid_length:
        guardPos, guardDirection = original_move(guardPos, guardDirection, visited)
    return visited

def rotate_counter_clockwise(direction):
    return (-direction[1], direction[0])

def move(position, direction):
    new_location = tuple(map(sum, zip(position, direction)))

    if not (0 <= new_location[1] < grid_height and 0 <= new_location[0] < grid_length): # return out of bounds location to stop while loop
        return position, direction
    
    if grid[new_location[1]][new_location[0]] == '#': # do not move, only rotate
        direction = rotate_counter_clockwise(direction)
        # loops start on a rotation
        return position, direction   

    # only here should we move
    return new_location, direction

def movement_loop(guard_pos, guard_direction):
    visited = set()
    while (guard_pos, guard_direction) not in visited and 0 <= guard_pos[1] < grid_height and 0 <= guard_pos[0] < grid_length:
        visited.add((guard_pos, guard_direction))
        guard_pos, guard_direction = move(guard_pos, guard_direction)
        
    print((guard_pos, guard_direction) in visited)
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
        print(guard_pos)
    y_counter +=1

original_grid = grid.copy()

grid_length = len(grid[0])-1
# grid_length = len(grid[0])
grid_height = y_counter

original_visited = original_movement_loop(guard_pos, guard_direction)
print("Original visited: ", original_visited)


for pos, dir in original_visited:
    # if pos == original_guard_pos:
        # continue
    grid[pos[1]][pos[0]] = '#'
    print("Exploring loop: ", pos)
    # print(grid)
    running_total += movement_loop(guard_pos, guard_direction)[0]
    # reset the grid by copying the original grid lists
    grid = original_grid.copy()
    for index in range(len(original_grid)):
        grid[index] = original_grid[index].copy()
    
print(running_total)