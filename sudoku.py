"""Contains the methods to solve a Sudoku board.

Example use case at the bottom.
""" 

def get_empty_space(board):
    """Searches a empty space in the board.

    Args:
        board: Sudoku board.

    Yields:
        int, int: Row and column of the empty space, returns -1, -1 if there are
        no empty spaces.
    """
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
                return i, j
    return -1, -1

def valid_value(board, row, col, value):
    """Checks if number is valid in position.

    Args:
        board: Sudoku board.
        row: Row to check.
        col: Column to check.
        value: Number to check.

    Return:
        bool: Indicates the validity of the number in the position.
    """
    for i in range(9):
        if board[i][col] == value:
            return False
    for j in range(9):
        if board[row][j] == value:
            return False

    square_row = row // 3 * 3
    square_col = col // 3 * 3

    for i in range(3):
        for j in range(3):
            if board[square_row+i][square_col+j] == value:
                return False
    return True


def solve(board):
    """Solves the sudoku using backtracking, it tranverses the search tree
    recursively in depth-first order.

    Args:
        board: Sudoku board.

    Returns:
        bool: Indicates if the board is solved.
    """

    row, col = get_empty_space(board)
    if row == -1:
        return True
    for value in range(1, 10):
        if valid_value(board, row, col, value):
            board[row][col] = value
            if solve(board):
                return True
            board[row][col] = 0
    return False


if __name__ == '__main__':
    example = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    print(solve(example))
    print(example)
