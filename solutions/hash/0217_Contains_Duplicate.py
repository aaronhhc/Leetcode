class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() //hash set
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            
