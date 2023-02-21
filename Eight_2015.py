#first half in 50:01
data = open("Eight_2015_data.txt", "r")
characters_in_string_code = 0
characters_in_memory = 0
for line in data.readlines():
    line = line.strip()
    characters_in_string_code += len(line)
    stripped_line = line.strip("\"")
    line_pointer = 0
    while line_pointer < len(stripped_line):
        if stripped_line[line_pointer] == "\\":
            if line_pointer == len(stripped_line) - 1:
                line_pointer += 2
            elif stripped_line[line_pointer + 1] == "x":
                line_pointer += 4
            else:
                line_pointer += 2
        else:
            line_pointer += 1
        characters_in_memory += 1
print(characters_in_string_code - characters_in_memory)
# second half in 1:15:54
data_2 = open("Eight_2015_data.txt", "r")
characters_in_encoded_string = 0
characters_in_original_string = 0
for line in data_2.readlines():
    line = line.strip()
    characters_in_original_string += len(line)
    line = line[1:-1]
    if len(line) == 0:
        characters_in_encoded_string += 6
    else:
        characters_in_encoded_string += 4
        line_pointer = 0
        while line_pointer < len(line):
            if line_pointer == len(line) - 1:
                characters_in_encoded_string += 2
            if line[line_pointer] == "\\":
                if line_pointer == len(line) - 1:
                    characters_in_encoded_string += 2
                    line_pointer += 1
                elif line[line_pointer + 1] == "\"" and line_pointer + 1 == len(line) - 1:
                    characters_in_encoded_string += 6
                    line_pointer += 2
                elif line[line_pointer + 1] == "\"":
                    characters_in_encoded_string += 4
                    line_pointer += 2
                else:
                    characters_in_encoded_string += 2
                    line_pointer += 1

            else:
                characters_in_encoded_string += 1
                line_pointer += 1
print(characters_in_encoded_string - characters_in_original_string)
