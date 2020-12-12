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

# Checks for a winner or a tie
def check_winner(round, player):
    if round > 4: 
        for combo in winning_combos:
            score = 0
            for index in combo:
                if board[index] == player:
                    score += 1
                if score == 3:
                    print("game over. ", player, "won.")
                    return True
        if round == 9:
            print("no one won, you're both losers.")
            return True
    return False

# the main function  
def game(turn):
    round = 0
    print_board()

    for i in range(9):

        # Gets player's next move
        print("where would you like to move?")
        number = int(input())

        # if the player chose an occupied space their turn is
        # skipped, otherwise their turn is added to the board
        if board[number] == '':
            board[number] = turn
        else:
            print("not available, x. your turn was skipped.")
        
        round += 1

        # Checking for winners before moving onto the next player
        if check_winner(round, turn) == True:
            break
        
        # Switches the player to 'o'
        if turn == 'o':
            turn = 'x'
        else:
            turn = 'o'

        print_board()

        # Computer move
        print('making a move...')
        moves = possible_moves(board)

        round += 1

        # Checking the winner before moving onto the next round
        if check_winner(round, turn) == True:
            break

        # Switches the player to x
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

    print_board()

# Finds all possible moves for the computer
def possible_moves(board):
    all_moves = []

    for k, v in board.items():
        if v == '':
            tmp = board.copy()
            tmp[k] = 'o'
            all_moves.append(tmp)
    return all_moves

# Beginning of the game:
print("Welcome To Tic Tac Toe!")
game(turn)