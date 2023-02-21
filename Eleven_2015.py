#I didnt count time on this one
data = "vzbxxyzz"
def check_password(password):
    first_condition = False
    letter_not_repeated = None
    first_half = False
    second_half = False
    for letter in range(len(password)):
        if password[letter] == "i" or password[letter] == "o" or password[letter] == "l":
            return False
        if letter < len(password) - 2:
            if ord(password[letter]) == ord(password[letter + 1]) - 1 and ord(password[letter + 1]) == ord(password[letter + 2]) -1:
                first_condition = True
        if letter > len(password) - 2:
            pass
        elif password[letter] == password[letter + 1] and password[letter] != letter_not_repeated:
            if first_half == True:
                second_half = True
            else:
                first_half = True
                letter_not_repeated = password[letter]
            if first_condition and first_half and second_half:
                return True
    return False
password_not_found = True
while password_not_found:
    last_character = ord(data[-1])
    last_character += 1
    character = chr(last_character)
    data = data[:-1] + character
    if check_password(data):
        password_not_found = False
        print(data)
    if last_character > 122:
        increment = True
        pointer = -2
        data = data[:-1] + "a"
        while pointer > - len(data)  and increment:
            character_increment = ord(data[pointer])
            character_increment += 1
            character = chr(character_increment)
            data = data[:pointer] + character + data[pointer + 1:]
            if check_password(data):
                password_not_found = False
                print(data)
                increment = False
            elif character_increment > 122:
                data = data[:pointer] + "a" + data[pointer + 1:]
                pointer -= 1
            else:
                increment = False
