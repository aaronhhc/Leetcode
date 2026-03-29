# 0121 Best Time to Buy and Sell Stock

## Idea
Use one pass to find the maximum profit.

- `curr`: the lowest price seen so far
- `profit`: the maximum profit so far

For each day, we do two things:
1. Update the minimum price
2. Calculate the profit if selling on that day
3. Keep the maximum profit

## Example
For `prices = [7, 1, 5, 3, 6, 4]`:

- The minimum price becomes `1`
- The best profit is `6 - 1 = 5`

So the answer is `5`.

## Complexity
- Time: `O(n)`
- Space: `O(1)`

## Note
This problem allows only **one transaction**.

The key idea is:

**track the lowest price first, then compute the largest possible profit after it.**