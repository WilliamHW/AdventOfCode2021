from get_aoc import get_input_lines

raw_input = get_input_lines(10)
opening_characters = {'(', '{', '[', '<'}
closing_characters = {')', '}', ']', '>'}
partner = {')':'(', ']':'[', '}':'{', '>':'<'}
reverse_partner = {'(':')', '[':']', '{':'}', '<':'>'}

bad_characters = list()
open_characters = list()
incomplete_lines = list()
for line in raw_input:
    for character in line:
        #print(character)
        if character in opening_characters:
            open_characters.append(character)
            #print(open_characters)
            #print("ever here?")
        elif character in closing_characters:
            #print(open_characters)
            #print("WHY NOT?")
            if partner[character] == open_characters[-1] : open_characters.pop()
            else:
                #print("somethings fucked")
                bad_characters.append(character)
                open_characters.clear()
                break
        else: print("even more fucked")
    if open_characters:
         #print("line " + line + " incomplete")
        print(line)
        incomplete_lines.append(line)
        pass
    open_characters.clear()
print(bad_characters)

def character_points(character):
    if character == ')' : points = 3
    if character == ']' : points = 57
    if character == '}' : points = 1197
    if character == '>' : points = 25137
    return points

syntax_error_score = sum(character_points(bad_character) for bad_character in bad_characters)
    
print(syntax_error_score)

print(incomplete_lines)
print(len(incomplete_lines))

def closing_points(character):
    if character == ')' : points = 1
    if character == ']' : points = 2
    if character == '}' : points = 3
    if character == '>' : points = 4
    return points

closing_scores = []
for line in incomplete_lines:
    this_closing_score = 0
    for character in line:
        #print(character)
        if character in opening_characters:
            open_characters.append(character)
            #print(open_characters)
            #print("ever here?")
        elif character in closing_characters:
            #print(open_characters)
            #print("WHY NOT?")
            if partner[character] == open_characters[-1] : open_characters.pop()
            else:
                print("somethings fucked")
                bad_characters.append(character)
                open_characters.clear()
                break
        else: print("even more fucked")
    print(open_characters)
    reversed_open_characters = open_characters[::-1] #.reverse() ### Why doesn't reverse work???
    print("hEREE")
    print(reversed_open_characters)
    print("now here")
    for open_character in reversed_open_characters :
        opposite = reverse_partner[open_character]
        this_closing_score = this_closing_score * 5
        this_closing_score += closing_points(opposite)
        #print(this_closing_score)
        #print("line " + line + " incomplete")
    open_characters.clear()
    closing_scores.append(this_closing_score)
    print("the current closing score is " + str(closing_scores))
#print(bad_characters)
closing_scores.sort()
print(closing_scores)
print("part two")
print(closing_scores[len(closing_scores) // 2])
