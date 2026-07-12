# LeetCode 55. Jump Game

Given an array `nums`, each element means the maximum jump length from that position. We want to decide whether we can reach the last index.

## 1. My initial approach

My first idea was to use a variable `count` to represent the remaining jump power.

- I moved forward step by step.
- Each time I moved, I decreased `count`.
- If I saw a larger value at the current index, I updated `count`.

This can work, but it is harder to reason about because `count` is not the main state we care about. We are really asking:

- Which indices are reachable?
- What is the farthest index we can reach so far?

That makes the problem easier to explain with a greedy invariant.

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        count = nums[0]
        if count == 0:
            return False

        for i in range(0, n - 1):
            if nums[i] == 0 and count == 0:
                return False
            if nums[i] > count:
                count = nums[i]
            if count >= (n - 1 - i):
                return True
            else:
                count -= 1
```

## 2. Key improvement

Instead of tracking remaining jump power, we should track the farthest reachable index.

- `farthest` = the farthest index we can reach so far
- For each index `i`:
  - If `i > farthest`, then index `i` is not reachable.
  - Otherwise, we can update:
    `farthest = max(farthest, i + nums[i])`

This is a cleaner greedy idea because we only care about the reachable range, not about simulating every jump one by one.

## 3. Greedy idea

We do not need to simulate every possible path.

We only need to know:

- whether the current index is reachable
- how far we can extend from this index

If the current index is reachable, it helps us expand the reachable range. If every visited index is reachable, then the last index is reachable.

## 4. Clean Python solution

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            # If the current index is beyond our reach, we cannot continue.
            if i > farthest:
                return False

            # Update the farthest index reachable so far.
            farthest = max(farthest, i + nums[i])

        return True
```

## 5. Optional early return version

This version can stop earlier as soon as the last index becomes reachable.

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if farthest >= last:
                return True

        return True
```

## 6. Important invariant

The main invariant is:

- `farthest` always stores the farthest index reachable using the positions we have already scanned.

From this invariant:

- If `i <= farthest`, then index `i` is reachable.
- If `i > farthest`, then there is no way to reach index `i`.

That is the core reason the greedy solution works.

## 7. Trace example

### Example 1: `nums = [2, 3, 1, 1, 4]`

- Start: `farthest = 0`
- At `i = 0`, `farthest = max(0, 0 + 2) = 2`
- At `i = 1`, `farthest = max(2, 1 + 3) = 4`
- We reach the end, so the answer is `True`

### Example 2: `nums = [3, 2, 1, 0, 4]`

- Start: `farthest = 0`
- At `i = 0`, `farthest = 3`
- At `i = 1`, `farthest = 3`
- At `i = 2`, `farthest = 3`
- At `i = 3`, `farthest = 3`
- At `i = 4`, we are already beyond `farthest`, so the function returns `False`

## 8. Complexity

- Time complexity: `O(n)`
- Space complexity: `O(1)`

## 9. My common mistakes and what to improve

- I tracked remaining jump power with `count`, but that made the logic harder to explain.
- I added extra edge-case checks because my loop invariant was not clear enough.
- I should think in terms of the reachable range instead of simulating jumps one by one.
- I should define the meaning of each variable before coding.
- I should prefer names like `farthest` when they directly describe the greedy state.
- I should write comments that explain the invariant, not just the syntax.
