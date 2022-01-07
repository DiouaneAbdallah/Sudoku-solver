# solver.py

def print_board(board):
    """
    prints a sudoku board
    :param board: 2d list of ints
    :return: None
    """
    print("  _ _ _   _ _ _   _ _ _")
    j = 0
    for row in board:
        print("| ", end="")
        j += 1
        i = 0
        for elem in row:
            i += 1
            print(elem, end=" ")
            if (i%3 == 0):
                print("| ", end="")
        if (j%3 == 0):
                print("\n  - - -   - - -   - - -", end="")
        print("\n", end="")

def find_empty(board):
    """
    finds an empty space in the sudoko board
    :param board: 2d list of ints
    :return: (int, int) row col
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def isSafe(board, row, col, num):
    """
    Check if we find num in 
    the same row ,col or box 
    :param board: 2d list of ints
    :param board: row
    :param board: col
    :param board: num
    :return: boolean
    """
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def solve(board):
    """
    Solves a sudoku board using backtracking
    :param board: 2d list of ints
    :return: solution
    """
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if isSafe(board, row, col, i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False