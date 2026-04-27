# 0155 Min Stack

## Problem Idea

We need to design a stack that supports four operations:

- `push(val)`: add a value to the stack
- `pop()`: remove the top value
- `top()`: return the top value
- `getMin()`: return the minimum value in the stack

The special requirement is that every operation should be `O(1)`.

If we only use one normal stack, `getMin()` would need to scan the whole stack, which is `O(n)`.

So we use two stacks:

- `stack`: stores all values
- `min_stack`: stores the current minimum values

## My Code Notes

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

## How The Two Stacks Work

### `stack`

This is the normal stack.

Every value gets pushed into `self.stack`.

Example:

```python
self.stack = [3, 5, 2, 2, 4]
```

The top value is the last value:

```python
self.stack[-1]  # 4
```

### `min_stack`

This stack only stores values that become the current minimum.

When pushing a value:

```python
if not self.min_stack or val <= self.min_stack[-1]:
    self.min_stack.append(val)
```

Meaning:

- if `min_stack` is empty, push the value
- if `val` is smaller than or equal to the current minimum, push it into `min_stack`

We use `<=` instead of `<` because duplicate minimum values matter.

Example:

```text
push 3 -> stack: [3]          min_stack: [3]
push 5 -> stack: [3, 5]       min_stack: [3]
push 2 -> stack: [3, 5, 2]    min_stack: [3, 2]
push 2 -> stack: [3, 5, 2, 2] min_stack: [3, 2, 2]
```

If we pop one `2`, there is still another `2` left, so the minimum should still be `2`.

That is why duplicate minimums must also be stored.

## `pop()`

```python
if self.stack.pop() == self.min_stack[-1]:
    self.min_stack.pop()
```

When removing the top value from the normal stack:

- if that value is also the current minimum
- remove it from `min_stack` too

This keeps `min_stack[-1]` always equal to the current minimum.

## `top()`

```python
return self.stack[-1]
```

The top of a stack is the last element in the list.

## `getMin()`

```python
return self.min_stack[-1]
```

The current minimum is always stored at the top of `min_stack`.

So `getMin()` is `O(1)`.

## Python Class Notes

### What is a class?

A class is a blueprint for creating objects.

For this problem, `MinStack` is the blueprint. When LeetCode runs:

```python
obj = MinStack()
```

Python creates one MinStack object.

That object has its own:

- `stack`
- `min_stack`

### What is `__init__`?

```python
def __init__(self):
    self.stack = []
    self.min_stack = []
```

`__init__` runs automatically when a new object is created.

So this:

```python
obj = MinStack()
```

automatically calls:

```python
obj.__init__()
```

The job of `__init__` is to set up the starting data for the object.

In this problem, the starting data is two empty lists.

### What is `self`?

`self` means "this object itself".

Inside the class, when we write:

```python
self.stack
```

it means:

```python
this MinStack object's stack
```

Example:

```python
obj = MinStack()
obj.push(5)
```

When `push` runs, Python secretly passes `obj` as `self`.

So this method:

```python
def push(self, val):
    self.stack.append(val)
```

acts like:

```python
obj.stack.append(5)
```

### Why do we need `self.stack` instead of just `stack`?

If we write:

```python
stack = []
```

inside a method, it is just a local variable. It disappears after the method finishes.

But if we write:

```python
self.stack = []
```

the list belongs to the object and can be used by all methods:

- `push`
- `pop`
- `top`
- `getMin`

That is why object data usually uses `self`.

## Complexity

- `push`: `O(1)`
- `pop`: `O(1)`
- `top`: `O(1)`
- `getMin`: `O(1)`

Space: `O(n)`

Why:

- `stack` can store all values.
- `min_stack` can also store up to `n` values if every new value is smaller than or equal to the previous minimum.

## Key Learning

- Use an extra stack to remember minimum values.
- Store duplicate minimums in `min_stack`, or popping one duplicate can break the answer.
- `__init__` prepares object data when the object is created.
- `self` lets different methods access the same object's data.
