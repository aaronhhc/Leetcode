class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left -> Right:
        # If rating is higher than the left neighbor,
        # give more candy than the left neighbor.
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right -> Left:
        # If rating is higher than the right neighbor,
        # make sure candy is also higher than the right neighbor.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)