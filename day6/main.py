input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Group class definition
class Group:

    def __init__(self):
        self.answers = {}
        self.group_count = 0

# Parse input
all_groups = []
current_group = Group()
for i in range(0, len(input_lines)):

    # New group
    if (input_lines[i] == "\n"):
        all_groups.append(current_group)
        current_group = Group()
        continue

    # Add onto current group
    line = input_lines[i].rstrip("\n")
    current_group.group_count += 1
    for j in range(0, len(line)):
        c_char = line[j]

        if (not (c_char in current_group.answers) ):
            current_group.answers.update({c_char: 0})
        
        current_group.answers[c_char] += 1

# Add last group to list
all_groups.append(current_group)

# Answer 1
ans_one = 0
for i in range(0, len(all_groups)):
    num_ans = len(all_groups[i].answers.keys())
    ans_one += num_ans
print ("Answer 1: " + str(ans_one))

# Answer 2
ans_two = 0
for i in range(0, len(all_groups)):
    
    for key in all_groups[i].answers:
        answer_count = all_groups[i].answers[key]
        if (answer_count  == all_groups[i].group_count):
            ans_two += 1
print ("Answer 2: " + str(ans_two))
