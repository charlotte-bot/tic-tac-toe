board = {7:'',8:'',9:'', 4:'',5:'',6:'', 1:'',2:'',3:''}

def print_board():
    print(board[7] , ' |' , board[8] , '|' , board[9])
    print('---------')
    print(board[4] , ' |' , board[5] , '|' , board[6])
    print('---------')
    print(board[1] , ' |' , board[2] , '|' , board[3])

def winner(round):
    if board[7] == board[8] == board[9] != '': #top row
        if board[7] =='x':
            print("game over. x won")
            return True
        else:
            print("game over. o won")
            return True
    
    elif board[6] == board[5] == board[4] != '': #middle row
        if board[6] =='x':
            print("game over. x won")
            return True
        else:
            print("game over. o won")
            return True

    elif board[3] == board[2] == board[1] != '': #bottom row
        if board[3] =='x':
            print("game over. x won")
            return True
        else:
            print("game over. o won")
            return True

    elif board[7] == board[4] == board[1] != '': #left column
        if board[7] =='x':
            print("game over. x won")
            return True
        else:
            print("game over. o won")
            return True

    elif board[8] == board[5] == board[2] != '': #middle column
        if board[8] =='x':
            print("game over. x won")
            return True
        else:
            print("game over. o won")
            return True
    
    elif board[9] == board[6] == board[3] != '': #right column
        if board[9] =='x':
            print("game over. x won")
            return True
        else:
            print("game over. o won")
            return True

    elif board[7] == board[5] == board[3] != '': #top left to bottom right
        if board[7] =='x':
            print("game over. x won")
            return True
        else:
            print("game over. o won")
            return True

    elif board[9] == board[5] == board[1] != '': #top right to bottom left
        if board[9] =='x':
            print("game over. x won")
            return True
        else:
            print("game over. o won")
            return True

    elif round == 9:
        print("no one won, you're both losers.")
        return False

def game():
    turn = 'x'
    round = 0

    for i in range(9):
        print_board()

        # human = x
        # robot = o

        print(turn , ", where would you like to move?")
        number = int(input())

        if board[number] == '':
            board[number] = turn
        else:
            print("not available,", turn, ". you're turned was skipped.")
        
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

        round += 1

        if winner(round) == True:
            break
        else:
            continue

        break

    print_board()

game()