board = {7:'',8:'',9:'', 4:'',5:'',6:'', 1:'',2:'',3:''}

winning_combos = [[7,8,9], [4,5,6], [1,2,3], [1,4,7], [2,5,8], [3,6,9], [3,5,7], [1,5,9]]

turn = 'x'

# function that prints to board.
def print_board():
    print(board[7] , ' |' , board[8] , '|' , board[9])
    print('---------')
    print(board[4] , ' |' , board[5] , '|' , board[6])
    print('---------')
    print(board[1] , ' |' , board[2] , '|' , board[3])

# Checks for a winner 
def check_winner(board, player): 
    for combo in winning_combos:
        score = 0
        for index in combo:
            if board[index] == player:
                score += 1
            if score == 3:
                return True
    return False

# Checks for a tie
def full_board(board):
    for k, v in board.items():
        if v == '':
            return False
    return True

# the main function  
def game(turn):
    round = 0
    print_board()

    for i in range(9):

        # Gets player's next move
        print("where would you like to move?")
        number = int(input())
        make_move(board, 'x', number)
        
        
        round += 1

        # Checking for winners before moving onto the next player
        if check_winner(board, turn) == True:
            print("game over. ", turn, "won.")
            break
        # Checking for a tie
        if full_board(board) == True:
            print("no one won, you're both losers.")
            break
        
        # Switches the player to 'o'
        if turn == 'x':
            turn = 'o'

        # Computer move
        move = computer_moves(board)
        make_move(board, turn, move)

        print_board()
        
        round += 1

        # Checking the winner before moving onto the next round
        if check_winner(board, turn) == True:
            print("game over. ", turn, "won.")
            break

        # Switches the player to x
        if turn == 'o':
            turn = 'x'

    print_board()

# Makes a move for the corresponding player
# If the space is unavailible, the turn is skipped.
def make_move(board, player, move):
    if board[move] == '':
        board[move] = player
    else:
        print("not available. your turn was skipped.")

# Finds all possible moves for the computer
def computer_moves(board):
    # check if the computer can win
    for k, v in board.items():
        tmp = board.copy()
        if v == '':
            make_move(tmp, 'o', k)
            if check_winner(tmp, 'o') == True:
                return k
    # check if the player can win and block them
    for k, v in board.items():
        tmp = board.copy()
        if v == '':
            make_move(tmp, 'x', k)
            if check_winner(tmp, 'x') == True:
                return k
    # check for an open middle space
    if board[5] == '':
        return 5
    # if all else fails, choose the first availible space
    for k, v in board.items():
        if v == '':
            return k

# Beginning of the game:
print("Welcome To Tic Tac Toe!")
game(turn)