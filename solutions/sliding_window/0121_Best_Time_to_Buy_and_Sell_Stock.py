class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            profit = max(prices[i] - curr, profit)
        return profit
