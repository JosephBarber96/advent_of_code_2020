input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Globals
PREAMBLE_LENGTH = 25

# Vars
numbers = []
final_target_number = 0

# Parse input into array
for i in range(0, len(input_lines)):
    num_s = input_lines[i].rstrip("\n")
    numbers.append(int(num_s))

# Function definitions

def check_for_XMAS_invalid_num(num_array, start_index, search_target):

    for i in range(start_index, start_index + PREAMBLE_LENGTH - 1):
        for j in range(i + 1, start_index + PREAMBLE_LENGTH):
            this_sum = num_array[i] + num_array[j]
            if (this_sum == search_target):
                return True

    return False

def check_contiguous_recursive(all_numbers, current_index, current_list, target):

    # Add number at index to list
    this_number = all_numbers[current_index]
    current_list.append(this_number)

    # Check value
    current_list_value = sum(current_list)

    # Contiguous numbers found
    if (current_list_value == target):      
        return (True, current_list)

    # Too high - exit
    elif (current_list_value > target):
        return (False, current_list)

    # Last number - exit
    elif ((current_index + 1) >= len(all_numbers)-1):
        return (False, current_lsit);

    # Keep searching
    else:
        return check_contiguous_recursive(all_numbers, current_index + 1, current_list, target)
    


# Answer 1
for i in range(0, len(numbers)):

    target_num = numbers[i + PREAMBLE_LENGTH]
    found_next = check_for_XMAS_invalid_num(numbers, i, target_num)

    if (not found_next):
        final_target_number = target_num
        break
print("Answer 1: " + str(final_target_number))


# Answer 2
for i in range(0, len(numbers)):

    number_list = []
    output = check_contiguous_recursive(numbers, i, number_list, final_target_number);

    if (output[0]):
        final_list = output[1]
        final_list.sort()
        print("Answer 2: " + str(final_list[0] + final_list[len(final_list)-1]))
        break
