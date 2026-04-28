# 0022 Generate Parentheses

## Problem Idea

Given `n` pairs of parentheses, generate all valid combinations.

Example:

```text
n = 3
```

Valid answers:

```text
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

The important rule is:

- we can use at most `n` left parentheses
- we can use at most `n` right parentheses
- a right parenthesis can only be added if there are more left parentheses already used

## Backtracking Idea

Build the string one character at a time.

At each step, choose:

- add `"("` if we still have left parentheses available
- add `")"` if it will not break the valid order

The recursive function tracks:

```python
backtrack(path, left, right)
```

Meaning:

- `path`: current parentheses string
- `left`: how many `"("` have been used
- `right`: how many `")"` have been used

## My Code Notes

```python
res = []

def backtrack(path, left, right):
    if len(path) == 2 * n:
        res.append(path)
        return

    if left < n:
        backtrack(path + '(', left + 1, right)

    if right < left:
        backtrack(path + ')', left, right + 1)

backtrack("", 0, 0)
return res
```

What this code does:

- Start with an empty string.
- Keep adding valid parentheses choices.
- When the string length reaches `2 * n`, save it into `res`.
- Use `left < n` to make sure we do not use too many left parentheses.
- Use `right < left` to make sure every right parenthesis has a matching left parenthesis before it.

## Why `right < left` Works

A valid parentheses string can never have more `")"` than `"("` at any point.

Example:

```text
())(
```

This becomes invalid as soon as the third character appears:

```text
())
```

There are more right parentheses than left parentheses, so the order is already broken.

That is why we only add `")"` when:

```python
right < left
```

## Recursion Tree Example

For `n = 2`:

```text
""
-> "("
   -> "(("
      -> "(()"
         -> "(())"
   -> "()"
      -> "()("
         -> "()()"
```

Answer:

```text
["(())", "()()"]
```

## Complexity

- Time: `O(4^n / sqrt(n))`
- Space: `O(n)`

Why:

- The number of valid parentheses combinations is the Catalan number.
- Each recursive path has length `2 * n`.
- The recursion depth is at most `2 * n`, so the call stack is `O(n)`.

## Key Learning

- Backtracking is useful when we need to generate all valid combinations.
- We can avoid invalid paths early by checking `left < n` and `right < left`.
- `path + '('` creates a new string for the next recursive call, so each path stays independent.
