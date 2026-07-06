# 你的版本
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # index
        n = len(nums)  # available length
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1  # available - 1
                # no i + 1 because we need to check the new value at index i
            else:
                i += 1
        return n


# ----------------------------------------


# 標準版本
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for x in nums:
            if x != val:
                nums[k] = x
                k += 1

        return k

'''
C++ 版本
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        int n = static_cast<int>(nums.size()); 

        //nums.size() 的型別是 size_t, 而 i 是 int, 嚴格一點會有 signed / unsigned comparison warning。
        for (int i = 0; i < n; ++i) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        
        return k;
    }
};
'''
