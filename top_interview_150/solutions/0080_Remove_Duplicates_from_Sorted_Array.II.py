class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        count = 1
        for i in range(1, n):
            if nums[i] == nums[k - 1] and count < 2:
                nums[k] = nums[i]
                k += 1
                count += 1
            elif nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
                count = 1
        return k
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        # nums[0:k] stores the valid elements found so far.
        for x in nums:
            # Always keep the first two elements.
            # After that, only keep x if it is different from nums[k - 2].
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1

        return k
'''