# AGENTS.md

## Project Overview

Backtracking Sudoku Solver — a single-file Python program that solves 9x9 Sudoku puzzles using recursive backtracking.

## How to Run

```bash
python3 main.py
```

## Testing

No test framework yet. Verify manually:

```bash
python3 main.py          # should print puzzle then solution
python3 -c "import main" # should import without side effects
```

## Key Files

| File | Purpose |
|------|---------|
| `main.py` | Solver logic and entry point |
| `README.md` | Project documentation |
| `AGENTS.md` | AI agent conventions |
| `.gitignore` | Git ignore rules |

## Coding Conventions

- **Language**: Python 3.7+
- **Type hints**: Use on all function signatures
- **Type aliases**: `Board = List[List[int]]` — use `Board` instead of raw nested lists
- **Docstrings**: Required for every function and module
- **Constants**: UPPER_SNAKE_CASE at module level
- **Functions**: snake_case
- **Error output**: Print errors to `sys.stderr`; use `sys.exit(1)` for failures
- **Style**: Follow PEP 8
- **Entry point**: Guard with `if __name__ == "__main__"`
