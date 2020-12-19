import sys

input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

class Bus():

    all_busses = []

    def __init__(self, id_val, bus_index):
        self.id = id_val
        self.index = bus_index
        self.wait_time = 0
        Bus.all_busses.append(self)

    def wait(self):
        self.wait_time += self.id

    def get_wait_time(self):
        return self.wait_time

    def reset(self):
        self.wait_time = 0


# Parse input
target_value = int(input_lines[0].rstrip("\n"))
busses = input_lines[1].rstrip("\n").split(",")
for i in range(0, len(busses)):
    if (busses[i] == "x"):
        continue
    bus_id_value = int(busses[i])
    temp_bus = Bus(bus_id_value, i)
    print("Bus id=" + str(bus_id_value) + " index=" + str(i))


# Answer 1
for i in range(0, len(Bus.all_busses)):
    
    this_bus = Bus.all_busses[i]
    this_bus.reset()

    while (this_bus.get_wait_time() < target_value):
        this_bus.wait()

lowest_bus = None
for i in range(0, len(Bus.all_busses)):
    if (lowest_bus == None):
        lowest_bus = Bus.all_busses[i]
    elif (Bus.all_busses[i].get_wait_time() < lowest_bus.get_wait_time()):
          lowest_bus = Bus.all_busses[i]

minutes_waiting = lowest_bus.get_wait_time() - target_value
print("Answer 1: " + str(lowest_bus.id * minutes_waiting))
    

# Slow solution which takes too long to solve
"""
# Answer 2
for i in range(0, len(Bus.all_busses)):
    Bus.all_busses[i].reset()

loops = 0
while True:

    loops += 1
    if (loops % 1000000 == 0):
        print("loops: " + str(loops))
        print("wait time: " + str(Bus.all_busses[0].get_wait_time()))

    # Increment values
    for i in range(0, len(Bus.all_busses)):
        Bus.all_busses[i].wait()

    # Check
    target = 0
    for i in range(0, len(Bus.all_busses)):
        if (Bus.all_busses[i].index == 0):
            target = Bus.all_busses[i].get_wait_time()
            i = 500

    all_correct = True
    for i in range(0, len(Bus.all_busses)):
        this_bus_wait_time = Bus.all_busses[i].get_wait_time()
        this_bus_index = Bus.all_busses[i].index

        if (this_bus_wait_time == (target + this_bus_index)):
            pass
        else:
            all_correct = False

    if (all_correct):
        print("Answer 2: " + str(starting_value))
        break
"""