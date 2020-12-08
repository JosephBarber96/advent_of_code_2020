input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Class definitions

class Instruction():

    def __init__(self, instruction, val):
        self.i_type = instruction
        self.value = value
        self.execute_count = 0

class Program():

    def __init__(self):
        self.accumulator = 0
        self.instructions = []

    def add_instruction(self, instuction_type, val):
        new_instuction = Instruction(instruction_type, val)
        self.instructions.append(new_instuction)

    # Executes each instruction until it hits a duplicate or program terminates at the final instruction. 
    # Returns tuple (bool, int) where bool=terminated_at_end and int=accumulator_value.
    def execute_program(self):

        self.reset_program()
        
        index = 0
        while (True):
            instruction = self.instructions[index]
            increment_index = True

            # Exit check - program loop
            if (instruction.execute_count > 0):
                return (False, self.accumulator)

            # Perform instruction
            if (instruction.i_type == "nop"):
                pass
            elif (instruction.i_type == "acc"):
                self.accumulator += instruction.value
            elif (instruction.i_type == "jmp"):
                index += instruction.value
                increment_index = False

            # Increment behaviour
            if (increment_index):
                index += 1
            instruction.execute_count += 1

            # Exit check - final instruction
            if (index >= len(self.instructions)):
                return(True, self.accumulator)


    def reset_program(self):
        self.accumulator = 0
        for i in range(0, len(self.instructions)):
            self.instructions[i].execute_count = 0
        

    def mutate_until_terminate(self):

        for i in range(0, len(self.instructions)):
            original_type = self.instructions[i].i_type

            # Mutate
            if (original_type == "jmp"):
                self.instructions[i].i_type = "nop"
            elif (original_type == "nop"):
                self.instructions[i].i_type = "jmp"

            # Check
            vals = self.execute_program()
            if (vals[0] == True):
                return vals[1]

            # Return state
            self.instructions[i].i_type = original_type
        
        return "Failed to find answer"
        

# Parse input into instructions
program = Program()
for i in range(0, len(input_lines)):
    line = input_lines[i].rstrip("\n")

    instruction_type = line.split(" ")[0]
    value_type = line.split(" ")[1][0]
    value = int(line.split(" ")[1].lstrip("+").lstrip("-"))
    if (value_type == "-"):
        value = -value

    program.add_instruction(instruction_type, value)

# Answer 1
accumulator_value = program.execute_program()[1]
print("Answer 1: " + str(accumulator_value))

# Answer 2
accumulator_value = program.mutate_until_terminate()
print("Answer 2: " + str(accumulator_value))
