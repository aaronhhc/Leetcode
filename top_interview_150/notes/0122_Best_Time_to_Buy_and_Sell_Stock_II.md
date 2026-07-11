# 0122 Best Time to Buy and Sell Stock II

## Idea
Capture every profitable transaction. You can make as many transactions as you want.

The key insight: sum all positive differences between consecutive prices. Each time the price goes up, we make a profit on that increment.

看到上漲就賺，不需要預測最高點。
只要今天比昨天貴，就可以賺這段差價

## Algorithm
1. Initialize `profit` to 0
2. Iterate through prices starting from index 1:
   - If current price is higher than previous price, add the difference to profit
   - This effectively captures every "uphill" as a transaction
3. Return total `profit`

## Example
For `prices = [7, 1, 5, 3, 6, 4]`:

- Day 0→1: 1 < 7, skip (no profit)
- Day 1→2: 5 > 1, profit += 4
- Day 2→3: 3 < 5, skip
- Day 3→4: 6 > 3, profit += 3
- Day 4→5: 4 < 6, skip

Total profit: 4 + 3 = 7

This is equivalent to buying at 1, selling at 5, buying at 3, selling at 6.

## Complexity
- Time: `O(n)` - single pass through prices
- Space: `O(1)` - constant extra space

## Key Differences from 0121
- 0121: One transaction only
- 0122: Unlimited transactions allowed

**Greedy approach**: capture every uphill segment as a profit opportunity.
