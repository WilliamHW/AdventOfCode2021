from get_aoc import get_input_lines

raw_input = get_input_lines(3)
length = len(raw_input)
width = len(raw_input[1])
ox_gen = raw_input.copy()
co2 = raw_input.copy()

one_counter = list()
zero_counter = list()
for digit in range(width): # intiates a counter list
    one_counter.append(0)
zero_counter = one_counter.copy()

for line in raw_input: # loop for each line
    for digit in range(width): # loop for each digit in line
        if line[digit] == "1": # check if 1
            one_counter[digit] += 1 # increase 1 counter for that space
        else:
            zero_counter[digit] += 1

half_length = length // 2
gama = list()
epsilon = list()

for digit in range(width):
    if one_counter[digit] > half_length:
        gama.append("1")
        epsilon.append("0")
    else:
        gama.append("0")
        epsilon.append("1")

gama_string = str()
epsi_string = str()

gama_answer = int(gama_string.join(gama),2)
epsi_answer = int(epsi_string.join(epsilon),2)

print("Part One")
print(gama_answer*epsi_answer)

one_counter = list()
zero_counter = list()
for digit in range(width): # intiates a counter list
    one_counter.append(0)
zero_counter = one_counter.copy()

for digit in range(width): # Working across the columns of numbers
    lines_left = len(ox_gen) # The number of remaining numbers
    if lines_left == 1: final_oxy = ox_gen.copy()
    half_length = lines_left / 2
    for line in ox_gen:
        if line[digit] == "1": one_counter[digit] += 1
    if one_counter[digit] >= half_length:
        to_be_removed = "0"
    else:
        to_be_removed = "1"
    temp_ox_gen = list()
    for line_num in range(lines_left):
        line = ox_gen[line_num]
        x = line[digit]
        if line[digit] != to_be_removed:
            temp_ox_gen.append(line)
    ox_gen = temp_ox_gen.copy()
    #print(ox_gen)  
    lines_left2 = len(co2)
    if lines_left2 == 1: final_co2 = co2.copy()
    half_length2 = lines_left2 / 2
    for line in co2:
        if line[digit] == "0": zero_counter[digit] += 1
    if zero_counter[digit] <= half_length2:
        to_be_removed2 = "1"
    else:
        to_be_removed2 = "0"
    temp_co2 = list()
    for line_num in range(lines_left2):
        line = co2[line_num]
        x = line[digit]
        if line[digit] != to_be_removed2:
            temp_co2.append(line)
    co2 = temp_co2.copy()
    print(co2)
    #if lines_left == 1: final_oxy = ox_gen.copy()
    #if lines_left2 == 1: final_co2 = co2.copy()

lines_left = len(ox_gen) # The number of remaining numbers
if lines_left == 1: final_oxy = ox_gen.copy()
lines_left2 = len(co2)
if lines_left2 == 1: final_co2 = co2.copy()

#print(ox_gen)
#print(len(ox_gen))
gama_string = str()
epsi_string = str()

gama_answer = int(gama_string.join(final_oxy[0]),2)
epsi_answer = int(epsi_string.join(final_co2[0]),2)
print("game " + str(gama_answer))
print("epsilon " + str(epsi_answer))
print("Part Two")
print(gama_answer*epsi_answer)