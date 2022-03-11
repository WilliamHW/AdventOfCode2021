from get_aoc import get_input_lines

raw_input = get_input_lines(9)

def row_heights (line):
    #heights = [9]
    heights = []
    for number in line:
        heights.append(int(number))
    #heights.append(9)
    return heights

heights = [row_heights(line) for line in raw_input] # Can I combine the function into this line?

low_points = list()

row_above = [9] * len(heights[0])
for line in range(len(heights)):
    this_line = heights[line]
    if line < len(heights)-1:
        #print(line)
        row_below = heights[line+1]
        #print("all but last")
    else:
        print("only once")
        row_below = [9] * len(heights[0])
    if (this_line[0] < this_line[1]) and (this_line[0] < row_above[0]) and (this_line[0] < row_below[0]):
            height = this_line[hori]
            low_point = [line, hori, height]
            low_points.append(low_point)
    for hori in range(1,len(heights[line]) - 1):
        position = [line, hori]
        #print(position)
        if (this_line[hori] < this_line[hori - 1]) and (this_line[hori] < this_line[hori + 1]) and (this_line[hori] < row_above[hori]) and (this_line[hori] < row_below[hori]):#
            #print("here")
            #print(type(row_above))
            #if (this_line[hori] < row_above[hori]) and (this_line[hori] < row_below[hori]):
             #   print ("now here")
            #print("I'm here")
            height = this_line[hori]
            low_point = [line, hori, height]
            print(low_point)
            low_points.append(low_point)
        #print("hori is " + str(hori))
    hori = len(this_line) - 1
    #print("this hroi " + str(hori))
    if (this_line[hori] < this_line[hori - 1]) and (this_line[hori] < row_above[hori]) and (this_line[hori] < row_below[hori]):
            #print("this hori " + str(hori))
            height = this_line[hori]
            low_point = [line, hori, height]
            print(low_point)
            low_points.append(low_point)
    print("line is " + str(line))
    row_above = heights[line]
    if (line + 1) == len(raw_input):
        row_below = [9] * len(heights[0])
        print("got here")

sumy = 0
for point in low_points:
    sumy += point[2] + 1
    
print("Part One: the sum of the low-points height is " + str(sumy))