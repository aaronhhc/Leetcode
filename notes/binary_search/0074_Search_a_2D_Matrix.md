# 0074 Search a 2D Matrix

## Problem Idea

We are given:

- a matrix where each row is sorted
- the first number of each row is greater than the last number of the previous row
- a target value `target`

We need to return `True` if `target` exists in the matrix.

If it does not exist, return `False`.

Example:

```text
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 3
answer = True
```

The value `3` exists in the first row.

Because the whole matrix is sorted like one long sorted array, we can use binary search.

---

## My First Idea

My first solution does two steps:

- decide which row could contain `target`
- run binary search inside that row

For each row, check whether `target` is between the first and last value of that row.

If yes, binary search that row.

---

## My Code Notes

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row: List[int], target) -> bool:
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = (low + high) // 2

                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            if c == 1:
                if target == matrix[i][0]:
                    return True

            if target > matrix[i][0] and target < matrix[i][c - 1]:
                return search(matrix[i], target)
            elif target == matrix[i][0] or target == matrix[i][c - 1]:
                return True

        return False
```

What this code does:

- Use a helper function to binary search one row.
- Loop through every row.
- If `target` equals the first or last value of a row, return `True`.
- If `target` is between the first and last value of a row, search inside that row.
- If no row contains the target, return `False`.

---

## Standard Binary Search Idea

The cleaner solution treats the matrix as one sorted 1D array.

If the matrix has:

- `rows` rows
- `cols` columns

Then there are `rows * cols` total values.

We can binary search from:

```python
left = 0
right = rows * cols - 1
```

The important part is converting a 1D index into a matrix position.

```python
row = mid // cols
col = mid % cols
```

Why this works:

- `mid // cols` tells us which row the index belongs to
- `mid % cols` tells us which column inside that row

---

## Standard Code Notes

```python
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2

        row = mid // cols
        col = mid % cols

        val = matrix[row][col]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

What this code does:

- Search the matrix as if it were one sorted array.
- Convert `mid` into `row` and `col`.
- Compare `matrix[row][col]` with `target`.
- If the value is too small, search the right half.
- If the value is too large, search the left half.
- If the loop ends, the target does not exist.

---

## Index Conversion

Example:

```text
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
```

This can be imagined as:

```text
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
```

If:

```text
cols = 4
mid = 6
```

Then:

```text
row = 6 // 4 = 1
col = 6 % 4 = 2
```

So index `6` points to:

```python
matrix[1][2] = 16
```

---

## Walkthrough

Example:

```text
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 3
```

Start:

```text
left = 0
right = 11
```

First middle:

```text
mid = 5
row = 5 // 4 = 1
col = 5 % 4 = 1
matrix[1][1] = 11
```

`11` is larger than `3`, so search the left half:

```text
left = 0
right = 4
```

Second middle:

```text
mid = 2
row = 2 // 4 = 0
col = 2 % 4 = 2
matrix[0][2] = 5
```

`5` is larger than `3`, so search the left half:

```text
left = 0
right = 1
```

Third middle:

```text
mid = 0
row = 0 // 4 = 0
col = 0 % 4 = 0
matrix[0][0] = 1
```

`1` is smaller than `3`, so search the right half:

```text
left = 1
right = 1
```

Fourth middle:

```text
mid = 1
row = 1 // 4 = 0
col = 1 % 4 = 1
matrix[0][1] = 3
```

Found the target, so return `True`.

---

## Edge Cases

### Target is the first value

```text
matrix = [[1, 3, 5]]
target = 1
answer = True
```

### Target is the last value

```text
matrix = [[1, 3, 5]]
target = 5
answer = True
```

### Target does not exist

```text
matrix = [[1, 3, 5]]
target = 2
answer = False
```

### Matrix has one column

```text
matrix = [[1], [3], [5]]
target = 3
answer = True
```

---

## Complexity

For the standard 1D binary search solution:

- Time: `O(log(m * n))`
- Space: `O(1)`

Why:

- There are `m * n` total values.
- Binary search removes half of the remaining values each time.
- Only a few variables are used.

For my first row-checking solution:

- Time: `O(m + log n)` in the worst case
- Space: `O(1)`

Why:

- It may scan through rows to find the possible row.
- Then it binary searches inside one row.

---

## Key Learning

- A sorted 2D matrix can be treated like one sorted 1D array.
- Convert 1D index to 2D position with `row = mid // cols` and `col = mid % cols`.
- Standard binary search is cleaner because it searches all values directly.
- `left` and `right` should cover indexes from `0` to `rows * cols - 1`.
