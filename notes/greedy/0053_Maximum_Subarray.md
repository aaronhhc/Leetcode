# 0053 Maximum Subarray

## Idea
Use Kadane’s Algorithm.

At each position:
- decide whether to start a new subarray
- or extend the current subarray

Keep track of:
- `current_sum`: the best subarray sum ending at current position
- `max_sum`: the best subarray sum seen so far

## Why this works
If the current subarray sum becomes worse than starting fresh from the current number,  
then it is better to start a new subarray.

So for each element, we choose:
- `current number`
- or `current_sum + current number`

Then update the global maximum.

## Complexity
- Time: `O(n)`
- Space: `O(1)`

## Note
This is the optimal solution because every number must be checked at least once.

## Key Idea

At each position, we only need to think about one thing:

For `nums[i]`, what is the **maximum subarray sum ending at `nums[i]`**?

There are only two possibilities:

1. Extend the previous subarray  
2. Start a new subarray from the current number

So the transition is:

`current_sum = max(nums[i], current_sum + nums[i])`

This means:

- if the previous sum is still useful, keep extending it
- if the previous sum becomes a burden, start fresh from `nums[i]`