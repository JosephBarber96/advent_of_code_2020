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
print("There are " + str(num_valid) + " valid tickets")

# A dictionary which uses the detail_name as the key, 
# and the value is a list of column index which have been ruled out
invalid_possibilities = {}

# Build up the keys of the dictionry
for detail in Ticket.valid_ticket_details:
    invalid_possibilities.update({ detail.name : [] })

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


# Now, search the dictionary
for key in invalid_possibilities.keys():

    all_possibilities = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    cannot_be = set(invalid_possibilities[key])

    can_be = all_possibilities.intersection(cannot_be)

    print (key + " CANNOT BE " + str(cannot_be))
    print (key + " CAN BE " + str(can_be))