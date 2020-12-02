input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

# Answer 1
ansFound = False;
for i in range(0, len(input_lines) - 1):
    x = int(input_lines[i])
    
    for j in range(i, len(input_lines)):
        y = int(input_lines[j])
        if (x + y == 2020):
            print ("Answer 1: " + str(x * y))
            ansFound = True
            break
        
    if (ansFound):
        break

# Answer 2
ansFound = False;
for i in range(0, len(input_lines) - 2):
    x = int(input_lines[i])
    
    for j in range(i, len(input_lines) - 1):
        y = int(input_lines[j])

        for k in range(j, len(input_lines)):
            z = int(input_lines[k])
        
            if (x + y + z == 2020):
                print ("Answer 2: " + str(x * y * z))
                ansFound = True
                break
            
        if (ansFound):
            break

    if (ansFound):
        break
