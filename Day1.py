from get_aoc import get_input

raw_input = get_input(1)

split_input = raw_input.split("\n") # Splitting the data into a list

numbers = [int(string) for string in split_input]

counter = 0
old_number = 1000

for number in numbers:
    if number > old_number: counter += 1
    old_number = number

print("Day One") # Answer was 1393-

print(counter)

new_counter = 0
old_window = sum(numbers[0:3])
#print(old_window)
iter_counter = 1

for number in numbers[1:-2]:
    #print(number)
    window = sum(numbers[iter_counter:iter_counter+3])
    #print(window)
    if window > old_window:
        new_counter += 1
        #print("new counter is : " + str(new_counter))
    old_window = window
    iter_counter += 1
    
print("Day Two") # Answer was 1359
print(new_counter)
    