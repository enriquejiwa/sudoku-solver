"""Contains the Sudoku class.

Example use case at the bottom.
"""
from random import sample
from copy import deepcopy
import time


class Sudoku():
    """Class containing the sudoku board and the methods to generate and solve.
    """

    def __init__(self):
        self.board = None
        self.start_board = None
        self.generate_board()
        self.game_over = False

    def generate_board(self):
        """Generates a solvable sudoku board containing only 17 numbers.

        A sudoku board with 17 numbers has unique solution.

        Returns:
            The generated board.
        """
        # Using random.sample, we generate two lists containing numbers 0-8, where
        # 0-2, 3-5, 6-8 are grouped together.
        rows = [g*3 + r for g in sample(range(3), 3)
                for r in sample(range(3), 3)]
        cols = [g*3 + c for g in sample(range(3), 3)
                for c in sample(range(3), 3)]
        # We generate a list of 1-9 with random sampling.
        values = sample(range(1, 10), 9)
        # We generate a complete board using the numbers of values and the ordering
        # of rows and cols.
        board = [[values[(3*(r % 3)+r//3+c) % 9] for c in cols] for r in rows]

        # We chose random 81-17=64 positions to erase the value.
        for i in sample(range(81), 64):
            board[i//9][i % 9] = 0

        self.game_over = False
        self.start_board = board
        self.board = deepcopy(board)

    def reset_board(self):
        """Resets the board to be equal to start_board
        """
        self.game_over = False
        self.board = deepcopy(self.start_board)

    def __get_empty_space(self) -> tuple[int, int]:
        """Searches a empty space in the board.

        Returns:
            int, int: Row and column of the empty space, returns -1, -1 if there are
            no empty spaces.
        """
        for i in range(9):
            for j in range(9):
                if not self.board[i][j]:
                    return i, j
        return -1, -1

    def __valid_value(self, row: int, col: int, value: int) -> bool:
        """Checks if number is valid in position.

        Args:
            row (int): Row to check.
            col (int): Column to check.
            value (int): Number to check.

        Returns:
            bool: Indicates the validity of the number in the position.
        """
        for i in range(9):
            if self.board[i][col] == value:
                return False
        for j in range(9):
            if self.board[row][j] == value:
                return False

        square_row = row // 3 * 3
        square_col = col // 3 * 3

        for i in range(3):
            for j in range(3):
                if self.board[square_row+i][square_col+j] == value:
                    return False
        return True

    def solve(self, gui=None):
        """Solves the sudoku using backtracking, it tranverses the search tree
        recursively in depth-first order.

        Returns:
            bool: Indicates if the board is solved.
        """
        row, col = self.__get_empty_space()
        if row == -1:
            return True
        for value in range(1, 10):
            if self.__valid_value(row, col, value):
                self.board[row][col] = value
                if gui:
                    gui.show_change()
                    time.sleep(0.01)
                if self.solve(gui):
                    return True
                self.board[row][col] = 0
        self.game_over = True
        return False

    def check_win(self) -> bool:
        """Checks if the board is solved.

        Returns:
            bool: If the board is solved.
        """
        for row in range(9):
            if not self.__check_row(row):
                return False
        for column in range(9):
            if not self.__check_column(column):
                return False
        for row in range(3):
            for column in range(3):
                if not self.__check_square(row, column):
                    return False
        self.game_over = True
        return True

    def __check_block(self, block: list):
        return set(block) == set(range(1, 10))

    def __check_row(self, row: int):
        return self.__check_block(self.board[row])

    def __check_column(self, column: int):
        return self.__check_block(
            [self.board[row][column] for row in range(9)]
        )

    def __check_square(self, row: int, column: int):
        return self.__check_block(
            [
                self.board[r][c]
                for r in range(row * 3, (row + 1) * 3)
                for c in range(column * 3, (column + 1) * 3)
            ]
        )

    def __str__(self):
        """Prints the board to the console with styling.
        """
        string = ""
        for i in range(9):
            if i == 0:
                string += "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n"
            elif i % 3 == 0:
                string += "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n"
            else:
                string += "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
            string += "║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║\n".format(
                *self.board[i])
        string += "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝\n"
        return string


if __name__ == '__main__':
    example = Sudoku()
    print(example)
    example.solve()
    print(example)
    print(example.check_win())
