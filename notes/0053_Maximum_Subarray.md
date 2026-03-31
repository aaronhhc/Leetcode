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