from get_aoc import get_input
raw_input = get_input(6) # example is 3,4,3,1,2

days = 2 # Number of days for simulation

print(raw_input)
string_ages = raw_input.split(",")
ages = list()
for age in string_ages:
    ages.append(int(age))

def new_fish(days_left):
    new_fishes = 0
    days_left = days_left-2
    if days_left > 0:
        for days in range(days_left, -1,-1):
            if (days_left == 0) or (days_left % 6 == 0):
                new_fishes += 1
                new_fishes += new_fish(days_left)
    return new_fishes

how_many_fish = 0
for fish_age in ages:
    how_many_fish += 1
    how_many_fish += new_fish(days - fish_age)
    print(how_many_fish)

print("Part Two: number of fish after " + str(days) + " days is :")
print(how_many_fish) # 391671