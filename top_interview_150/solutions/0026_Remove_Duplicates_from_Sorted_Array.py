#Python solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: #edge case
            return n
        #key = nums[0] #can switch to n[k - 1] because key is always n[k - 1]
        k = 1 #unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k

'''
C++ solution
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = static_cast<int>(nums.size());

        if (n <= 1) {
            return n;
        }

        // nums[0:k] stores the unique elements found so far.
        int k = 1;

        for (int i = 1; i < n; ++i) {
            // nums[k - 1] is the last unique element.
            if (nums[i] != nums[k - 1]) {
                nums[k++] = nums[i];
            }
        }

        return k;
    }
};
'''