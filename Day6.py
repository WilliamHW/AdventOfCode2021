from get_aoc import get_input
raw_input = get_input(6)

days = 80 # Number of days for simulation

string_ages = raw_input.split(",")
ages = list()
for age in string_ages:
    ages.append(int(age))
last_day = ages

data = list()
data.append(ages)
#print(data)

new_ages = list()
for day in range(days):
    new_ages.clear()
    for fish in last_day:
        fish -= 1
        if fish >= 0: new_ages.append(fish)
        else:
            new_ages.append(6)
            new_ages.append(8)
    last_day = new_ages.copy()
    #print(new_ages)
    #data.append(new_ages.copy())
    
print("Part One: number of fish after " + str(days) + " days is :")
print(len(new_ages)) # 391671
#print(data)