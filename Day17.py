import math

#target area: x=20..30, y=-10..-5
#target = [20, 30, -10, -5]
#target area: x=143..177, y=-106..-71
target = [143, 177, -106, -71]
xmin, xmax, ymin, ymax = target
#xmin = 20
#xmax = 30
#ymin = -10 # Other way around???
#ymax = -5
#target = [xmin, xmax, ymin, ymax]
#x=143..177, y=-106..-71

min_x_velocity = math.ceil(math.sqrt(2 * xmin + 1/4) - 1/2)
max_x_velocity = xmax
min_y_velocity = ymin
#Generate array of possible test values

x = 0
y = 0

def check_hit (x_init_vel, y_init_vel, target):
    xmin, xmax, ymin, ymax = target
    #if x_init_vel < (math.sqrt(2 * xmin + 1/4) - 1/2) : return False
    x = x_init_vel
    y = y_init_vel
    x_vel = x_init_vel
    y_vel = y_init_vel
    top_point = 0
    while y >= ymin and x <= xmax:
        #print(x, y)
        if y > top_point: top_point = y
        if x >= xmin and x <= xmax and y >= ymin and y <= ymax: return True, top_point
        if x_vel > 0 : x_vel -= 1
        y_vel -= 1
        x += x_vel
        y += y_vel
    return False, top_point

#print(check_hit(7, 2, target))
#print(check_hit(6, 3, target))
#print(check_hit(9, 0, target))
#print(check_hit(17, -4, target))
#print(check_hit(6, 9, target))

test_y = min_y_velocity
something_works = True
highest_point = 0
possibilities = set()
#while something_works == True:
#    something_works = False
while test_y <= 105: #9 for example, 105 for my data
    #something_works = False
    for test_x in range(min_x_velocity, max_x_velocity+1):
        hit, high_point = check_hit(test_x, test_y, target)
        if hit == True:
            hit_coords = (test_x, test_y)
            possibilities.add(hit_coords)
            #something_works = True
            if high_point > highest_point :
                highest_point = high_point
                best_x_vel = test_x
                best_y_vel = test_y
    test_y += 1

print("The answer to PART ONE is :")
print(highest_point, best_x_vel, best_y_vel)
#Answer 1326 too low
#Right answer: 5565 17 105

answer_set = {(23,-10),(25,-9),(27,-5),(29,-6),(   22,-6),(   21,-7),(   9,0),(     27,-7),(   24,-5),(
25,-7),(   26,-6),(   25,-5),(   6,8),(     11,-2),(   20,-5),(   29,-10),(  6,3),(     28,-7),(
8,0),(     30,-6),(   29,-8),(   20,-10),(  6,7),(     6,4),(     6,1),(     14,-4),(   21,-6),(
26,-10),(  7,-1),(    7,7),(     8,-1),(    21,-9),(   6,2),(     20,-7),(   30,-10),(  14,-3),(
20,-8),(   13,-2),(   7,3),(     28,-8),(   29,-9),(   15,-3),(   22,-5),(   26,-8),(   25,-8),(
25,-6),(   15,-4),(   9,-2),(    15,-2),(   12,-2),(   28,-9),(   12,-3),(   24,-6),(   23,-7),(
25,-10),(  7,8),(     11,-3),(   26,-7),(   7,1),(     23,-9),(   6,0),(     22,-10),(  27,-6),(
8,1),(     22,-8),(   13,-4),(   7,6),(     28,-6),(   11,-4),(   12,-4),(   26,-9),(   7,4),(
24,-10),(  23,-8),(   30,-8),(   7,0),(     9,-1),(    10,-1),(   26,-5),(   22,-9),(   6,5),(
7,5),(     23,-6),(   28,-10),(  10,-2),(   11,-1),(   20,-9),(   14,-2),(   29,-7),(   13,-3),(
23,-5),(   24,-8),(   27,-9),(   30,-7),(   28,-5),(   21,-10),(  7,9),(     6,6),(     21,-5),(
27,-10),(  7,2),(     30,-9),(   21,-8),(   22,-7),(   24,-9),(   20,-6),(   6,9),(     29,-5),(
8,-2),(    27,-8),(   30,-5),(   24,-7)}

print("PART TWO")
#print("The possibilities are :")
#print(possibilities)
print("Of which there are : " + str(len(possibilities)))
#1692 too low
#Right answer is 2118

#difference = answer_set.difference(possibilities)
#print(difference)
#print(len(difference))