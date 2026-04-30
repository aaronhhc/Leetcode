# 0704 Binary Search

## Problem Idea

We are given:

- a sorted array `nums`
- a target value `target`

We need to return the index of `target`.

If `target` does not exist in the array, return `-1`.

Example:

```text
nums = [-1, 0, 3, 5, 9, 12]
target = 9
answer = 4
```

The value `9` is at index `4`.

Because the array is sorted, we can use binary search instead of checking every number one by one.

---

## Binary Search Idea

Use two pointers:

- `low` starts at the first index
- `high` starts at the last index

Each time:

- calculate the middle index
- compare `nums[mid]` with `target`
- remove the half that cannot contain the answer

The search range keeps getting smaller until we either find the target or the range becomes empty.

---

## My Code Notes

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
```

What this code does:

- Start with the whole array as the search range.
- Find the middle index.
- If the middle value is the target, return `mid`.
- If the middle value is smaller than the target, search the right half.
- If the middle value is larger than the target, search the left half.
- If the loop ends, the target is not in the array.

---

## Pointer Movement

### When `nums[mid] < target`

The middle value is too small.

Since the array is sorted, every value to the left of `mid` is also too small.

So we move `low`:

```python
low = mid + 1
```

### When `nums[mid] > target`

The middle value is too large.

Since the array is sorted, every value to the right of `mid` is also too large.

So we move `high`:

```python
high = mid - 1
```

---

## Walkthrough

Example:

```text
nums = [-1, 0, 3, 5, 9, 12]
target = 9
```

Start:

```text
low = 0
high = 5
```

First middle:

```text
mid = (0 + 5) // 2 = 2
nums[mid] = 3
```

`3` is smaller than `9`, so search the right half:

```text
low = 3
high = 5
```

Second middle:

```text
mid = (3 + 5) // 2 = 4
nums[mid] = 9
```

Found the target, so return `4`.

---

## Why `while low <= high`?

The condition means the search range is still valid.

When `low == high`, there is still one number left to check.

When `low > high`, the search range is empty, so the target does not exist.

That is why the function returns `-1` after the loop.

---

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

Why:

- Each step removes about half of the remaining search range.
- Only a few variables are used.

---

## Key Learning

- Binary search works when the array is sorted.
- `low` and `high` represent the current possible search range.
- Use `mid + 1` and `mid - 1` because `mid` has already been checked.
- Remember to keep `while low <= high` so the last remaining element is checked.
