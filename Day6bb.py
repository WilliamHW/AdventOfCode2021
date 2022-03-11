from get_aoc import get_input
raw_input = get_input(6) # example is 3,4,3,1,2

days = 256 # Number of days for simulation

print(raw_input)
string_ages = raw_input.split(",")
ages = list()
for age in string_ages:
    ages.append(int(age))
    
adults = list()
children = list()
for x in range(7):
    adults.append(0)
    children.append(0)
    
#print(adults)
for age in ages:
    adults[age] += 1
    
#print("Day 0")
#print(adults)
#print(children)
#print(sum(adults) + sum(children))

#print(adults)
for day in range(days):
    birth_time = adults[0]
    for x in range(1, 7):
        adults[x-1] = adults[x]
    adults[1] += children[0]
    adults[6] = birth_time
    for x in range(1, 7):
        children[x-1] = children[x]
    children[6] = birth_time
    print("Day " + str(day+1))
    print(adults)
    print(children)
    print(sum(adults) + sum(children))
    
    

how_many_fish = sum(adults) + sum(children)

print("Part Two: number of fish after " + str(days) + " days is :")
print(how_many_fish) # 391671