# 0150 Evaluate Reverse Polish Notation

## Problem Idea

Reverse Polish Notation means the operator comes after the numbers.

Example:

```text
["2", "1", "+", "3", "*"]
```

This means:

```text
(2 + 1) * 3 = 9
```

## Stack Idea

Use a stack to store numbers.

For each token:

- if it is a number, push it into the stack
- if it is an operator, pop two numbers, calculate, and push the result back

At the end, the stack has one number left. That number is the answer.

## Important Detail

When popping two numbers:

```python
right = stack.pop()
left = stack.pop()
```

Order matters for subtraction and division.

Example:

```text
["4", "2", "-"]
```

This means:

```text
4 - 2
```

So the first popped number is the right side, and the second popped number is the left side.

## Python Division Note

LeetCode wants division to truncate toward zero.

So use:

```python
int(left / right)
```

Example:

```python
int(6 / -4)  # -1
```

Do not use `//` here, because Python floor division rounds down.

Example:

```python
6 // -4  # -2
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`

Why:

- We scan every token once.
- The stack can store up to `n` numbers.
