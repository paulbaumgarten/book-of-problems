
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def display_board(board):
    print(" {} | {} | {}".format(board[0],board[1],board[2]))
    print("---|---|---")
    print(" {} | {} | {}".format(board[3],board[4],board[5]))
    print("---|---|---")
    print(" {} | {} | {}".format(board[6],board[7],board[8]))

def check_for_two_of_three(board, piece, sq1, sq2, sq3):
    if (board[sq1] == piece) and (board[sq2] == piece):
        return True, sq3
    elif (board[sq1] == piece) and (board[sq3] == piece):
        return True, sq2
    elif (board[sq2] == piece) and (board[sq3] == piece):
        return True, sq1
    else:
        return False, -1

def calculate_computer_move( turn, board ):
    if turn == 1:
        # if the player took the center, we'll go for a corner, else we'll take center
        if board[4] == "X":
            return 0
        else:
            return 4
    if turn >= 3:
        # if the player has two out of three squares, find and block the empty square
        caught, goto = check_for_two_of_three(board, "X", 0, 1, 2)
        if caught and board[goto] == " ":
            return goto
        caught, goto = check_for_two_of_three(board, "X", 3, 4, 5)
        if caught and board[goto] == " ":
            return goto
        caught, goto = check_for_two_of_three(board, "X", 6, 7, 8)
        if caught and board[goto] == " ":
            return goto
        caught, goto = check_for_two_of_three(board, "X", 0, 3, 6)
        if caught and board[goto] == " ":
            return goto
        caught, goto = check_for_two_of_three(board, "X", 1, 4, 7)
        if caught and board[goto] == " ":
            return goto
        caught, goto = check_for_two_of_three(board, "X", 2, 5, 8)
        if caught and board[goto] == " ":
            return goto
        caught, goto = check_for_two_of_three(board, "X", 0, 4, 8)
        if caught and board[goto] == " ":
            return goto
        caught, goto = check_for_two_of_three(board, "X", 2, 4, 6)
        if caught and board[goto] == " ":
            return goto
        # player isn't smart enough to get two out of three. 
        return 1


print("Welcome to tic-tac-toe!")
print("The board looks like this...")
display_board([1,2,3,4,5,6,7,8,9])
print("Type the number of the square to make that move.")
print("Because I am a good host, I will let the guest go first.")
gameOver = False
turn = 0
while not gameOver:
    move = int(input("What square number is your move? "))
    move = move - 1 # Convert from 1-9 to 0-8
    if not board[move] == " ":
        print("Sorry, that square is already taken")
    else:
        board[move] = "X"
        turn += 1
        # Calculate computer move
        computer_move = calculate_computer_move( turn, board )
        print("I will go to square",(computer_move+1))
        board[computer_move] = "O"
        turn += 1
        display_board(board)
        # TODO: Check for game over
