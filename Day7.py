import math
from get_aoc import get_input
raw_input = get_input(7) # example is 16,1,2,0,4,2,7,1,2,14
positions_string = raw_input.split(",")
positions = list()
for position in positions_string:
    positions.append(int(position))

min_position = min(positions)
max_position = max(positions)

distance = list() # Creates an empty distance array for the difference between input and an 'x' value
for x in range(len(positions)):
    distance.append(0)
distance2 = distance.copy()

distances = list() # Array (of distance array elements), that is as long as possible positions
distances2 = list()
for tested_position in range(max_position + 1): # Should go from min_position to max position, but I have 1 in my data
    for position in range(len(positions)):
        how_far = abs(positions[position] - tested_position)
        distance[position] = how_far
        distance2[position] = ((how_far*(how_far + 1))/2)
    distances.append(distance.copy())
    distances2.append(distance2.copy())

sums = list() # Creates an empty distance array for the difference between input and an 'x' value
sums2 = list()
for y in range(len(distances)):
    sumy = sum(distances[y])
    sumy2 = sum(distances2[y])
    sums.append(sumy)
    sums2.append(sumy2)

print("Part One:")
print("In position " + str(sums.index(min(sums))) + " the crabs only use " + str(min(sums)) + " fuel.") # 298 is too low

print("Part Two:")
print("When the new method the optimal position is " + str(sums2.index(min(sums2))) + " where the crabs use " + str(min(sums2)) + " fuel.") # 298 is too low


