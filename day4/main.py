input_file = open("input.txt", 'r')
input_lines = input_file.readlines()

#
# Passport Class Definition
#

class Passport:

    def __init__(self):
        self.birth_year = ""        # byr
        self.issue_year = ""        # iyr
        self.expiration_year = ""   # eyr
        self.height = ""            # hgt
        self.hair_colour = ""       # hcl
        self.eye_colour = ""        # ecl
        self.passport_id = ""       # pid
        self.country_id = ""        # cid

    def validate_self(self):
        self.birth_year = self.birth_year.rstrip("\n")
        self.issue_year = self.issue_year.rstrip("\n")
        self.expiration_year = self.expiration_year.rstrip("\n")
        self.height = self.height.rstrip("\n")
        self.hair_colour = self.hair_colour.rstrip("\n")
        self.eye_colour = self.eye_colour.rstrip("\n")
        self.passport_id = self.passport_id.rstrip("\n")
        self.country_id = self.country_id.rstrip("\n")

    def is_valid_one(self):
        if (self.birth_year == ""):
            return False
        if (self.issue_year == ""):
            return False
        if (self.expiration_year == ""):
            return False
        if (self.height == ""):
            return False
        if (self.hair_colour == ""):
            return False
        if (self.eye_colour == ""):
            return False
        if (self.passport_id == ""):
            return False

        return True

    def is_valid_two(self):
        byr = self.is_birth_year_valid()
        iyr = self.is_issue_year_valid()
        eyr = self.is_expiration_year_valid()
        hgt = self.is_height_valid()
        hcl = self.is_hair_colour_valid();
        ecl = self.is_eye_colour_valid()
        pid = self.is_passport_id_valid()
        cid = self.is_country_id_valid()

        return (byr and iyr and eyr and hgt and hcl and ecl and pid)
    
    def is_birth_year_valid(self):
        if (self.birth_year == ""):
            return False
        val = int(self.birth_year)
        return (val >= 1920 and val <= 2002)

    def is_issue_year_valid(self):
        if (self.issue_year == ""):
            return False
        val = int(self.issue_year)
        return (val >= 2010 and val <= 2020)

    def is_expiration_year_valid(self):
        if (self.expiration_year == ""):
            return False
        val = int(self.expiration_year)
        return (val >= 2020 and val <= 2030)

    def is_height_valid(self):
        if (self.height == ""):
            return False
        
        # Filter to get only numbers
        height_val = int("".join(filter(str.isdigit, self.height)))
        
        # Filter to get only alphabet
        measure_type = "".join(filter(str.isalpha, self.height))

        if (measure_type == "cm"):
            return (height_val >= 150 and height_val <= 193)
        elif (measure_type == "in"):
            return (height_val >= 59 and height_val <= 76)
        else:
            return False

    def is_hair_colour_valid(self):
        if (self.hair_colour == ""):
            return False

        if (self.hair_colour == ""):
            return False

        if (self.hair_colour[0] != "#"):
            return False

        if (len(self.hair_colour) != 7):
            return False

        for i in range(1, len(self.hair_colour)):

            char_valid = True
            
            v = self.hair_colour[i]

            if (v.isdigit()):
                continue

            elif (v.isalpha()):
                ascii_value = ord(v)

                if (ascii_value >= 97 and ascii_value <= 102):
                    continue
                else:
                    return False

            else:
                return False

        return True

    def is_eye_colour_valid(self):
        if (self.eye_colour == ""):
            return False

        valid_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        for i in range(0, len(valid_list)):
            if (self.eye_colour == valid_list[i]):
                return True
            
        return False

    def is_passport_id_valid(self):
        if (self.passport_id == ""):
            return False

        if (len(self.passport_id) != 9):
            return False

        for i in range(0, len(self.passport_id)):
            if (not (self.passport_id[i].isdigit())):
                return False

        return True

    
    def is_country_id_valid(self):
        return True


#
# Parse Input
#

all_passports = []
current_passport = Passport()

for i in range(0, len(input_lines)):

    # End of passport?
    if (input_lines[i] == "\n"):

        # Add
        all_passports.append(current_passport)

        # Reset
        current_passport = Passport()

        # Continue to next loop
        continue 

    # Get the key:value pairs on this line
    pairs = input_lines[i].split(" ");

    # Parse each pair
    for j in range(0, len(pairs)):
        info = pairs[j].split(":")
        key = info[0]
        val = info[1]

        if (key == "byr"):
            current_passport.birth_year = val
        elif (key == "iyr"):
            current_passport.issue_year = val
        elif (key == "eyr"):
            current_passport.expiration_year = val
        elif (key == "hgt"):
            current_passport.height = val
        elif (key == "hcl"):
            current_passport.hair_colour = val
        elif (key == "ecl"):
            current_passport.eye_colour = val
        elif (key == "pid"):
            current_passport.passport_id = val
        elif (key == "cid"):
            current_passport.country_id = val

# After loop, add final
all_passports.append(current_passport)


#
# Run validation
#

num_valid_one = 0
num_valid_two = 0
for i in range(0, len(all_passports)):

    all_passports[i].validate_self()
    
    if (all_passports[i].is_valid_one()):
        num_valid_one += 1

    if (all_passports[i].is_valid_two()):
        num_valid_two += 1

print("Answer 1: " + str(num_valid_one))
print("Answer 2: " + str(num_valid_two))
