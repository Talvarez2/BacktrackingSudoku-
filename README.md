# Backtracking Sudoku Solver

A Python Sudoku solver that uses a recursive backtracking algorithm to fill in a 9x9 grid.

## How It Works

1. Find the first empty cell (value `0`)
2. Try digits 1-9, checking row, column, and 3x3 box constraints
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

This solves the built-in example puzzle and prints the result.

## Requirements

- Python 3.7+
