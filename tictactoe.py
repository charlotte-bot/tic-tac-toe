board = [{7:'',8:'',9:''}, {4:'',5:'',6:''}, {1:'',2:'',3:''}]

def print_board():
    print(board[0][7] , ' |' , board[0][8] , ' |' , board[0][9])
    print('--+---+--')
    print(board[1][4] , ' |' , board[1][5] , ' |' , board[1][6])
    print('--+---+--')
    print(board[2][1] , ' |' , board[2][2] , ' |' , board[2][3])

def game():
    print_board()

    # human = x
    # robot = o

game()