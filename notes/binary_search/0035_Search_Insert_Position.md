# 0035 Search Insert Position

## Problem Idea

We are given:

- a sorted array `nums`
- a target value `target`

We need to return the index of `target`.

If `target` is not in the array, return the index where it should be inserted to keep the array sorted.

Example:

```text
nums = [1, 3, 5, 6]
target = 5
answer = 2
```

The value `5` already exists at index `2`.

Another example:

```text
nums = [1, 3, 5, 6]
target = 2
answer = 1
```

The value `2` should be inserted before `3`, so the answer is index `1`.

Because the array is sorted, we can use binary search.

---

## Binary Search Idea

This problem is similar to regular binary search.

The difference is:

- if we find `target`, return its index
- if we do not find `target`, return the position where the search ended

At the end, `low` is the first position where `target` could be inserted.

---

## My Code Notes

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return low
```

What this code does:

- Start with the whole array as the search range.
- Find the middle index.
- If the middle value equals `target`, return `mid`.
- If `target` is larger, search the right half.
- If `target` is smaller, search the left half.
- If the loop ends, return `low` as the insert position.

---

## Why Return `low`?

When the loop ends, `low > high`.

At that moment:

- everything before `low` is smaller than `target`
- everything from `low` onward is greater than `target`

So `low` is exactly where `target` should be inserted.

Example:

```text
nums = [1, 3, 5, 6]
target = 2
```

At the end:

```text
low = 1
high = 0
```

Index `1` is the correct insert position because `2` belongs between `1` and `3`.

---

## Pointer Movement

### When `target > nums[mid]`

The middle value is too small.

Since the array is sorted, `target` must be to the right.

So we move `low`:

```python
low = mid + 1
```

### When `target < nums[mid]`

The middle value is too large.

Since the array is sorted, `target` must be to the left.

So we move `high`:

```python
high = mid - 1
```

---

## Walkthrough

Example:

```text
nums = [1, 3, 5, 6]
target = 2
```

Start:

```text
low = 0
high = 3
```

First middle:

```text
mid = (0 + 3) // 2 = 1
nums[mid] = 3
```

`2` is smaller than `3`, so search the left half:

```text
low = 0
high = 0
```

Second middle:

```text
mid = (0 + 0) // 2 = 0
nums[mid] = 1
```

`2` is larger than `1`, so search the right side:

```text
low = 1
high = 0
```

Now `low > high`, so the loop stops.

Return `low`, which is `1`.

---

## Edge Cases

### Insert at the beginning

```text
nums = [1, 3, 5, 6]
target = 0
answer = 0
```

### Insert at the end

```text
nums = [1, 3, 5, 6]
target = 7
answer = 4
```

### Target already exists

```text
nums = [1, 3, 5, 6]
target = 5
answer = 2
```

---

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

Why:

- Each loop removes about half of the search range.
- Only `low`, `high`, and `mid` are used.

---

## Key Learning

- This is binary search with an insertion answer.
- If `target` is found, return `mid`.
- If `target` is not found, return `low`.
- After the search ends, `low` points to the first valid insert position.
