# Backtracking Sudoku Solver

A Python Sudoku solver that uses a recursive backtracking algorithm to fill in a 9×9 grid.

## How It Works

1. Find the first empty cell (value `0`)
2. Try digits 1–9, checking row, column, and 3×3 box constraints
3. Recurse; if a dead end is reached, backtrack and try the next digit

## Usage

```bash
python main.py
```

This solves the built-in example puzzle and prints the result.

## Requirements

- Python 3.10+
