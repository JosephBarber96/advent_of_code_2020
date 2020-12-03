input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

row_width = len(input_lines[0])
row_count = len(input_lines)

def Slope(x_increment, y_increment):
    global input_lines
    global row_width
    global row_count

    y = 0
    x = 0
    trees = 0

    while True:

        # Move
        x += x_increment
        y += y_increment

        # Wrap
        if (x >= row_width - 1):
            x -= (row_width - 1)

        # Tree check
        if (input_lines[y][x] == '#'):
            trees += 1

        # Exit check
        if (y >= row_count - 1):
            return trees

# Answer 1
print("Answer 1: " + str(Slope(3, 1)))

# Answer 2
a = Slope(1, 1)
b = Slope(3, 1)
c = Slope(5, 1)
d = Slope(7, 1)
e = Slope(1, 2)
total_multi = a * b * c * d * e
print("Answer 2: " + str(total_multi))
