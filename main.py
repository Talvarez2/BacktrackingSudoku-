from Backtracking import solve_sudoku

def print_sudoku(sudoku):
	for i in sudoku:
		print(i)


if __name__ == "__main__":
	sudoku = [[0 for i in range(9)] for i in range(9)]
	solve_sudoku(sudoku)
	print_sudoku(sudoku)
