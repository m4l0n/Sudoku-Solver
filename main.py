def fill_values(board):
    if (check_complete(board) and check_duplicates(board)):
        for i in board:
            print(i)
        return True

    i, j = find_first_empty(board)
    for k in range(1, 10):
        board[i][j] = k
        if (check_duplicates(board)):
            if (fill_values(board)):
                return True
        board[i][j] = -1
    return False


def find_first_empty(board):
    for i in range(9):
        for j in range(9):
            if (board[i][j] == -1):
                return i, j


def check_complete(board):
    for i in board:
        for j in i:
            if (j == -1):
                return False

    return True


def check_duplicates(board):
    # Check row
    for i in board:
        h_check = {}
        for j in i:
            if (j != -1 and j not in h_check):
                h_check[j] = "1"
            elif (j == -1):
                continue
            else:
                return False
    # Check column
    for i in range(9):
        v_check = {}
        for j in board:
            if j[i] not in v_check and j[i] != -1:
                v_check[j[i]] = "1"
            elif (j[i] == -1):
                continue
            else:
                return False
    # Check grid
    flag = 0
    flag2 = 0
    for i in range(9):
        grid_check = {}
        if (i in [0, 3, 6]):
            flag = 0
        elif (i in [1, 4, 7]):
            flag = 3
        elif (i in [2, 5, 8]):
            flag = 6
        if (i in [0, 1, 2]):
            flag2 = 0
        elif (i in [3, 4, 5]):
            flag2 = 3
        elif (i in [6, 7, 8]):
            flag2 = 6
        for row in range(3):
            for column in range(3):
                if board[row+flag2][column+flag] not in grid_check and board[row+flag2][column+flag] != -1:
                    grid_check[board[row+flag2][column+flag]] = "1"
                elif (board[row+flag2][column+flag] == -1):
                    continue
                else:
                    return False
    return True


if __name__ == "__main__":
    input_board = [[-1, -1, 1, -1, 2, -1, -1, 5, 7],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 9],
                   [-1, 4, -1, 1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, 6, -1, 4, -1, -1],
                   [-1, 3, -1, -1, -1, 7, -1, 6, 5],
                   [-1, -1, 5, -1, -1, -1, 9, -1, -1],
                   [-1, -1, -1, -1, -1, -1, 6, -1, -1],
                   [8, -1, -1, -1, -1, 3, -1, -1, -1],
                   [-1, -1, 4, -1, 7, -1, -1, 2, 1]]
    # Check if the board is a proper sudoku board
    assert len(input_board) == 9, 'The board is not a proper sudoku board!'
    for i in input_board:
        assert len(i) == 9, 'The board is not a proper sudoku board!'
    if (fill_values(input_board)):
        print("Sudoku Completed!")