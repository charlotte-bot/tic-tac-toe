Tic Tac Toe:
    Implement AI:
        Go through every game state possible and select the best
        Recursive algorithm

        function when given a board and player:
            gives a list of boards. each board containts every possible moves the player can make.
            every time human makes move (before computer move):
                look at board and make random move
                recursively call same function and make move for human
                repeat
                (build tree of all possible moves)
