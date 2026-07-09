class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #消去
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
            #print(candidate, count)
        return candidate
