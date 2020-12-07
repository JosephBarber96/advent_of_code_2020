input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

#
# Class definitions
#
class Bag:

    # Static
    all_bags = {}

    def __init__(self, identifier):
        self.id = identifier
        self.children = {}
        
        Bag.all_bags.update({self.id : self})

class BagCounter:

    def __init__(self):
        self.count = 0

    def add(self, num):
        self.count += num

    def get_count(self):
        return self.count


#
# Parse input into Bag objects
#
for i in range(0, len(input_lines)):

    line = input_lines[i].rstrip("\n")
    
    # This bag
    bag_one = line.split("contain")[0].rstrip(" ").rstrip("s")
    current_bag = Bag(bag_one)

    # Remaining bags it can contain
    remaining_bags = line.split("contain")[1].split(",")

    for j in range(0, len(remaining_bags)):
        rem_bag_info = remaining_bags[j].lstrip(" ").rstrip(".").rstrip("s")

        if ("no other bag" in rem_bag_info):
            continue
        
        num_bag = int(rem_bag_info[0])
        rem_bag_id = rem_bag_info[2:]
        current_bag.children.update({rem_bag_id : num_bag})


#
# Recursive checks
#
def check_for_id_recursive(starting_bag, current_bag, search_id, ans_list):

    if (current_bag == search_id):
        if (not (starting_bag in sgb_list)):
            sgb_list.append(starting_bag)
        return

    this_bag = Bag.all_bags[current_bag]
    for key in this_bag.children:
        check_for_id_recursive(starting_bag, key, search_id, ans_list)


def total_bag_contents_recursive(current_bag, bag_counter):

    current_bag = Bag.all_bags[current_bag]
 
    for key in current_bag.children.keys():
        num_child = current_bag.children[key]
        bag_counter.add(num_child)
        
        for i in range(0, num_child):
            total_bag_contents_recursive(key, bag_counter)


#
# Answers
#


# Answer 1
SEARCH_ID = "shiny gold bag"
sgb_list = []
for key in Bag.all_bags:
    if (key == SEARCH_ID):
        continue
    check_for_id_recursive(key, key, SEARCH_ID, sgb_list)
print("Answer 1: " + str(len(sgb_list)))

# Answer 2
bag_counter = BagCounter()
total_bag_contents_recursive(SEARCH_ID, bag_counter)
print("Answer 2: " + str(bag_counter.get_count()))
