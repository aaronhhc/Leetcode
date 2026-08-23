class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        # res[i] stores the product of all elements to the left of i
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        suffix = 1

        # Multiply by the product of all elements to the right of i
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res