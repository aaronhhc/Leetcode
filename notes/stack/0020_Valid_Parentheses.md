# 0020 Valid Parentheses

## Problem Idea

We need to check whether every closing bracket matches the most recent unmatched opening bracket.

Valid examples:

- `"()"` -> `True`
- `"()[]{}"` -> `True`
- `"{[]}"` -> `True`

Invalid examples:

- `"(]"` -> `False`
- `"([)]"` -> `False`
- `"("` -> `False`

The important rule is order. A closing bracket must close the latest opening bracket first.

## My Code Notes

### Stack solution

```python
pairs = {')': '(', ']': '[', '}': '{'}
stack = []

for bracket in s:
    if bracket in pairs:
        if not stack or stack.pop() != pairs[bracket]:
            return False
    else:
        stack.append(bracket)

return not stack
```

What this code does:

- Use `pairs` to map every closing bracket to its matching opening bracket.
- Push opening brackets into `stack`.
- When a closing bracket appears, check the top of the stack.
- If the stack is empty or the top does not match, return `False`.
- At the end, return `True` only if there are no unmatched opening brackets left.

## Why Stack Works

Parentheses follow last-in, first-out order.

Example:

```text
{ [ ] }
```

The `[` opens after `{`, so `]` must close before `}`.

That is exactly how a stack works:

- newest opening bracket is checked first
- older opening brackets wait below it

## Key Python Concepts

### Dictionary lookup

```python
pairs = {')': '(', ']': '[', '}': '{'}
```

This lets us quickly find the expected opening bracket for each closing bracket.

### `not stack`

```python
if not stack:
```

An empty list is considered `False` in Python, so `not stack` means the stack has no elements.

### `stack.pop()`

```python
stack.pop()
```

Removes and returns the last element from the list. This is how we check the latest unmatched opening bracket.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

Why:

- Each bracket is visited once.
- In the worst case, all brackets are opening brackets, so the stack can store `n` characters.

## Key Learning

- Stack is the natural tool when the latest opened item must be closed first.
- A dictionary makes the code shorter than writing separate checks for `)`, `]`, and `}`.
- `return not stack` is a clean Pythonic way to make sure nothing is left unmatched.
