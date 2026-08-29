# LeetCode 135 - Candy

## Problem

There are `n` children standing in a line.

Each child has a rating given by `ratings[i]`.

Rules:

1. Every child must get at least `1` candy.
2. A child with a higher rating than an adjacent child must get more candies.

Return the minimum number of candies needed.

---

## Key Idea

Each child may need to satisfy conditions from both sides:

```text
left neighbor <- child -> right neighbor
```

Instead of handling both directions at the same time, separate them into two passes.

### Pass 1: Left -> Right

Only consider the left neighbor.

If:

```python
ratings[i] > ratings[i - 1]
```

then:

```python
candies[i] = candies[i - 1] + 1
```

This guarantees:

```text
higher rating than left neighbor
-> more candies than left neighbor
```

### Pass 2: Right -> Left

Now consider the right neighbor.

If:

```python
ratings[i] > ratings[i + 1]
```

then `candies[i]` must be greater than `candies[i + 1]`.

However, the first pass may already have assigned more candies to `i`.

So we use:

```python
candies[i] = max(candies[i], candies[i + 1] + 1)
```

---

## Why `max()`?

Example:

```text
ratings = [1, 2, 3, 4, 2, 1]
```

Initially:

```text
candies = [1, 1, 1, 1, 1, 1]
```

After the left-to-right pass:

```text
ratings = [1, 2, 3, 4, 2, 1]
candies = [1, 2, 3, 4, 1, 1]
```

Now scan from right to left.

At `i = 4`:

```text
rating: 2 > 1
```

So:

```python
candies[4] = max(1, 1 + 1)
           = 2
```

Now:

```text
candies = [1, 2, 3, 4, 2, 1]
```

At `i = 3`:

```text
rating: 4 > 2
```

The right side requires at least:

```text
candies[4] + 1 = 3
```

But the first pass already gave:

```text
candies[3] = 4
```

Therefore:

```python
candies[3] = max(4, 3)
           = 4
```

If we directly wrote:

```python
candies[i] = candies[i + 1] + 1
```

then `candies[3]` would become `3`, causing:

```text
ratings = [1, 2, 3, 4, 2, 1]
candies = [1, 2, 3, 3, 2, 1]
```

Now rating `4 > 3`, but candies are `3 == 3`, which violates the rule.

So `max()` means:

```text
keep the left-side requirement
OR
satisfy the right-side requirement

take the larger one
```

---

## Final Solution

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left -> Right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right -> Left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
```

---

## Complexity

```text
Time: O(n)
Space: O(n)
```

We scan the array twice, so the total time is still `O(n)`.

The `candies` array requires `O(n)` extra space.

---

## Mistakes / Confusing Points

### 1. Trying to handle both neighbors at once

My first implementation tried to repeatedly fix both sides in multiple loops.

This made the logic more complicated than necessary.

Better:

```text
Pass 1: only satisfy the left neighbor
Pass 2: only satisfy the right neighbor
```

### 2. Why two passes?

A left-to-right pass can only naturally guarantee the condition with the left neighbor.

For example:

```text
ratings = [3, 2, 1]
```

The decreasing direction cannot be correctly handled using only a left-to-right pass.

So another pass from right to left is needed.

### 3. Why `max()`?

The first pass may already assign a larger value because of the left neighbor.

The second pass should not destroy that result.

Therefore:

```python
candies[i] = max(candies[i], candies[i + 1] + 1)
```

---

## Takeaway

```text
Initialize everyone with 1 candy.

Left -> Right:
    satisfy the left-neighbor condition.

Right -> Left:
    satisfy the right-neighbor condition.

Use max():
    keep whichever side requires more candies.
```

Core pattern:

```python
candies[i] = max(
    current_left_requirement,
    right_requirement
)
```

A child must satisfy both neighbors, so keep the larger requirement.