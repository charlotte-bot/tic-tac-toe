board = {7:'',8:'',9:'', 4:'',5:'',6:'', 1:'',2:'',3:''}

def print_board():
    print(board[7] , ' |' , board[8] , '|' , board[9])
    print('---------')
    print(board[4] , ' |' , board[5] , '|' , board[6])
    print('---------')
    print(board[1] , ' |' , board[2] , '|' , board[3])

def game():
    turn = 'x'

    for i in range(9):
        print_board()

        # human = x
        # robot = o


        print(turn , ",where would you like to move?")
        number = int(input())

        if board[number] == '':
            board[number] = turn
        else:
            print("not available.")
        
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

    print_board()
game()