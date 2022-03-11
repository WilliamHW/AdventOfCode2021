from get_aoc import get_input_lines

raw_input = get_input_lines(5)

def get_instructions(line_from_input): # format x1,y1 -> x2,y2
    start, end = line_from_input.split(" -> ")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    return int(x1), int(y1), int(x2), int(y2)

instructions = [get_instructions(line) for line in raw_input]

max_x = 0
max_y = 0
for line in instructions: # Finds highest number values
    if line[0] > max_x: max_x = line[0]
    if line[2] > max_x: max_x = line[2]
    if line[1] > max_y: max_y = line[1]
    if line[3] > max_y: max_y = line[3]

def empty_board(max_x):
    line= list()
    for x in range(max_x + 1):
        line.append(0)
    return line
        
points = list()
for y in range(max_y + 1): # makes a counter board of zeros
    points.append(empty_board(max_x))
#print(points)

def mark_vert_line(points, x, y1, y2): # Marks a horizontal line on the scoring board
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    for y in range(min_y, max_y + 1):
        line = points[y]
        line[x] += 1
    return points

def mark_hori_line(points, y, x1, x2): # Marks a horizontal line on the scoring board
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    line = points[y]
    for x in range(min_x, max_x + 1):
        line[x] += 1
    points[y] = line
    return points

def mark_diagonal_line(points, x1, y1, x2, y2):
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    x = min_x
    slope = (x2-x1)/(y2-y1)
    if slope > 0 :
        for y in range(min_y, max_y +1):
            line = points[y]
            line[x] += 1
            points[y] = line
            x += 1
    if slope < 0 :
        x = max_x
        for y in range(min_y, max_y +1):
            line = points[y]
            line[x] += 1
            points[y] = line
            x -= 1        
    return points

for line in instructions: # Goes through the lines and marks them on the board
    if line[0] == line[2]:points = mark_vert_line(points, line[0], line[1], line[3])
    elif line[1] == line[3]:points = mark_hori_line(points, line[1], line[0], line[2])
    else: points = mark_diagonal_line(points, line[0], line[1], line[2], line[3])

how_many_twos = 0
for line in points:
    for x in range(len(line)):
        if line[x] >= 2: how_many_twos += 1

print("Part One")
print(how_many_twos) # Was 5585 (Now no longer correct, cause of the diagonal ones)

print("Part Two")
print(how_many_twos)
#print(points)