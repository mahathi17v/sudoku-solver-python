# Sudoku Solver using Python

A beginner-friendly Sudoku Solver built in Python using the Backtracking Algorithm.

## Features

- Solves any valid 9×9 Sudoku puzzle
- Accepts user input from the terminal
- Uses recursion and backtracking
- Displays the completed Sudoku grid
- Handles unsolvable puzzles

## Technologies Used

- Python 3

## Algorithm

This project uses the Backtracking Algorithm:

1. Find an empty cell.
2. Try numbers from 1 to 9.
3. Check if the number is valid.
4. Recursively solve the remaining grid.
5. Backtrack if no valid number can be placed.

## Project Structure

```text
Sudoku-Solver/
│
├── sudoku_solver.py
└── README.md
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/sudoku-solver-python.git
```

Navigate to the project directory:

```bash
cd sudoku-solver-python
```

Run the program:

```bash
python sudoku_solver.py
```

## Example Input

```text
9 0 6 0 7 0 4 0 3
0 0 0 4 0 0 2 0 0
0 7 0 0 2 3 0 1 0
5 0 0 0 0 0 1 0 0
0 4 0 2 0 8 0 6 0
0 0 3 0 0 0 0 0 5
0 3 0 7 0 0 0 5 0
0 0 7 0 0 5 0 0 0
4 0 5 0 1 0 7 0 8
```

## Example Output

```text
9 2 6 5 7 1 4 8 3
3 5 1 4 8 6 2 7 9
8 7 4 9 2 3 5 1 6
5 8 2 3 6 7 1 9 4
1 4 9 2 5 8 3 6 7
7 6 3 1 9 4 8 2 5
2 3 8 7 4 9 6 5 1
6 1 7 8 3 5 9 4 2
4 9 5 6 1 2 7 3 8
```

## Concepts Practiced

- Functions
- Lists
- Nested Loops
- Recursion
- Backtracking
- Problem Solving

## Future Improvements

- GUI using Tkinter
- Random Sudoku Generator
- Difficulty Levels
- Sudoku Validation
- Web Version using JavaScript