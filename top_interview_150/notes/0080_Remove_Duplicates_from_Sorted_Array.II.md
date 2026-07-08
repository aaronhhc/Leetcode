# 0080 Remove Duplicates from Sorted Array II

## Problem

Given a sorted array `nums`, remove duplicates in place such that each element appears at most twice and return the new length.

The first `k` elements of `nums` should contain the final result with the relative order preserved.

Example:

```text
nums = [0,0,1,1,1,2,2,3]
```

Result:

```text
nums = [0,0,1,1,2,2,3,_]
return 7
```

---

## My Code Notes

### Approach

Use a write pointer `k` to build the valid prefix of the array.

- Always keep the first element.
- Track how many times the current value is included so far.
- If a new value appears, write it and reset the count.
- If the same value appears and the count is less than `2`, keep it.
- Otherwise, skip it.

### Python Implementation

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        count = 1

        for i in range(1, n):
            if nums[i] == nums[k - 1] and count < 2:
                nums[k] = nums[i]
                k += 1
                count += 1
            elif nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
                count = 1

        return k
```

### Why This Works

The array is sorted, so duplicates appear consecutively.

- `k` marks the next write position for valid elements.
- `nums[k - 1]` is the last value included in the result prefix.
- `count` tracks how many times that value has been written.
- When a duplicate appears, we only accept it the second time.

At the end, the first `k` entries are the result and the rest of the array can be ignored.

### Example Walkthrough

```text
nums = [0,0,1,1,1,2,2,3]
```

- `0` kept, count = 1
- next `0` kept, count = 2
- `1` kept, reset count = 1
- next `1` kept, count = 2
- next `1` skipped because count == 2
- `2` kept, reset count = 1
- next `2` kept, count = 2
- `3` kept, reset count = 1

Result:

```text
nums = [0,0,1,1,2,2,3,_]
return 7
```

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

---

## Key Takeaway

For sorted arrays with a duplicate allowance, maintain a write pointer plus a small local count to preserve only the allowed number of duplicates in place.
