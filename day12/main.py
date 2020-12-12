from enum import Enum

input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Class definitions

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Instruction():

    def __init__(self, instruction, value):
        self.instruction = instruction
        self.value = value
        return


    def __str__(self):
        return ("" + self.instruction + "" + str(self.value))
        

class Ship():

    def __init__(self):
        self.dir = Direction.EAST
        self.x = 0
        self.y = 0
        self.waypoint_x = 0
        self.waypoint_y = 0
        self.instructions = []


    def reset(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.dir = Direction.EAST


    def add_instruction(self, instruction):
        self.instructions.append(instruction)


    # Follows Answer 1 sailing instructions.
    # Returns tuple of final (x, y) position.
    def sail(self):

        self.reset()

        for i in range(0, len(self.instructions)):

            instruct = self.instructions[i].instruction
            val = int(self.instructions[i].value)

            # Move - Absolute direction
            if (instruct == "N"):
                self.y += val
            elif (instruct == "E"):
                self.x += val
            elif (instruct == "S"):
                self.y -= val
            elif (instruct == "W"):
                self.x -= val
            # Move - Relative direction
            elif (instruct == "F"):
                if (self.dir == Direction.NORTH):
                    self.y += val
                elif (self.dir == Direction.EAST):
                    self.x += val
                elif (self.dir == Direction.SOUTH):
                    self.y -= val
                elif (self.dir == Direction.WEST):
                    self.x -= val
            # Turn
            elif (instruct == "R"):
                turn_times = val / 90
                self.turn_right(turn_times)
            elif (instruct == "L"):
                turn_times = val / 90
                self.turn_left(turn_times)

        return (self.x, self.y)


    # Follows Answer 2 sailing instructions.
    # Returns tuple of final (x, y) position.
    def sail_with_waypoint(self):

        self.reset()

        for i in range(0, len(self.instructions)):

            instruct = self.instructions[i].instruction
            val = int(self.instructions[i].value)

            # Move Waypoint
            if (instruct == "N"):
                self.waypoint_y += val
            elif (instruct == "E"):
                self.waypoint_x += val
            elif (instruct == "S"):
                self.waypoint_y -= val
            elif (instruct == "W"):
                self.waypoint_x -= val
            # Move towards waypoint
            elif (instruct == "F"):
                dif_x = self.waypoint_x - self.x
                dif_y = self.waypoint_y - self.y
                self.x += (dif_x * val)
                self.y += (dif_y * val)
                self.waypoint_x += (dif_x * val)
                self.waypoint_y += (dif_y * val)
            # Rotate the waypoint
            elif (instruct == "R"):
                turn_times = val / 90
                self.rotate_waypoint_right(turn_times)
            elif (instruct == "L"):
                turn_times = val / 90
                self.rotate_waypoint_left(turn_times)

        return (self.x, self.y)


    def turn_right(self, times):
        for i in range(0, int(times)):
            if (self.dir == Direction.NORTH):
                self.dir = Direction.EAST
            elif (self.dir == Direction.EAST):
                self.dir = Direction.SOUTH
            elif (self.dir == Direction.SOUTH):
                self.dir = Direction.WEST
            elif (self.dir == Direction.WEST):
                self.dir = Direction.NORTH

                
    def turn_left(self, times):
        for i in range(0, int(times)):
            if (self.dir == Direction.NORTH):
                self.dir = Direction.WEST
            elif (self.dir == Direction.WEST):
                self.dir = Direction.SOUTH
            elif (self.dir == Direction.SOUTH):
                self.dir = Direction.EAST
            elif (self.dir == Direction.EAST):
                self.dir = Direction.NORTH


    def rotate_waypoint_right(self, times):
        for i in range(0, int(times)):
            y_to_ship = (self.y - self.waypoint_y)
            x_to_ship = (self.x - self.waypoint_x)

            self.waypoint_x = self.x + (y_to_ship * -1)
            self.waypoint_y = self.y + x_to_ship


    def rotate_waypoint_left(self, times):
        for i in range(0, int(times)):
            y_to_ship = (self.y - self.waypoint_y)
            x_to_ship = (self.x - self.waypoint_x)

            self.waypoint_x = self.x + y_to_ship
            self.waypoint_y = self.y + (x_to_ship * -1)


# Parse input
ship = Ship()
for i in range(0, len(input_lines)):
    line = input_lines[i].rstrip("\n")
    alpha = "".join(i for i in line if i.isalpha())
    number = "".join(i for i in line if i.isdigit())
    ship.add_instruction(Instruction(alpha, number))


# Answer 1
final_pos = ship.sail()
print("Answer 1: " + str(abs(final_pos[0]) + abs(final_pos[1])))


# Answer 2
final_pos = ship.sail_with_waypoint()
print("Answer 2: " + str(abs(final_pos[0]) + abs(final_pos[1])))
