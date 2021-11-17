"""Contains the SudokuUI class and starts the execution of the GUI.
"""
import tkinter as tk
import sudoku

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


class SudokuUI(tk.Frame):
    """GUI class of the game. Inherits from tkinter.Frame.
    """

    def __init__(self, parent, game):
        self.parent = parent
        self.game = game
        tk.Frame.__init__(self, parent)
        self.row, self.col = 0, 0
        self.__init_ui()
        self.visualizing = False

    def __init_ui(self):
        """Initializes the UI.
        """
        self.parent.title("Sudoku")
        self.pack(fill=tk.BOTH)
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)
        frame = tk.Frame(self.parent)
        frame.pack(fill=tk.Y, side=tk.TOP)
        btn_clear = tk.Button(frame, text="Clear",
                              command=self.__clear_answers)
        btn_clear.pack(side=tk.LEFT)
        btn_solve = tk.Button(frame, text="Solve",
                              command=self.__solve)
        btn_solve.pack(side=tk.LEFT)
        btn_visualize = tk.Button(frame, text="Visualize",
                                  command=self.__visualize)
        btn_visualize.pack(side=tk.LEFT)
        btn_new = tk.Button(frame, text="New",
                            command=self.__new_board)
        btn_new.pack(side=tk.LEFT)

        self.__draw_grid()
        self.__draw_board()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        """Draws the lines that form the grid of the sudoku.
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x_start = MARGIN + i * SIDE
            y_start = MARGIN
            x_end = MARGIN + i * SIDE
            y_end = HEIGHT - MARGIN
            self.canvas.create_line(x_start, y_start, x_end, y_end, fill=color)

            x_start = MARGIN
            y_start = MARGIN + i * SIDE
            x_end = WIDTH - MARGIN
            y_end = MARGIN + i * SIDE
            self.canvas.create_line(x_start, y_start, x_end, y_end, fill=color)

    def __draw_board(self):
        """Inserts the numbers of the sudoku board into the grid.
        """
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.board[i][j]
                if answer != 0:
                    x_coord = MARGIN + j * SIDE + SIDE / 2
                    y_coord = MARGIN + i * SIDE + SIDE / 2
                    original = self.game.start_board[i][j]
                    if answer == original:
                        color = "black"
                        font = ("Purisa", 30, "bold")
                    else:
                        color = "sea green"
                        font = ("Purisa", 25)
                    self.canvas.create_text(
                        x_coord, y_coord, text=answer, tags="numbers",
                        fill=color, font=font)

    def __clear_answers(self):
        """Removes all the input from the user.
        """
        if not self.visualizing:
            self.game.reset_board()
            self.canvas.delete("victory")
            self.__draw_board()

    def __solve(self):
        """Solves the sudoku board and displays it.
        """
        if not self.visualizing:
            self.game.reset_board()
            self.game.solve()
            self.canvas.delete("victory")
            self.__draw_board()

    def __new_board(self):
        """Generates a new board and displays it.
        """
        if not self.visualizing:
            self.game.generate_board()
            self.canvas.delete("victory")
            self.__draw_board()

    def __visualize(self):
        """Visualizes the solving of the sudoku board.
        """
        if not self.visualizing:
            self.visualizing = True
            self.game.reset_board()
            self.canvas.delete("victory")
            self.game.solve(self)
            self.visualizing = False
            self.canvas.delete("victory")

    def show_change(self):
        """Helper method to be called by the Sudoku class each time it inserts
        a number with solving to be visualized
        """
        if self.visualizing:
            self.__draw_board()
            super().update()

    def __cell_clicked(self, event):
        """Updates the cell that is clicked by the user.
        """
        if self.game.game_over:
            return
        x_coord, y_coord = event.x, event.y
        if (MARGIN < x_coord < WIDTH - MARGIN and
                MARGIN < y_coord < HEIGHT - MARGIN):
            self.canvas.focus_set()

            row, col = (y_coord - MARGIN) // SIDE, (x_coord - MARGIN) // SIDE

            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif (self.game.board[row][col] == 0 or
                  self.game.board[row][col] != self.game.start_board[row][col]):
                self.row, self.col = row, col

        self.__draw_cursor()

    def __draw_cursor(self):
        """Draws a rectangle around the cell selected by the user.
        """
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x_start = MARGIN + self.col * SIDE + 1
            y_start = MARGIN + self.row * SIDE + 1
            x_end = MARGIN + (self.col + 1) * SIDE - 1
            y_end = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x_start, y_start, x_end, y_end,
                outline="red", tags="cursor"
            )

    def __key_pressed(self, event):
        """Inserts the number pressed by the user to the selected cell.
        """
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.board[self.row][self.col] = int(event.char)
            self.col, self.row = -1, -1
            self.__draw_board()
            self.__draw_cursor()
            if self.game.check_win():
                self.__draw_victory()

    def __draw_victory(self):
        """Draws a circle to signal that the board is solved.
        """
        x_0 = y_0 = MARGIN + SIDE * 2
        x_1 = y_1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x_0, y_0, x_1, y_1,
            tags="victory", fill="dark orange", outline="orange"
        )
        x_coord = y_coord = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x_coord, y_coord,
            text="WIN", tags="victory",
            fill="white", font=("Arial", 32)
        )


if __name__ == '__main__':
    board = sudoku.Sudoku()
    root = tk.Tk()
    SudokuUI(root, board)
    root.geometry(f"{WIDTH}x{HEIGHT + 40}")
    root.mainloop()
