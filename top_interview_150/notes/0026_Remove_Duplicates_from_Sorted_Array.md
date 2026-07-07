# 0026 Remove Duplicates from Sorted Array

## Problem

Given a sorted array `nums`, remove the duplicates in place and return the new length of the array.

The important requirement is that each element in the first `k` positions should be unique, and the relative order of the remaining elements must stay the same.

Example:

```text
nums = [1, 1, 2]
```

Result:

```text
nums = [1, 2, _]
return 2
```

---

## My Code Notes

This problem can be solved with a write pointer that keeps track of where the next unique value should go.

### 1) Python version from your file

This version uses `k` as the count of unique elements found so far.

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k
```

### How it works

- `k` starts at `1` because the first element is already considered unique.
- For each later element, compare it with the previous unique value `nums[k - 1]`.
- If it is different, place it into the next position `nums[k]` and increment `k`.

### 2) C++ version from your file

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = static_cast<int>(nums.size());

        if (n <= 1) {
            return n;
        }

        int k = 1;

        for (int i = 1; i < n; ++i) {
            if (nums[i] != nums[k - 1]) {
                nums[k++] = nums[i];
            }
        }

        return k;
    }
};
```

The logic is the same as the Python version, but the syntax is adapted for C++.

---

## Why It Works

Because the array is sorted, duplicates appear next to each other.

That means once we find a new value that is different from the previous unique value, we can safely place it into the next available slot.

At the end:

- the first `k` positions contain the unique elements
- the remaining positions can be ignored

This is an in-place solution, so no extra array is needed.

---

## Example Walkthrough

```text
nums = [0, 0, 1, 1, 1, 2, 2, 3]
```

Process:

- `0` is the first unique value
- next `0` is duplicate, skip
- `1` is new, place at index `1`
- next `1` is duplicate, skip
- `2` is new, place at index `2`
- `3` is new, place at index `3`

Final result:

```text
nums = [0, 1, 2, 3, _, _, _, _]
return 4
```

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

---

## Key Takeaway

This is a classic in-place array problem.

The main idea is to keep a pointer for the next unique position and overwrite duplicates as we scan the array.
