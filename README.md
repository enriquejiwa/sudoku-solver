<p align="center">
  <img src="https://github.com/enriquejiwa/sudoku-solver/blob/main/assets/icon.png" width="256" height="256">
  <h1 align="center">sudoku-solver</h2>
  <p align="center">
    <a href="https://github.com/enriquejiwa/sudoku-solver/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-informational">
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-v3.9-informational">
    </a>
  </p>
</p>

A [Sudoku](https://en.wikipedia.org/wiki/Sudoku) GUI that generates a sudoku board and lets the user play or visualize how it is solved by backtracking.

<p align="center">
	<img src="https://github.com/enriquejiwa/sudoku-solver/blob/main/assets/screenrecording.gif">
</p>

## Controls

| Buttons           | Actions                               |
|-------------------|---------------------------------------|
| `Clear`           | Removes all the user input.           |
| `Solve`           | Displays the solution.                |
| `Visualize`       | Displays the resolution.              |
| `New`             | Generates another sudoku board.       |

## Requirement

It requires the [tkinter](https://docs.python.org/3/library/tkinter.html) library, use the following command to check if tkinter is properly installed:

```bash
python -m tkinter
```

If not, use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install tk
```

## Usage

-	Clone this repository using
```
git clone https://github.com/enriquejiwa/sudoku-solver.git
```
**OR**
Zip Download the Repository and Extract its contents.
-	Run the [sudoku_gui.py](https://github.com/enriquejiwa/sudoku-solver/blob/main/sudoku_gui.py) file directly in your Terminal using
```
python sudoku_gui.py
```
**OR**
```
python3 sudoku_gui.py
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
