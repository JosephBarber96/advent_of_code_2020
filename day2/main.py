input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

def parse_line(full_line):
    LOWER_NUMBER = 0
    UPPER_NUMBER = 1
    CHARACTER = 2
    PASSWORD = 3

    current_state = LOWER_NUMBER

    lower_case_str = ""
    upper_case_str = ""
    char_str = ""
    pass_str = ""

    # Parse
    for i in range(0, len(full_line)):

        if (current_state == LOWER_NUMBER):
            
            if (full_line[i] == '-'):
                current_state = UPPER_NUMBER
                continue
            
            lower_case_str += full_line[i]

        elif (current_state == UPPER_NUMBER):

            if (full_line[i] == ' '):
                current_state = CHARACTER
                continue

            upper_case_str += full_line[i]

        elif (current_state == CHARACTER):

            if (full_line[i] == ':'):
                current_state = PASSWORD
                continue

            char_str += full_line[i]

        elif (current_state == PASSWORD):

            if (full_line[i] == ' '):
                continue

            pass_str += full_line[i]

    return int(lower_case_str), int(upper_case_str), char_str, pass_str
    

def is_pass_valid_one(full_line):

    parse = parse_line(full_line)

    lower_allowance = parse[0]
    upper_allowance = parse[1]
    char = parse[2]
    password = parse[3]
    
    char_count = password.count(char)
    return (char_count >= lower_allowance and char_count <= upper_allowance)

def is_pass_valid_two(full_line):

    parse = parse_line(full_line)

    left_index = parse[0]
    right_index = parse[1]
    char = parse[2]
    password = parse[3]

    is_left = password[left_index - 1] == char
    is_right = password[right_index - 1] == char
    is_both = is_left and is_right

    return ( (is_left or is_right) and not is_both)

# Answer 1
num_valid = 0
for i in range(0, len(input_lines)):
    if (is_pass_valid_one(input_lines[i])):
        num_valid+=1
print("Answer 1: " + str(num_valid))

# Answer 2
num_valid = 0
for i in range(0, len(input_lines)):
    if (is_pass_valid_two(input_lines[i])):
        num_valid+=1
print("Answer 2: " + str(num_valid))

