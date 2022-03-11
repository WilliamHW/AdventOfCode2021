from get_aoc import get_input_lines

raw_input = get_input_lines(8)

signal = list()
output = list()
for line in raw_input:
    split_line = line.split(" | ")
    signal.append(split_line[0])
    output.append(split_line[1])
#signal, output = raw_input.split(" | ")
#print(output)

def length_string(set):
    return len(set)

def get_values(line_from_input_or_output, boolean): # format x1,y1 -> x2,y2
    """for each value in line_from_input_or_output:
        start, end = line_from_input.split()
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")"""
    values = [get_set_of_letters(value) for value in line_from_input_or_output.split()]
    if boolean == True : values.sort(key = length_string)
    #print(values)
    return values

def get_set_of_letters(individual_letter_string):
    letter_set = set()
    for letter in individual_letter_string: letter_set.add(letter)
    return letter_set

#print("outputs")
output_values = [get_values(line, False) for line in output]
#print("input signals")
signal_values = [get_values(line, True) for line in signal]

counter = 0
for each_output in output_values:
    for each_value in each_output:
        if (len(each_value) == 2) or (len(each_value) == 3) or (len(each_value) == 4 or (len(each_value) == 7)):
            counter += 1
            #print(each_value)
            
print("Part One: Number of 2,3,4 or 7 length output answers (numbers 1, 7, 4 or 8) is " + str(counter))

def get_empty_key():
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    empty_temp_value = "_"
    key = dict.fromkeys(letters, empty_temp_value)
    return key

def find_numbers(signal_input):
    key = get_empty_key()
    for number in signal_input:
        if len(number) == 2 : one = number
        if len(number) == 3 :
            seven = number
            key["a"] = seven.difference(one).pop()          
        if len(number) == 4 : four = number
        if len(number) == 5 and len(number.intersection(one)) == 2 : three = number
        elif len(number) == 5 and len(number.intersection(four)) == 3 : five = number
        elif len(number) == 5 : two = number
        if len(number) == 6 and len(number.intersection(four)) == 4 : nine = number
        elif len(number) == 6 and len(number.intersection(seven)) == 3 : zero = number
        elif len(number) == 6 : six = number
        if len(number) == 7 :
            eight = number
            key["d"] = eight.difference(zero).pop()  
    key["c"] = eight.difference(six).pop()
    key["e"] = eight.difference(nine).pop()
    #temp_f = {key["b"]} # Can this go directly into the line below?
    key["f"] = one.intersection(six).pop()
    temp_four_seven = four.union(seven)
    key["g"] = nine.difference(temp_four_seven).pop()
    temp_one_two = one.union(two)
    key["b"] = eight.difference(temp_one_two).pop()
    key_reversed = reverse_dictionary(key)
    return key_reversed

def reverse_dictionary(key):
    key_reversed = get_empty_key()
    for entry in key:
        value = key[entry]
        key_reversed[value] = entry
    #print(key)
    #print(key_reversed)
    return key_reversed
    

def get_number(key, letters): #letters is a set?
    #print(letters)
    #print(key)
    if len(letters) == 2 : number = 1
    elif len(letters) == 3 : number = 7
    elif len(letters) == 4 : number = 4
    elif len(letters) == 7 : number = 8
    else:
        temp_set = set()
        for letter in letters:
            temp_set.add(key[letter])
        if len(letters) == 5 :
            two = {'a', 'c', 'd', 'e', 'g'}
            three = {'a', 'c', 'd', 'f', 'g'}
            five = {'a', 'b', 'd', 'f', 'g'}
            if len(temp_set.difference(two)) == 0 : number = 2
            elif len(temp_set.difference(three)) == 0 : number = 3
            elif len(temp_set.difference(five)) == 0 : number = 5
            else: print("I've screwed up")
        elif len(letters) == 6 :
            zero = {'a', 'b', 'c', 'e', 'f', 'g'}
            six = {'a', 'b', 'd', 'e', 'f', 'g'}
            nine = {'a', 'b', 'c', 'd', 'f', 'g'}
            if len(temp_set.difference(zero)) == 0 : number = 0
            elif len(temp_set.difference(six)) == 0 : number = 6
            elif len(temp_set.difference(nine)) == 0 : number = 9
        else:
            print("I've screwed up")
            number = 666
    #print(number)
    return str(number)



counter = 0
for line_number in range(len(signal_values)):
    key = find_numbers(signal_values[line_number])
    output_value = output_values[line_number]
    #number_string = ""
    #print("my string is" + number_string)
    temp_list = list()
    for output in output_value:
        temp_list.append(get_number(key, output))
        #print(temp_list)
        number_string = "".join(temp_list)
        #print(number_string)
        #print("my string is" + number_string)

        #number_string.join(get_number(key, output))
    counter += int(number_string)

print("Part Two: the sum of the output values is " + str(counter))