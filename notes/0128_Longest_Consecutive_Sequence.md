# 0128 Longest Consecutive Sequence

## Problem Idea

We need to find the length of the longest sequence of consecutive numbers.

Example:

- `nums = [100, 4, 200, 1, 3, 2]`
- The longest consecutive sequence is `[1, 2, 3, 4]`
- Answer: `4`

The important part is:

- The numbers do not need to appear next to each other in the original array.
- We only care whether consecutive values exist.

---

## My Code Notes

### 1. Self-written solution

```python
nums = sorted(set(nums))
n = len(nums)
if n == 0:
    return 0

total = 1
curr_best = 1

for i in range(1, n):
    if nums[i - 1] + 1 == nums[i]:
        curr_best += 1
    else:
        total = max(curr_best, total)
        curr_best = 1

total = max(curr_best, total)
return total
```

What this version does:

- `set(nums)` removes duplicates.
- `sorted(...)` puts the numbers in increasing order.
- Then we scan the sorted numbers from left to right.
- If the current number is exactly `previous + 1`, the sequence continues.
- If not, the current consecutive sequence ends and we reset `curr_best`.

Why removing duplicates matters:

- For `nums = [1, 2, 2, 3]`, the duplicate `2` should not break the sequence.
- `set(nums)` changes it to `{1, 2, 3}`, so the sequence is handled cleanly.

Time complexity:

- `set(nums)`: `O(n)`
- sorting: `O(m log m)`, where `m` is the number of unique numbers
- scan: `O(m)`
- Total: `O(n + m log m)`

Space complexity:

- `O(m)` for the set / sorted unique list

This solution is correct and easy to understand, but it is not the optimal LeetCode solution because sorting costs `O(m log m)`.

---

### 2. Better set solution

```python
nums = set(nums)
longest_streak = 0

for num in nums:
    if num - 1 not in nums:
        curr_num = num
        curr_streak = 1

        while curr_num + 1 in nums:
            curr_num += 1
            curr_streak += 1

        longest_streak = max(longest_streak, curr_streak)

return longest_streak
```

Main idea:

- Use a set so we can check whether a number exists in `O(1)` average time.
- Only start counting a sequence from the first number in that sequence.

The key condition is:

```python
if num - 1 not in nums:
```

This means:

- `num` is the start of a sequence.
- Example: in `[1, 2, 3, 4]`, only `1` should start counting.
- `2`, `3`, and `4` are skipped as starting points because each has a previous number.

Why this avoids extra work:

- Without this check, we might count the same sequence many times.
- With this check, each consecutive chain is only expanded once.

Example:

For `nums = [100, 4, 200, 1, 3, 2]`, the set is:

```python
{1, 2, 3, 4, 100, 200}
```

Start points:

- `1` is a start because `0` is not in the set.
- `100` is a start because `99` is not in the set.
- `200` is a start because `199` is not in the set.
- `2`, `3`, and `4` are not starts because their previous numbers exist.

So the longest chain found is:

```python
1 -> 2 -> 3 -> 4
```

Answer: `4`

## Complexity

For the better set solution:

- Time: `O(n)` average
- Space: `O(n)`

Why time is `O(n)`:

- Creating the set takes `O(n)`.
- Each number is visited in the outer loop.
- The `while` loop only extends from sequence starts, so across the whole algorithm each number is part of a chain expansion at most once.

## Key Learning

- Sorting makes this problem easier to think about, but it gives `O(n log n)` time.
- A set lets us check neighbors quickly.
- The condition `num - 1 not in nums` is the key trick.
- Only begin counting from the start of a sequence.

