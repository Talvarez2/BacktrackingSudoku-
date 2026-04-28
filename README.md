# Backtracking Sudoku Solver

A Python Sudoku solver that uses a recursive backtracking algorithm to fill in a 9x9 grid.

## How It Works

1. Find the first empty cell (value `0`)
2. Try digits 1–9, checking row, column, and 3×3 box constraints
3. Recurse; if a dead end is reached, backtrack and try the next digit

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Solver logic and entry point |
| `README.md` | Project documentation |
| `AGENTS.md` | AI agent conventions |
| `.gitignore` | Git ignore rules |

## Usage

```bash
python3 main.py
```

### Example Output

```
Puzzle:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
---------------------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
---------------------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

Solution:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

## Requirements

- Python 3.7+
