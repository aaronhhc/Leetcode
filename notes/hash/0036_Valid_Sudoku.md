# 0036 Valid Sudoku

## Problem Idea

We need to check whether a partially filled Sudoku board is valid.

The board is valid if every filled number follows these rules:

- No duplicate number in the same row.
- No duplicate number in the same column.
- No duplicate number in the same 3x3 box.

Important detail:

- Empty cells are represented by `"."`.
- Empty cells do not matter, so we skip them.
- We do not need to solve the Sudoku. We only check whether the current board is valid.

---

## My Code Notes

The main idea is to use hash sets to remember which numbers we have already seen.

Your solution keeps three groups:

- `rows`: remembers numbers already seen in each row.
- `cols`: remembers numbers already seen in each column.
- `box`: remembers numbers already seen in each 3x3 box.

Why sets are useful:

- A set can check whether a number already exists in `O(1)` average time.
- If the number already exists in the row, column, or box, the board is invalid immediately.

---

## Key Check

For each non-empty cell, we check three things:

- Has this value already appeared in this row?
- Has this value already appeared in this column?
- Has this value already appeared in this 3x3 box?

If any answer is yes, return `False`.

If all checks pass, add the value into the row set, column set, and box set.

At the end, if no duplicates were found, return `True`.

---

## Box Index

The key trick in this problem is how to identify each 3x3 box.

Your solution uses:

- row group: `r // 3`
- column group: `c // 3`

So each box can be represented by a pair:

- top-left box: `(0, 0)`
- top-middle box: `(0, 1)`
- top-right box: `(0, 2)`
- middle-left box: `(1, 0)`
- bottom-right box: `(2, 2)`

Example:

- Cell `(0, 0)` belongs to box `(0, 0)`
- Cell `(1, 2)` belongs to box `(0, 0)`
- Cell `(4, 5)` belongs to box `(1, 1)`
- Cell `(8, 8)` belongs to box `(2, 2)`

This makes it easy to store and check values for each box.

---

## Complexity

The board size is always 9x9, so technically the time and space are constant.

But if we describe it generally:

- Time: `O(81)`, which is `O(1)` for a fixed Sudoku board
- Space: `O(81)`, which is also `O(1)`

Why:

- We visit each cell once.
- We store each filled value at most once in a row set, column set, and box set.

---

## Key Learning

- Use hash sets when you need fast duplicate checking.
- For Sudoku, check row, column, and 3x3 box at the same time.
- The 3x3 box index can be found with integer division: `r // 3` and `c // 3`.
- Skip `"."` because empty cells do not affect validity.
- `defaultdict(set)` is a good fit here because each row, column, or box automatically starts with an empty set.
