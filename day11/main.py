from copy import deepcopy

input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Process input
seat_layout = []
for i in range(0, len(input_lines)):
    line = input_lines[i].rstrip("\n")
    seat_layout.append([])
    for j in range(0, len(line)):
        seat_layout[i].append(line[j])


def compare_grids(l_grid, r_grid):

    # Assumes they are the same width and height
    height = len(l_grid)
    width = len(l_grid[0])
    
    for y in range(0, height):
        for x in range(0, width):
            
            if (l_grid[y][x] != r_grid[y][x]):
                return False

    return True


def conways_game_of_life(grid):

    old_grid = deepcopy(grid)
    new_grid = deepcopy(grid)

    height = len(grid)
    width = len(grid[0])

    for y in range(0, height):
        for x in range(0, width):

            if (old_grid[y][x] == '.'):
                continue

            occupied_adjacent = 0

            # Up
            if (y > 0 and old_grid[y-1][x] == '#'):
                occupied_adjacent += 1
            # Up Right
            if (y > 0 and x < width-1 and old_grid[y-1][x+1] == '#'):
                occupied_adjacent += 1
            # Right
            if (x < width-1 and old_grid[y][x+1] == '#'):
                occupied_adjacent += 1
            # Down Right
            if (y < height-1 and x < width-1 and old_grid[y+1][x+1] == '#'):
                occupied_adjacent += 1
            # Down
            if (y < height-1 and old_grid[y+1][x] == '#'):
                occupied_adjacent += 1
            # Down left 
            if (y < height-1 and x > 0 and old_grid[y+1][x-1] == '#'):
                occupied_adjacent += 1
            # Left
            if (x > 0 and old_grid[y][x-1] == '#'):
                occupied_adjacent += 1
            # Up Left
            if (x > 0 and y > 0 and old_grid[y-1][x-1] == '#'):
                occupied_adjacent += 1

            this_empty = (grid[y][x] == 'L')

            # Empty and 0 adjacent = become occupied
            if (this_empty and occupied_adjacent == 0):
                new_grid[y][x] = '#'
                
           # Occupied and 4+ adjacent = become empty
            elif ( (not this_empty) and occupied_adjacent >= 4):
                new_grid[y][x] = 'L'
            

    if (compare_grids(old_grid, new_grid)):
        return new_grid
    else:
        return conways_game_of_life(new_grid)


def occupied_in_direction(y_start, x_start, y_dir, x_dir, grid):

    height = len(grid)
    width = len(grid[0])

    c_y = y_start;
    c_x = x_start;

    while True:
        c_y += y_dir
        c_x += x_dir

        # In bounds
        if ( (c_y <= height-1) and (c_y >= 0) and (c_x <= width-1) and (c_x >= 0) ):

            # Floor - continue
            if (grid[c_y][c_x] == '.'):
                continue

            # Occupied
            if (grid[c_y][c_x] == '#'):
                return True

            # Empty seat
            if (grid[c_y][c_x] == 'L'):
                return False
                      
        # Out of bounds 
        else:
            # print("ret oob")
            return False

    
# Conways game of life: Line of Sight edition.
# Searches for first 'valid' cell per direction instead of only adjacent cells
def conways_game_of_life_LoS(grid, depth):

    old_grid = deepcopy(grid)
    new_grid = deepcopy(grid)

    height = len(grid)
    width = len(grid[0])

    for y in range(0, height):
        for x in range(0, width):

            if (old_grid[y][x] == '.'):
                continue

            occupied_adjacent = 0

            # Up
            seat_up = occupied_in_direction(y, x, -1, 0, old_grid)
            if (seat_up):
                occupied_adjacent += 1
            # Up Right
            seat_up_right = occupied_in_direction(y, x, -1, 1, old_grid)
            if (seat_up_right):
                occupied_adjacent += 1
            # Right
            seat_right = occupied_in_direction(y, x, 0, 1, old_grid)
            if (seat_right):
                occupied_adjacent += 1
            # Down Right
            seat_down_right = occupied_in_direction(y, x, 1, 1, old_grid)
            if (seat_down_right):
                occupied_adjacent += 1
            # Down
            seat_down = occupied_in_direction(y, x, 1, 0, old_grid)
            if (seat_down):
                occupied_adjacent += 1
            # Down left
            seat_down_left = occupied_in_direction(y, x, 1, -1, old_grid)
            if (seat_down_left):
                occupied_adjacent += 1
            # Left
            seat_left = occupied_in_direction(y, x, 0, -1, old_grid)
            if (seat_left):
                occupied_adjacent += 1
            # Up Left
            seat_up = occupied_in_direction(y, x, -1, -1, old_grid)
            if (seat_up):
                occupied_adjacent += 1

            this_empty = (old_grid[y][x] == 'L')

            # Empty and 0 adjacent = become occupied
            if (this_empty and occupied_adjacent == 0):
                new_grid[y][x] = '#'
                
           # Occupied and 5+ adjacent = become empty
            elif ( (not this_empty) and occupied_adjacent >= 5):
                new_grid[y][x] = 'L'
            

    if (compare_grids(old_grid, new_grid)):
        return new_grid
    else:
        return conways_game_of_life_LoS(new_grid, depth + 1)


# Answer 1
final_grid = conways_game_of_life(seat_layout)
num_occupied = 0
for y in range(0, len(final_grid)):
    for x in range(0, len(final_grid[0])):
        if (final_grid[y][x] == '#'):
            num_occupied += 1
print("Answer 1: " + str(num_occupied))


# Answer 2
final_grid_LoS = conways_game_of_life_LoS(seat_layout, 0)
num_occupied = 0
for y in range(0, len(final_grid_LoS)):
    for x in range(0, len(final_grid_LoS[0])):
        if (final_grid_LoS[y][x] == '#'):
            num_occupied += 1
print("Answer 2: " + str(num_occupied))
