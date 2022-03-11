from get_aoc import get_input

raw_input = get_input(13)

points, folds = raw_input.split("\n\n")
#print(points)

individual_points = [point.split(",") for point in points.split("\n")]
#individual_points = [int(number) for number in individual_points]
individual_coords = []
for x, y in individual_points:
    new_point = [int(x), int(y)]
    individual_coords.append(new_point)
#print(individual_coords)

#print(folds)
individual_folds = [instruction[11::].split("=") for instruction in folds.split("\n")]
#print(individual_folds)

highest_x = 0
highest_y = 0

for point in individual_points:
    if int(point[0]) > highest_x : highest_x = int(point[0])
    if int(point[1]) > highest_y : highest_y = int(point[1])

## Turns out I could just create the matrix directly (see line 39)
def create_grid (width, length): # creates an empty grid of the size required
    new_grid = []
    for y in range(length):
        new_line = []
        for x in range(width):
            new_line.append(False)
        new_grid.append(new_line)
    return new_grid

## dots = create_grid(highest_x, highest_y) # Empty grid

dots = [[0]*(highest_x + 1) for _ in range(highest_y + 1)]
#print(dots)
        
for x, y in individual_coords:
    dots[y][x] = 1
#print(dots)

def vertical_fold(place, dots):
    old_width = len(dots[0])
    #print(old_width)
    updated_dots = []
    first_changed_column = 2*int(place) - old_width + 1
    print("the first changed column is:")
    print(first_changed_column)
    for y in range(len(dots)):
        new_line = []
        for x in range(int(place)):
            if x >= first_changed_column:
                opposite_column = old_width - 1 - (x - first_changed_column)
                new_value = dots[y][x] + dots[y][opposite_column]
                if new_value >= 2 : new_value = 1
                new_line.append(new_value)
            else :
                new_line.append(dots[y][x])
        updated_dots.append(new_line)                 
    return updated_dots

def horizontal_fold(place, dots):
    old_length = len(dots)
    first_changed_line = 2*int(place) - old_length + 1
    print("the first changed line is:")
    print(first_changed_line)
    width = len(dots[0])
    updated_dots = []
    for y in range(int(place)):
        new_line = []
        opposite_line = old_length - y - 1
        for x in range(width):
            new_value = dots[y][x] + dots[opposite_line][x]
            if new_value >= 2 : new_value = 1
            new_line.append(new_value)
        updated_dots.append(new_line)
    return updated_dots

def count_dots(dots):
    total_dots = 0
    for y in dots:
        for x in y:
            if x > 0 : total_dots += 1
    return total_dots
    

for fold, place in individual_folds:
    temp_dots = dots.copy()
    if fold == "x" : dots = vertical_fold (place, temp_dots)
    if fold == "y" : dots = horizontal_fold (place, temp_dots)
    print("After fold " + fold + " " + place)
    print(count_dots(dots))
    #print(dots)
    
print(dots)
print("more readable")
for y in dots:
    print(y)
    

##PART ONE
# First guess 897 = too high
# Second guess 767 = too low
# After again fixing, 3rd guess was right 770