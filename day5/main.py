import math

input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Define some consts
ROW_COUNT = 128
COL_COUNT = 8

def get_board_id(boarding_pass):
    global ROW_COUNT
    global COL_COUNT
    
    front_boundary = 0
    back_boundary = ROW_COUNT-1
    final_row = 0

    left_boundary = 0
    right_boundary = COL_COUNT-1
    final_column = 0

    for i in range(0, len(boarding_pass)):

        letter = boarding_pass[i]

        if (i < 7-1):
            difference = int(abs(back_boundary - front_boundary))
            half_difference = difference / 2
            half_difference = math.ceil(half_difference)

            if (letter == "F"):
                back_boundary -= half_difference
            elif (letter == "B"):
                front_boundary += half_difference

        elif (i == 7-1):
            if (letter == "F"):
                final_row = min(front_boundary, back_boundary)
            elif (letter == "B"):
                final_row = max(front_boundary, back_boundary)

        elif (i > 7-1):
            difference = int(abs(left_boundary - right_boundary))
            half_difference = difference / 2
            half_difference = math.ceil(half_difference)

            if (i == len(boarding_pass)-1):
                if (letter == "L"):
                    final_column  = min(left_boundary, right_boundary)
                elif (letter == "R"):
                    final_column = max(left_boundary, right_boundary)
            else:
                if (letter == "L"):
                    right_boundary -= half_difference
                elif (letter == "R"):
                    left_boundary += half_difference

    board_id = (final_row * 8) + final_column
    return board_id

# Answer 1
boarding_pass_list = []
for i in range(0, len(input_lines)):
    boarding_pass = input_lines[i]
    boarding_pass = boarding_pass.rstrip("\n")
    boarding_id = get_board_id(boarding_pass)
    boarding_pass_list.append(boarding_id)
boarding_pass_list.sort()
highest_id = boarding_pass_list[len(boarding_pass_list)-1]
print("Anwer 1: " + str(highest_id))

# Answer 2
for i in range(1, len(input_lines)-1):

    current_id = boarding_pass_list[i]
    next_id = boarding_pass_list[i+1]

    if ((current_id + 1) != next_id):
        print ("Answer 2: " + str(current_id + 1))
        break
