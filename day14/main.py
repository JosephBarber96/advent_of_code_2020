input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

#                   #
# Utility functions #
#                   #

def binary_value_at_index(index):
    ret_val = 1
    if (index == 1):
        return ret_val

    for i in range(0, index - 1):
        ret_val *= 2

    return ret_val


def number_to_binary36string(number):

    current_value = number
    starting_string = "0" * 36

    for i in range(36, 0, -1):
        this_index_val = binary_value_at_index(i)
        if (current_value >= this_index_val):
            current_value -= this_index_val
            str_list_cpy = list(starting_string)
            str_list_cpy[i-1] = "1"
            starting_string = "".join(str_list_cpy)

    return starting_string

def binary36string_to_int(str_val):
    value = 0

    for i in range(0, 36):
        if (str_val[i] == "1"):
            value += binary_value_at_index(i+1)

    return value


def apply_mask_to_value(number, mask):

    for i in range(0, len(number)):
        if (mask[i] == "1"):
            str_as_list = list(number)
            str_as_list[i] = "1"
            number = "".join(str_as_list)
        elif (mask[i] == "0"):
            str_as_list = list(number)
            str_as_list[i] = "0"
            number = "".join(str_as_list)

    return number


def apply_mask_to_memaddress(address, mask):

    for i in range(0, len(address)):
        if (mask[i] == "1"):
            str_as_list = list(address)
            str_as_list[i] = "1"
            address = "".join(str_as_list)
        elif (mask[i] == "0"):
            pass
        elif (mask[i] == "X"):
            str_as_list = list(address)
            str_as_list[i] = "X"
            address = "".join(str_as_list)

    return address
    

def get_all_floating_binary_possibilities(current_str, current_list, current_index):

    append = True

    # Loop from the current index to look for the next X
    for i in range(current_index, len(current_str)):

        if (current_str[i] == "X"):

            # Create 2 copies of the string
            # Set X to 1 and X to 0 for each respective string
            # Continue the search recursively, until we reach the end]
            zero_lst = list(current_str)
            zero_lst[i] = "0"
            zero_str = "".join(zero_lst)
            get_all_floating_binary_possibilities(zero_str, current_list, i+1)


            one_lst = list(current_str)
            one_lst[i] = "1"
            one_str = "".join(one_lst)
            get_all_floating_binary_possibilities(one_str, current_list, i+1)

            append = False
            break

            
    # When we reach the end of the string, add it to the list
    if (append):
        current_list.append(current_str)


#
# Answer 1
#

current_mask = ""
mem = {}

for i in range(0, len(input_lines)):
    line = input_lines[i].rstrip("\n")
    
    # Mask
    if ("mask" in line):
        current_mask = line.split("=")[1].rstrip(" ")[::-1] 
        
    # Set memory val
    else:

        # Grab the memory-address and desired value from the string
        mem_index = int(line.split("[")[1].split("]")[0])
        new_val = int(line.split("=")[1].rstrip(" "))

        # Apply the mask to the desired value, represented as a string
        as_binary_string = number_to_binary36string(new_val)
        num_with_mask = apply_mask_to_value(as_binary_string, current_mask)

        # Add to / Update dict
        if (not mem_index in mem.keys()):
            mem.update({mem_index : ""})
        mem[mem_index] = num_with_mask


accumulative_value = 0
for key in mem.keys():
    accumulative_value += binary36string_to_int(mem[key])
print("Answer 1: " + str(accumulative_value))


#
# Answer 2
#

current_mask = ""
mem = {}

for i in range(0, len(input_lines)):
    line = input_lines[i].rstrip("\n")
    
    # Mask
    if ("mask" in line):
        current_mask = line.split("=")[1].rstrip(" ")[::-1]
        # print("new mask: " + current_mask)
        
    # Set memory val
    else:

        # Grab the memory-address and desired value from the string
        mem_address = int(line.split("[")[1].split("]")[0])
        new_val = int(line.split("=")[1].rstrip(" "))

        # Represent mem address as string
        mem_addr_string = number_to_binary36string(mem_address)

        # Apply the mask to the memory address
        address_with_mask = apply_mask_to_memaddress(mem_addr_string, current_mask)

        # Get all possible mem_address values (as a result of the floating bits)
        all_mem_addresses = []
        get_all_floating_binary_possibilities(address_with_mask, all_mem_addresses, 0)

        # For each possibility, write into that memory address
        new_val_as_string = number_to_binary36string(new_val)
        for j in range(0, len(all_mem_addresses)):
            this_addr = all_mem_addresses[j]
            if (not this_addr in mem.keys()):
                mem.update({this_addr:0})
            mem[this_addr] = new_val_as_string

accumulative_value = 0
for key in mem.keys():
    accumulative_value += binary36string_to_int(mem[key])
print("Answer 2: " + str(accumulative_value))

