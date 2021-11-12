"""Contains the methods to generate, solve and diplay (console) a Sudoku board.

Example use case at the bottom.
"""
from random import sample

def generate_board():
    """Generates a solvable sudoku board containing only 17 numbers.

    A sudoku board with 17 numbers has unique solution.

    Returns:
        The generated board.
    """

    # Using random.sample, we generate two lists containing numbers 0-8, where
    # 0-2, 3-5, 6-8 are grouped together.
    rows = [ g*3 + r for g in sample(range(3), 3) for r in sample(range(3), 3) ]
    cols = [ g*3 + c for g in sample(range(3), 3) for c in sample(range(3), 3) ]
    # We generate a list of 1-9 with random sampling.
    values = sample(range(1, 10), 9)
    # We generate a complete board using the numbers of values and the ordering
    # of rows and cols.
    board = [[values[(3*(r%3)+r//3+c)%9] for c in cols] for r in rows]

    # We chose random 81-17=64 positions to erase the value.
    for i in sample(range(81), 64):
        board[i//9][i%9] = 0

    return board

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

def print_board(board):
    """Prints the board to the console with styling.

    Args:
        board: Sudoku board.
    """
    string = ""
    for i in range(9):
        if i == 0:
            string += "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n"
        elif i % 3 == 0:
            string += "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n"
        else:
            string += "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
        string += "║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n".format(*board[i])
    string += "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝\n"
    print(string)

if __name__ == '__main__':
    example = generate_board()
    print_board(example)
    solve(example)
    print_board(example)
