class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        #My solution
        n = len(nums)
        if n == 1:
            return True

        count = nums[0]
        if count == 0:
            return False

        for i in range(0, n - 1):
            if nums[i] == 0 and count == 0:
                return False
            if nums[i] > count:
                count = nums[i]
            if count >= (n - 1 - i):
                return True
            else:
                count -= 1
        '''
        #standard solution
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
        return True