# Class definitions
class NumberMemory():

    def __init__(self):
        self.dict = {} # { number : [0=last_round, 1=penultimate_round] }
        self.last_number_new = True
        self.last_number = -1


    def get_last_occurance(self, number):
        return self.dict[number][0]


    def get_penultimate_occurance(self, number):
        return self.dict[number][1]


    def register_number_on_round(self, number, rnd):

        if (not number in self.dict.keys()):
            self.last_number_new = True
            self.dict.update({number : [-1, -1]})
            self.dict[number][0] = rnd
        else:
            self.last_number_new = False
            self.dict[number][1] = self.dict[number][0]
            self.dict[number][0] = rnd

        self.last_number = number
            

    def was_last_number_new(self):
        return self.last_number_new


    def get_last_number(self):
        return self.last_number


# Get input
input_file = open("input.txt", 'r')
input_lines = input_file.readlines()


# Define vars
current_turn = 0
number_memory = NumberMemory()


# Parse
starting_numbers = input_lines[0].rstrip("\n").split(",")
for i in range(0, len(starting_numbers)):
    current_turn += 1
    num = int(starting_numbers[i])

    number_memory.register_number_on_round(num, current_turn)


# Answer 1 and 2
while (True):

    current_turn += 1

    if (current_turn == 2020 + 1):
        print("Answer 1: " + str(number_memory.get_last_number()))
        print("Calculating Answer 2 (takes 1-2 minutes")
    
    # Last round?
    if (current_turn >= 30000000 + 1):
        break
    
    # Last number was new... 
    if (number_memory.was_last_number_new()):
        # CurrentRound num = 0
        number_memory.register_number_on_round(0, current_turn)
        
    # Last number wasn't new
    else:

        # Get the two last occurances of this number
        last_num = number_memory.get_last_number()   
        last_occurance = number_memory.get_last_occurance(last_num)
        penultimate_occurance = number_memory.get_penultimate_occurance(last_num)

        # Calculate and register new number
        new_num = last_occurance - penultimate_occurance
        number_memory.register_number_on_round(new_num, current_turn)

print("Answer 2: " + str(number_memory.get_last_number()))
