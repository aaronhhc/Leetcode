class Solution:
    #my solution during contest
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return [0]
        res = [0] * len(nums)
        for i in range(len(nums) - 1):
            j = i + 1
            key = nums[i] % 2
            if key == 0: #even
                while j < len(nums):
                    if nums[j] % 2 != 0: #oppo -> odd
                        res[i] += 1
                    j += 1
            else: #odd
                while j < len(nums):
                    if nums[j] % 2 == 0: #oppo -> even
                        res[i] += 1
                    j += 1
        return res

    #standard solution using suuffix
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
