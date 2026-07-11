# 0121 Best Time to Buy and Sell Stock

## Idea
Use one pass to find the maximum profit.

- `min_price`: the lowest price seen so far
- `max_profit`: the maximum profit so far

For each day, we do two things:
1. Update the minimum price seen so far
2. Calculate the profit if selling on that day and keep the maximum profit

## Algorithm
1. Initialize `min_price` to the first price and `max_profit` to 0
2. Iterate through prices:
   - Track the minimum price up to current day
   - Calculate profit: `current_price - min_price`
   - Update `max_profit` if current profit is better
3. Return `max_profit`

## Example
For `prices = [7, 1, 5, 3, 6, 4]`:

- Day 0: min_price = 7, max_profit = 0
- Day 1: min_price = 1, max_profit = 0
- Day 2: min_price = 1, max_profit = 4 (5 - 1)
- Day 3: min_price = 1, max_profit = 4
- Day 4: min_price = 1, max_profit = 5 (6 - 1) ✓
- Day 5: min_price = 1, max_profit = 5

Answer: `5`

## Complexity
- Time: `O(n)` - single pass through prices
- Space: `O(1)` - constant extra space

## Key Insight
This problem allows only **one transaction** (one buy, one sell).

**Track the lowest price first, then compute the largest possible profit after it.**
