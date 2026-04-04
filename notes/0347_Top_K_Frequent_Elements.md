# 0347 Top K Frequent Elements

## Problem Idea

We need to return the `k` numbers that appear most often in `nums`.

The core of this problem is:

1. Count how many times each number appears.
2. Pick the `k` numbers with the highest frequency.

---

## My Code Notes

### 1. Self-written solution

```python
keys = set(nums)
freq = dict.fromkeys(keys, 0)
for num in nums:
    freq[num] += 1
sorted_freq = dict(sorted(freq.items(), key = lambda x:x[1], reverse = True))
return list(sorted_freq.keys())[:k]
```

What this version does:

- `set(nums)` gets all unique numbers first.
- `dict.fromkeys(keys, 0)` creates a frequency table with initial value `0`.
- The loop counts how many times each number appears.
- `sorted(...)` sorts the dictionary items by frequency from large to small.
- Finally, it returns the first `k` keys.

Why it works:

- Every number is counted correctly.
- Sorting by frequency ensures the most frequent numbers come first.

Time complexity:

- Counting: `O(n)`
- Sorting: `O(m log m)`, where `m` is the number of unique values
- Total: `O(n + m log m)`

Space complexity:

- `O(m)`

Small note:

- Converting the sorted result back into a dictionary is not necessary here. You only need the sorted list of pairs or keys.

---

### 2. Better sorting solution

```python
freq = defaultdict(int)
for num in nums:
    freq[num] += 1
sorted_freq = sorted(freq.items(), key = lambda x:x[1], reverse = True)
return [num for num, count in sorted_freq[:k]]
```

What improved:

- `defaultdict(int)` makes frequency counting cleaner.
- `sorted_freq` stays as a list of `(num, count)` pairs, which is simpler than converting back to a dictionary.
- The list comprehension directly extracts the answer.

Why this version is cleaner:

- Less unnecessary conversion.
- Easier to read.
- Keeps the same overall logic.

Time complexity:

- Still `O(n + m log m)`

Space complexity:

- Still `O(m)`

---

### 3. Bucket sort solution

```python
freq = defaultdict(int)
for num in nums:
    freq[num] += 1

bucket = [[] for _ in range(len(nums) + 1)]
for num, count in freq.items():
    bucket[count].append(num)

ans = []
for count in range(len(bucket) - 1, 0, -1):
    for num in bucket[count]:
        ans.append(num)
        if len(ans) == k:
            return ans
```

Main idea:

- A number can appear at most `len(nums)` times.
- So we create buckets where:
  - index = frequency
  - value = list of numbers with that frequency

Example:

- If `2` appears 3 times, then `2` goes into `bucket[3]`.
- If `5` appears 1 time, then `5` goes into `bucket[1]`.

Why this is faster:

- We avoid sorting all unique elements.
- We just scan the buckets from high frequency to low frequency.

Time complexity:

- Counting: `O(n)`
- Filling buckets: `O(m)`
- Scanning buckets: `O(n)`
- Total: `O(n)`

Space complexity:

- `O(n)`

Why this is the best solution in your file:

- It matches the common optimal approach for this problem.
- It is faster than sorting when the input gets large.

---

## Key Learning

- Hash map is used to count frequency.
- Sorting solution is easier to think of first.
- Bucket sort uses the fact that frequency is bounded by `n`.
- This problem is a good example of turning a sorting problem into a linear-time solution.

---

## Code Style Notes

- Your progression is good: brute-force thinking -> cleaner hash map solution -> optimal bucket solution.
- If you want this Python file to run directly on LeetCode, make sure the imports are included:

```python
from typing import List
from collections import defaultdict
```

- Since the file currently defines `class Solution` three times, only the last one will actually remain if the file is executed as normal Python. That is fine for keeping study notes, but if you want to submit one version, keep only the approach you want to use.
