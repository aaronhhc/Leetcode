# 3917 Count Indices With Opposite Parity

## Problem Idea

Given an integer array `nums`, return an array `res` where:

```text
res[i] = number of indexes j where j > i and nums[j] has opposite parity from nums[i]
```

Opposite parity means:

- even number vs odd number
- odd number vs even number

Example:

```text
nums = [1, 2, 3, 4]
```

For index `0`, `nums[0] = 1`, which is odd.

The later even numbers are `2` and `4`, so:

```text
res[0] = 2
```

## My First Idea

My contest solution checks every number after the current index.

For each `i`:

- get the parity of `nums[i]`
- scan from `i + 1` to the end
- count numbers with the opposite parity

This works, but it repeats a lot of checking.

If `nums` has length `n`, each index may scan almost the whole rest of the array.

So the time complexity is `O(n^2)`.

## My Code Notes

```python
def countOppositeParity(self, nums: list[int]) -> list[int]:
    if len(nums) == 1:
        return [0]

    res = [0] * len(nums)

    for i in range(len(nums) - 1):
        j = i + 1
        key = nums[i] % 2

        if key == 0:
            while j < len(nums):
                if nums[j] % 2 != 0:
                    res[i] += 1
                j += 1
        else:
            while j < len(nums):
                if nums[j] % 2 == 0:
                    res[i] += 1
                j += 1

    return res
```

What this code does:

- `key = nums[i] % 2` checks whether `nums[i]` is even or odd.
- If `nums[i]` is even, count later odd numbers.
- If `nums[i]` is odd, count later even numbers.
- The last index always stays `0` because there are no later numbers.

## Optimized Idea

Instead of scanning the right side again and again, scan from right to left.

Keep two counters:

- `even_count`: how many even numbers are already seen on the right
- `odd_count`: how many odd numbers are already seen on the right

When we are at index `i`:

- if `nums[i]` is even, the answer is `odd_count`
- if `nums[i]` is odd, the answer is `even_count`

Then update the counter for `nums[i]`.

This is a suffix count idea.

## Standard Code Notes

```python
def countOppositeParity(self, nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    even_count = 0
    odd_count = 0

    for i in range(n - 1, -1, -1):
        if nums[i] % 2 == 0:
            res[i] = odd_count
            even_count += 1
        else:
            res[i] = even_count
            odd_count += 1

    return res
```

What this code does:

- Start from the last index.
- `even_count` and `odd_count` represent numbers to the right of current index.
- Store the opposite parity count into `res[i]`.
- Add current number into its own parity counter.

## Walkthrough

Example:

```text
nums = [1, 2, 3, 4]
```

Start:

```text
res = [0, 0, 0, 0]
even_count = 0
odd_count = 0
```

Index `3`, value `4` is even:

```text
res[3] = odd_count = 0
even_count = 1
```

Index `2`, value `3` is odd:

```text
res[2] = even_count = 1
odd_count = 1
```

Index `1`, value `2` is even:

```text
res[1] = odd_count = 1
even_count = 2
```

Index `0`, value `1` is odd:

```text
res[0] = even_count = 2
odd_count = 2
```

Final answer:

```text
[2, 1, 1, 0]
```

## Important Python Note

In the current file, `countOppositeParity` appears twice in the same class.

Python only keeps the second definition, so the optimized suffix-count version is the one that actually runs.

## Complexity

Brute force version:

- Time: `O(n^2)`
- Space: `O(n)` for the result array

Optimized suffix-count version:

- Time: `O(n)`
- Space: `O(n)` for the result array
