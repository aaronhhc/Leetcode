# 0027 Remove Element

## Problem

Given an array `nums` and a value `val`, remove all occurrences of `val` in place and return the new length of the array.

The relative order of the remaining elements must stay the same.

Example:

```text
nums = [3, 2, 2, 3], val = 3
```

Result:

```text
nums = [2, 2, _, _]
return 2
```

---

## My Code Notes

There are two common ways to solve this problem.

### 1) Python version from your code

This version uses two pointers and swaps from the end.

- `i` points to the current index being checked.
- `n` is the current available length.
- If `nums[i] == val`, replace it with `nums[n - 1]` and shrink `n`.
- Otherwise, move `i` forward.

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
```

This works because the values overwritten from the end are no longer needed, and the valid prefix is kept at the front.

### 2) Standard Python write-pointer version

This is the more common LeetCode-style solution.

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for x in nums:
            if x != val:
                nums[k] = x
                k += 1

        return k
```

Here, `k` is the next write position. Every time we see a value we want to keep, we place it at `nums[k]`.

### 3) C++ version

The C++ version uses the same idea as the standard Python version.

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        int n = static_cast<int>(nums.size());

        for (int i = 0; i < n; ++i) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }

        return k;
    }
};
```

Note: `nums.size()` returns `size_t`, so converting it to `int` avoids signed/unsigned comparison warnings.

---

## Why It Works

The first `k` positions of the array always contain the values we want to keep.

Each time we encounter a value that should remain:

- we write it into the next available slot
- then increase the write pointer

At the end, `k` is the length of the new array.

This is an in-place solution, so no extra array is needed.

---

## Example Walkthrough

```text
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
```

Process:

- `0` -> keep
- `1` -> keep
- `2` -> remove
- `2` -> remove
- `3` -> keep
- `0` -> keep
- `4` -> keep
- `2` -> remove

Final state:

```text
nums = [0, 1, 3, 0, 4, _, _, _]
return 5
```

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

---

## Key Takeaway

This problem can be solved in two clean ways:

1. swap values from the end
2. write kept values from the front

Both approaches are efficient, in-place, and work well for LeetCode-style submissions.
