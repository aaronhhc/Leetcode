#My solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        n = len(nums)
        if n == 0:
            return 0
        total = 1
        curr_best = 1
        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                curr_best += 1
            else:
                total = max(curr_best, total)
                curr_best = 1
        total = max(curr_best, total)

        return total
#############################################################################
#Better solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_streak = 0
        for num in nums:
            if num - 1 not in nums:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak