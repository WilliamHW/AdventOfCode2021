from get_aoc import get_input

raw_input = get_input(2)

split_input = raw_input.split("\n") # Splitting the data into a list

instructions = [line.split() for line in split_input]
print(instructions)
#[int(string) for string in split_input]

hori = 0
depth = 0

for instruction in instructions:
    #print(instruction)
    if instruction[0] == "forward": hori = hori + int(instruction[1])
    elif instruction[0] == "down": depth = depth + int(instruction[1])
    elif instruction[0] == "up": depth = depth - int(instruction[1])
    else: "Somethings fucked"

answer = hori * depth

print("Day One")
print(hori, depth) # 2053 1033
print(answer) # 2120749

hori = 0
depth = 0
aim = 0

for instruction in instructions:
    #print(instruction)
    if instruction[0] == "forward":
        hori = hori + int(instruction[1])
        depth = depth + (int(instruction[1]) * aim)
    elif instruction[0] == "down": aim = aim + int(instruction[1])
    elif instruction[0] == "up": aim = aim - int(instruction[1])
    else: "Somethings fucked"

answer = hori * depth

print("Day Two") 
print(hori, depth, aim) # 2053 1033
print(answer) # Answer was 2138382217