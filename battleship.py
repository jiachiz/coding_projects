from random import randint

board = []

for i in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "This is the battlefield:"
print_board(board)


rand1_row = randint(0,5)
rand1_col = randint(0,5)

rand2_row = randint(0,5)
rand2_col = randint(0,5)

for turn in range(100):

    guess_row = int(raw_input("Please enter a row: "))
    guess_col = int(raw_input("Please enter a column: "))

    if rand1_row == guess_row and rand1_col == guess_col:
        print "You hit the enemy!"
        board[guess_row][guess_col] = "#"
        print_board(board)
    elif rand2_row == guess_row and rand2_col == guess_col:
        print "You hit the enemy!"
        board[guess_row][guess_col] = "#"
        print_board(board)
    elif guess_row > len(board)-1 or guess_col > len(board)-1:
        print "That is not on the board!"
    elif board[guess_row][guess_col] == "X":
        print "You have already made that move!"
    else:
        print "You missed!"
        board[guess_row][guess_col] = "X"
        print "Turn", turn + 1
        print_board(board)

