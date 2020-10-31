board = {7:'',8:'',9:'', 4:'',5:'',6:'', 1:'',2:'',3:''}

winning_combos = [[7,8,9], [4,5,6], [1,2,3], [1,4,7], [2,5,8], [3,6,9], [3,5,7], [1,5,9]]

turn = 'x'

def print_board():
    print(board[7] , ' |' , board[8] , '|' , board[9])
    print('---------')
    print(board[4] , ' |' , board[5] , '|' , board[6])
    print('---------')
    print(board[1] , ' |' , board[2] , '|' , board[3])

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
   
def game(turn):
    round = 0
    print_board()

    for i in range(9):


        print("where would you like to move?")
        number = int(input())

        if board[number] == '':
            board[number] = turn
        else:
            print("not available, x. your turn was skipped.")
        
        round += 1

        if check_winner(round, turn) == True:
            break
        
        if switch_player(turn) == 'o':
            turn = 'o'
        else:
            turn = 'x'

        print_board()

        moves = possible_moves(board)

        round += 1

        if check_winner(round, turn) == True:
            break

        if switch_player(turn) == 'x':
            turn = 'x'
        else:
            turn = 'o'

    print_board()

def switch_player(turn):
    if turn == 'x':
        return 'o'
    elif turn == 'o':
        return 'x'

def possible_moves(board):
    print('making a move...')
    for k, v in board.items():
        if board[k] == '':
            board[k] = 'o'
            print_board()
            break
    return k, v

# Beginning of the game:
print("Welcome To Tic Tac Toe!")
game(turn)