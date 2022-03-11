from get_aoc import get_input

raw_input = get_input(4)
num_order, board_data = raw_input.split("\n\n", 1) # Splitting the data into a list
individual_boards = board_data.split("\n\n")

def make_board(rough_board_data):
    lines = rough_board_data.split("\n")
    return [split_lines(line) for line in lines]

def split_lines(lines_with_return_character):
    numbers = lines_with_return_character.split()
    return numbers

boards = [make_board(board) for board in individual_boards]
#print(boards)

def numbers_together(separated_board):
    new_board = separated_board[0]
    for line in separated_board[1:]:
        new_board.extend(line)
    return new_board

new_boards = [numbers_together(board) for board in boards]
#print(new_boards)

#for board in boards:
    #for line in

"""def clear_board(board_with_numbers):
    for number in range(25):
        board_with_numbers[number] = False
    return board_with_numbers
   
copied = new_boards.copy()
ticked = [clear_board(board) for board in copied]"""
#print(ticked)

def empty_board():
    empty = list()
    for x in range(25):
        empty.append(False)
    return empty
        
ticked = list()
for x in range(len(new_boards)):
    ticked.append(empty_board())
#    [empty_board for length in new_boards]
#print(ticked)
#print(len(ticked))
#print(boards)
def update_board(individual_ticked_board, index):
    individual_ticked_board[index] = True
    print("so I'm here")
    print("the index is " + str(index))
    return individual_ticked_board

def check_board(ticked_board, index):
    row = index // 5 # from row 0-4
    column = index % 5
    row_counter = 0
    column_counter = 0
    finished = False
    for x in range((5*row), (5*row+5)): # Checks the row
        if ticked_board[x] == True: row_counter +=1
    for y in range(column, 25, 5): # Checks the column
        if ticked_board[y] == True: column_counter += 1
    if (row_counter == 5) or (column_counter == 5): finished = True
    return finished

for number in num_order:
    for board in range(len(new_boards)):
        current_board = new_boards[board]
        try:
            place = current_board.index(number)
        except:
            #print("the number " + str(number) + " wasn't found on this board")
            pass
        else:
            ticked[board] = update_board(ticked[board], place)
            finished = check_board(ticked[board], place)
            if finished == True:
                print("That's a bingo")
                print(board)
                print(number)
                break
            
print(ticked)