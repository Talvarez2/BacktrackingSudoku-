"""Backtracking Sudoku Solver.

Solves a 9x9 Sudoku puzzle using a recursive backtracking algorithm.
Each empty cell (value ``0``) is filled by trying digits 1-9 while
respecting row, column, and 3x3 box constraints.
"""

from __future__ import annotations

from typing import List

EMPTY: int = 0
SIZE: int = 9
BOX: int = 3

Board = List[List[int]]

EXAMPLE_BOARD: Board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def validate_board(board: Board) -> None:
    """Raise ``ValueError`` if *board* is not a valid 9x9 Sudoku grid.

    Checks dimensions and that every cell value is an integer in 0-9.
    """
    if len(board) != SIZE:
        raise ValueError(f"Board must have {SIZE} rows, got {len(board)}")
    for i, row in enumerate(board):
        if len(row) != SIZE:
            raise ValueError(
                f"Row {i} must have {SIZE} columns, got {len(row)}"
            )
        for j, val in enumerate(row):
            if not isinstance(val, int) or not (0 <= val <= SIZE):
                raise ValueError(
                    f"Invalid value {val!r} at ({i}, {j}); "
                    f"expected int 0–{SIZE}"
                )


def print_board(board: Board) -> None:
    """Print the board in a human-readable grid format."""
    for i, row in enumerate(board):
        if i % BOX == 0 and i != 0:
            print("-" * 21)
        line = ""
        for j, val in enumerate(row):
            if j % BOX == 0 and j != 0:
                line += "| "
            line += f"{val if val != EMPTY else '.'} "
        print(line.rstrip())


def find_empty(board: Board) -> tuple[int, int] | None:
    """Return the ``(row, col)`` of the first empty cell, or ``None``."""
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == EMPTY:
                return (r, c)
    return None


def is_valid(board: Board, row: int, col: int, num: int) -> bool:
    """Check whether placing *num* at (*row*, *col*) is valid."""
    if num in board[row]:
        return False
    if any(board[r][col] == num for r in range(SIZE)):
        return False
    box_r, box_c = BOX * (row // BOX), BOX * (col // BOX)
    for r in range(box_r, box_r + BOX):
        for c in range(box_c, box_c + BOX):
            if board[r][c] == num:
                return False
    return True


def solve(board: Board) -> bool:
    """Solve the board in-place using backtracking. Return ``True`` if solved."""
    cell = find_empty(board)
    if cell is None:
        return True
    row, col = cell
    for num in range(1, SIZE + 1):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = EMPTY
    return False


def main() -> None:
    """Run the solver on the example board."""
    board: Board = [row[:] for row in EXAMPLE_BOARD]
    validate_board(board)
    print("Puzzle:")
    print_board(board)
    print()
    if solve(board):
        print("Solution:")
        print_board(board)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
