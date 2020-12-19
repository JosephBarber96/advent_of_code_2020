input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Class definitions

class ArrangementCounter():

    def __init__(self):
        self.counter = 0

    def add(self):
        self.counter += 1

    def get_count(self):
        return self.counter


# Functions

# This is a recursive function which should generate the correct answer for Part 2.
# However, this quickly becomes vastly costly and will take hours to compute.
# I will search for a better solution. 
def check_all_arrangements_recursive(all_numbers, current_arrangement, current_index, counter):

    # Check for exit 
    if (this_index == (len(all_numbers)-1)):
        counter.add()
        return

    # Create local copys to use within the function scope
    this_arrangement = list(current_arrangement)
    this_index = int(current_index)

    current_last_number = this_arrangement[len(this_arrangement)-1]

    # Check if any next number can create a new arrangement, call add on and call var
    loop_from = this_index + 1
    loop_to = len(all_numbers)
    for loop in range(loop_from, loop_to, 1):

        possible_next_number = all_numbers[loop]        
        difference = possible_next_number - current_last_number
     
        if (difference <= 3):
            this_arrangement.append(possible_next_number)
            next_index = int(loop)
            check_all_arrangements(all_numbers, this_arrangement, next_index, counter) 



def solve_one():
    one_differences = 0
    three_differences = 0
    current_voltage = 0
    for i in range(0, len(joltages)):
        next_voltage = joltages[i]
        difference = next_voltage - current_voltage

        if (difference == 1):
            one_differences += 1
        elif (difference == 3):
            three_differences += 1

        current_voltage = next_voltage
    three_differences += 1

    one_times_three = one_differences * three_differences
    return one_times_three




# Parse input
joltages = []
for i in range(0, len(input_lines)):
    joltages.append(int(input_lines[i].rstrip("\n")))
joltages.sort()

# Answer 1
print("Answer 1: " + str(solve_one()))


# Answer 2
print("Ans 2 start")
joltages.insert(0, 0)
print(joltages)
possibilities_at_index = {}
for i in range(0, len(joltages) - 2):
    
    current_joltage = joltages[i]

    possibilities_at_index.update({i:0})

    # Possible next
    for j in range(i + 1, len(joltages) - 1):
        possible_next = joltages[j]
        difference = possible_next - current_joltage

        if (difference <= 3):
            possibilities_at_index[i] += 1

print (possibilities_at_index)
final_answer = 1
counter = 0
for key in possibilities_at_index.keys():
    possible = possibilities_at_index[key]
    final_answer += counter * possible
    counter += possible
    """
    counter += 1
    remaining = len(joltages) - counter
    print("differences at " + str(joltages[key]) + " = " + str(possibilities_at_index[key]))
    final_answer += remaining * possibilities_at_index[key]
    """
print(final_answer)
# Slow, Recursive approach :-
"""
arrangement_counter = ArrangementCounter()
starting_arrangement = [0]
check_all_arrangements_recursive(joltages, starting_arrangement, -1, arrangement_counter)
final_count = arrangement_counter.get_count()
print("num arrangements: " + str(final_count)) 
"""