def sloveSudoku(board):
    # The function modifies the board in place to present the solution .Hence there is np need to return board
    def isValid():
        for x in range(9):
            if board[x][col] == num:
                return False
            if board[row][x]==num:
                return False
            r = 3*(row//3) + x//3
            c = 3*(col//3) + x%3
            if board[r][c]==num:
             return False
        return True

    def fillTheBoard(board):
        # the next element cell
        for row in range(9):
            for col in range(9):
                if board[row][col] =='.':
                    for num in '123456789':
                        if isValid(num,row,col):
                            board[row][col] = num
                            if(fillTheBoard(board)): return True
                            board[row][col] = '.' #backtracking step
                    return False

        return True


    fillTheBoard(board)