# 0169 Majority Element

## Problem

Given an array `nums`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times.

You may assume that the majority element always exists in the array.

Example:

```text
nums = [3, 2, 3]
```

Result:

```text
3
```

---

## My Code Notes

This problem is solved with the Boyer-Moore Voting Algorithm.

### Key idea

Keep a candidate and a counter while scanning the array once.

- Start with `candidate = None` and `count = 0`.
- For each value `num` in `nums`:
  - if `count == 0`, set `candidate = num`.
  - if `num == candidate`, increment `count`.
  - otherwise, decrement `count`.

At the end, `candidate` is the majority element.

### Why it works

A majority element has more occurrences than all other values combined.
Every time a non-candidate value appears, it cancels out one candidate count.
Because the majority appears more than half the time, the candidate cannot be
fully canceled.

This gives a linear time, constant space solution.

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 消去
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
            # print(candidate, count)

        return candidate
```

---

## Complexity

- Time: `O(n)`
- Space: `O(1)`

---

## Example Walkthrough

```text
nums = [2, 2, 1, 1, 1, 2, 2]
```

Process:

- candidate = 2, count = 1
- see 2, count = 2
- see 1, count = 1
- see 1, count = 0
- see 1, candidate = 1, count = 1
- see 2, count = 0
- see 2, candidate = 2, count = 1

Result: majority element is `2`.
