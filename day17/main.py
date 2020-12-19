import copy

# Consts

NUM_CYCLES = 6

# Class definitions

class Cube():

    # A dictionary to store all cubes
    all_cubes = {}

    # The low and high bounds of x, y and z coordinates of all cubes
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    z_min = 0
    z_max = 0

    def __init__ (self, is_active, x, y, z):
        self.is_active = is_active
        self.x = x
        self.y = y
        self.z = z

        key = Cube.get_key(x, y, z)
        self.key = key
        Cube.all_cubes.update({key : self})

        Cube.register_xyz(x, y, z)


    def count_active_neighbours(self):

        active_counter = 0

        z_low = self.z - 1
        z_high = self.z + 1

        y_low = self.y - 1
        y_high = self.y + 1

        x_low = self.x - 1
        x_high = self.x + 1

        for z in range(z_low, z_high + 1):
            for y in range(y_low, y_high + 1):
                for x in range(x_low, x_high + 1):

                    if (x == self.x and y == self.y and z == self.z):
                        continue

                    if (Cube.get_cube(x, y, z).is_active):
                        active_counter += 1

        return active_counter


    @staticmethod
    def get_cube(x, y, z):

        key = Cube.get_key(x, y, z)
        if key in Cube.all_cubes:
            return Cube.all_cubes[key]
        else:
            c = Cube(False, x, y, z)
            return c

    
    @staticmethod
    def get_key(x, y, z):
        return str(x) + str(y) + str(z)


    @staticmethod
    def register_xyz(x, y, z):

        if (x < Cube.x_min):
            Cube.x_min = x
        if (x > Cube.x_max):
            Cube.x_max = x

        if (y < Cube.y_min):
            Cube.y_min = y
        if (y > Cube.y_max):
            Cube.y_max = y

        if (z < Cube.z_min):
            Cube.z_min = z
        if (z > Cube.z_max):
            Cube.z_max = z


    @staticmethod
    def active_cube_count():
        active_count = 0
        for k in Cube.all_cubes:
            if (Cube.all_cubes[k].is_active):
                active_count += 1
        return active_count


# Methods

def create_cubes(z_min, z_max, y_min, y_max, x_min, x_max):

    for z in range(z_min, z_max + 1):
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                Cube(False, x, y, z)


def cycle():

    z_min = Cube.z_min - 1
    z_max = Cube.z_max + 1

    y_min = Cube.y_min - 1
    y_max = Cube.y_max + 1

    x_min = Cube.x_min - 1
    x_max = Cube.x_max + 1

    # print("cycle: x_min=%d, x_max=%d, y_min=%d, y_max=%d, z_min=%d, z_max=%d," % (x_min, x_max, y_min, y_max, z_min, z_max))

    after = copy.deepcopy(Cube.all_cubes)

    for z in range(z_min, z_max + 1):
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):

                # Get cube, check neighbours
                this_cube = Cube.get_cube(x, y, z)
                num_active_neighbours = this_cube.count_active_neighbours()

                # Check active/inactive state, apply to copied dict
                if (this_cube.is_active):
                    if (num_active_neighbours == 2 or num_active_neighbours == 3):
                        after[this_cube.key].is_active = True
                    else:
                        after[this_cube.key].is_active = False
                elif (not this_cube.is_active):
                    if (num_active_neighbours == 3):
                        after[this_cube.key].is_active = True

    # Update all_cubes dict with the changed dict
    Cube.all_cubes = copy.deepcopy(after)


# Parse input
input_file = open("input.txt", 'r')
input_lines = input_file.readlines()


# Create cubes
array_size = len(input_lines[0].rstrip("\n")) + NUM_CYCLES * 2
print("Array size: " + str(array_size))
create_cubes(-array_size, array_size, -array_size, array_size, -array_size, array_size)
print("cubes: " + str(len(Cube.all_cubes)))
print("Cube boundaries minx=%d maxx=%d miny=%d maxy=%d minz=%d maxz=%d" % (Cube.x_min, Cube.x_max, Cube.y_min, Cube.y_max, Cube.z_min, Cube.z_max))

# Read through input, update cubes
input_x = 0
input_y = 0
for l in input_lines:
    line = l.rstrip("\n")
    for c in line:
        input_active = (c == '#')
        Cube.get_cube(input_x, input_y, 0).is_active = input_active
        input_x += 1

    input_y += 1
    input_x = 0

# Cycle
ALLOW_DEBUG_NEW = True
num_active = Cube.active_cube_count()
print("At start: " + str(num_active) + " active cubes")
for i in range(0, NUM_CYCLES):
    cycle()
    num_active = Cube.active_cube_count()
    print("After " + str(i+1) + " cycle - " + str(num_active) + " active cubes")

# Number of active cubes? 

# Note: 387 too low. 543 too high. 