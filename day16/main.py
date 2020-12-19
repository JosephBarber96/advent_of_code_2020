from enum import Enum

# Enum definitions

class ParseMode(Enum):
    VALID_TICKET_INFO = 0
    OWN_TICKET = 1
    NEARBY_TICKETS = 2


# Class definitions 

class NumberBoundary():

    def __init__(self, lower, higher):
        self.min = lower
        self.max = higher



class TicketDetail():

    def __init__(self, field_name, bounds):
        self.name = field_name
        self.boundaries = bounds
        self.valid_column_entries = {}

    
    def is_number_valid(self, num):

        for boundary in self.boundaries:
            if (num >= boundary.min and num <= boundary.max):
                return True

        return False


    def register_valid_column_entry(self, col):

        if (not col in self.valid_column_entries.keys()):
            self.valid_column_entries.update({col: 0})

        self.valid_column_entries[col] += 1


class Ticket():

    valid_ticket_details = []
    all_tickets = []

    def __init__(self, vals):
        self.values = vals
        Ticket.all_tickets.append(self)


    def check_validity(self):

        invalid_values = []

        # Loop through each ticket value
        for value in self.values:

            # See if this value meets the criteria for any details
            this_val_valid = False
            for detail in Ticket.valid_ticket_details:

                # Get the valid boundaries for this detail
                # Check it fits into atleast one boundary
                for boundary in detail.boundaries:
                    if (value >= boundary.min and value <= boundary.max):
                        this_val_valid = True

            if (not this_val_valid):
                invalid_values.append(int(value))

        return invalid_values



# Var definition

parse_mode = ParseMode.VALID_TICKET_INFO
own_ticket = None
valid_tickets = []


# Functions 

def ParseNumerBounary(text_data):

    dat = text_data.rstrip("\n").rstrip(" ")
    l = dat.split("-")[0]
    r = dat.split("-")[1]
    return NumberBoundary(int(l), int(r))


def ParseInput(lines):
    global parse_mode
    global own_ticket

    for i in range(0, len(lines)):

        line = lines[i].rstrip("\n")

        # Check for move onto next mode
        if (line == ""):
            if (parse_mode == ParseMode.VALID_TICKET_INFO):
                parse_mode = ParseMode.OWN_TICKET
            elif (parse_mode == ParseMode.OWN_TICKET):
                parse_mode = ParseMode.NEARBY_TICKETS
            continue

        # Valid ticket info
        if (parse_mode == ParseMode.VALID_TICKET_INFO):
            field_name = line.split(":")[0]
            values = line.split(":")[1]
            l_vals = values.split("or")[0]
            r_vals = values.split("or")[1]

            det = TicketDetail(field_name, [ParseNumerBounary(l_vals), ParseNumerBounary(r_vals)])
            Ticket.valid_ticket_details.append(det)
        
        # Own ticket
        elif (parse_mode == ParseMode.OWN_TICKET):
            if ("your ticket" in line):
                continue

            nums_as_str = line.split(",")
            nums_as_int = []
            for j in range(0, len(nums_as_str)):
                nums_as_int.append(int(nums_as_str[j]))

            own_ticket = Ticket(nums_as_int)
            
        # Nearby tickets
        elif (parse_mode == parse_mode.NEARBY_TICKETS):
            if ("nearby tickets" in line):
                continue

            nums_as_str = line.split(",")
            nums_as_int = []
            for j in range(0, len(nums_as_str)):
                nums_as_int.append(int(nums_as_str[j]))

            Ticket(nums_as_int)


# Get input
input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Parse
ParseInput(input_lines)

# Answer 1
error_rate = 0
for ticket in Ticket.all_tickets:

    if (ticket is own_ticket):
        continue

    inv_values = ticket.check_validity()

    if (len(inv_values) == 0):
        valid_tickets.append(ticket)
    else:
        for val in inv_values:
            error_rate += val

print("Answer 1: " + str(error_rate))


# Answer 2
num_valid = len(valid_tickets)

# A dictionary which uses the detail_name as the key, 
# and the value is a list of column index which have been ruled out
invalid_possibilities = {}

# A dictionary which stores the set of available answers against the detail_name
available_answers = {}

# A dictionary which stores the column against the detail_name
final_answer = {}

# Build up the dictionaries
for detail in Ticket.valid_ticket_details:
    invalid_possibilities.update({ detail.name : [] })
    available_answers.update({ detail.name : [] })
    final_answer.update({ detail.name : [] })


# For each ticket...
for ticket in valid_tickets:

    # For each value
    for x in range(0, len(ticket.values)):
        col = x
        val = ticket.values[x]

        # Check it against each detail
        for detail in Ticket.valid_ticket_details:

            # Does the value in column 'x' fit into detail?
            # If not: register it into the dictionry
            if (not detail.is_number_valid(val)):
                invalid_possibilities[detail.name].append(col)


# Now, search the dictionary, and get a set for each key showing only possible possibilities
all_possible = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
for key in invalid_possibilities.keys():

    all_possibilities = set(all_possible)
    cannot_be = set(invalid_possibilities[key])
    can_be = all_possibilities.difference(cannot_be)

    # Set the value to the set of possible answers
    available_answers[key] = can_be


# Loop, assigning the only valid row, until everything is assigned
loop_counter = 0
while True:

    loop_counter += 1

    if (loop_counter >= 21):
        break

    lowest_key = ""
    lowest_entry_count = len(all_possible) + 1

    # Look for the set with the lowest number of possibilities
    for key in available_answers.keys():
        num_valid = len(available_answers[key])
        if (num_valid < lowest_entry_count):
            lowest_entry_count = num_valid
            lowest_key = key

    # Grab the value from the set
    possible_val = next(iter(list(available_answers[lowest_key])))

    # This is now the answer to this key
    final_answer[lowest_key] = possible_val

    # Remove this key from the dictionaries
    del available_answers[lowest_key]

    # Remove this value from the sets of all other dict entries
    for key in available_answers.keys():
        if (possible_val in available_answers[key]):
            available_answers[key].remove(possible_val)


# Now we have a dictionary which stores which column index of ticket values belong to which ticket detail
# Look for each ticket detail starting with the word 'departure' and get the that details value on my ticket
# multiply these togetether
dept_values = []
for key in final_answer.keys():
    if ("departure" in key):
        column = final_answer[key]
        dept_values.append(own_ticket.values[column])

print(dept_values)

final_dept_product = dept_values[0]
for i in range(1, len(dept_values)):
    final_dept_product *= dept_values[i]
