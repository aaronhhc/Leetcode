class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Track the lowest buying price seen so far.
            min_price = min(price, min_price)

            # Sell today and update the best profit if possible.
            max_profit = max(max_profit, price - min_price)

        return max_profit