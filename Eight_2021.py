data = open("/Users/lukasz/Desktop/Aoc 2021/Eight_2021_data.txt", "r")
counter = 0
for line in data.readlines():
    line_split = line.split()
    output = False
    for word in line_split:
        if word =='|': output = True
        elif output:
            if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7: counter += 1
print(counter)
data = open("/Users/lukasz/Desktop/Aoc 2021/Eight_2021_data.txt", "r")
check_if_num_in_dict = lambda num, dict: num in dict.values()
def decipher(digits_ciphered, digits_deciphered, segments):
    # finding the d segment using numbers 2, 3, 5 and knowledge about a and g segments
    digits_2_3_5 = [digit for digit in digits_ciphered if len(digit) == 5]
    digits_2_3_5_intersection = [segment for segment in digits_2_3_5[0] if segment in digits_2_3_5[1] and segment in digits_2_3_5[2]]
    d_segment = ''.join([segment for segment in digits_2_3_5_intersection if segment not in segments['a'] and segment not in segments['g']])
    if check_if_num_in_dict(d_segment, segments) or len(d_segment) == 2: return {}, False
    segments['d'] = d_segment
    # finding the b segment with knowledge about number 1 and d segement
    b_segment = ''.join([segment for segment in digits_deciphered[4] if segment not in segments['d'] and segment not in digits_deciphered[1]])
    if check_if_num_in_dict(b_segment, segments) or len(b_segment) == 2: return {}, False
    segments['b'] = b_segment
    # finding the f segment and 6 number at one moment with knowledge of a, b, d, e, g possible_segments
    digits_0_6_9 = [digit for digit in digits_ciphered if len(digit) == 6]
    digit_6 = ''.join([digit for digit in digits_0_6_9 if segments['a'] in digit and segments['b'] in digit and segments['d'] in digit and segments['e'] in digit and segments['g'] in digit])
    digits_deciphered[6] = digit_6
    f_segment = ''.join([segment for segment in digit_6 if not segments['a'] in segment and not segments['b'] in segment and not segments['d'] in segment and not segments['e'] in segment and not segments['g'] in segment])
    if check_if_num_in_dict(f_segment, segments) or len(f_segment) == 2: return {}, False
    segments['f'] = f_segment
    # finding the c segment which is 8 number minus all known segments
    c_segment = ''.join([segment for segment in digits_deciphered[8] if not segments['a'] in segment and not segments['b'] in segment and not segments['d'] in segment and not segments['e'] in segment and not segments['g'] in segment and not segments['f'] in segment])
    if check_if_num_in_dict(c_segment, segments) or len(c_segment) == 2: return {}, False
    segments['c'] = c_segment
    # Finally deciphering all digits
    digits_deciphered[0] = segments['a'] + segments['b'] + segments['c'] + segments['e'] + segments['f'] + segments['g']
    digits_deciphered[2] = segments['a'] + segments['c'] + segments['d'] + segments['e'] + segments['g']
    digits_deciphered[3] = segments['a'] + segments['c'] + segments['d'] + segments['f'] + segments['g']
    digits_deciphered[5] = segments['a'] + segments['b'] + segments['d'] + segments['f'] + segments['g']
    digits_deciphered[9] = segments['a'] + segments['b'] + segments['c'] + segments['d'] + segments['f'] + segments['g']
    return digits_deciphered, True
added_outputs = 0
for line in data.readlines():
    input_values = []
    output_values = []
    numbers = {}
    line_split = line.split()
    output = False
    for word in line_split:
        if word =='|': output = True
        elif output: output_values.append(word)
        else:
            if len(word) == 2: numbers[1] = word
            elif len(word) == 3: numbers[7] = word
            elif len(word) == 4: numbers[4] = word
            elif len(word) == 7: numbers[8] = word
            else: input_values.append(word)
    segments = {}
    # finding the a segment
    segments['a'] = ''.join([segment for segment in numbers[7] if segment not in numbers[1]])
    # Calculating the e segment as one of two possible and assigning the other value to the g segment
    possible_segments = [segment for segment in numbers[8] if segment not in numbers[7] and segment not in numbers[4]]
    segments['e'] = ''.join(possible_segments[0])
    segments['g'] = ''.join(possible_segments[1])
    digits_deciphered, deciphered_correctly = decipher(input_values, numbers, segments)
    if not deciphered_correctly:
        segments['e'] = ''.join(possible_segments[1])
        segments['g'] = ''.join(possible_segments[0])
        digits_deciphered, deciphered_correctly = decipher(input_values, numbers, segments)
    inv_digits_deciphered = {''.join(sorted(v)): k for k, v in digits_deciphered.items()}
    current_output = ''
    for digit in output_values:
        current_output += str(inv_digits_deciphered[''.join(sorted(digit))])
    added_outputs += int(current_output)
print(added_outputs)
