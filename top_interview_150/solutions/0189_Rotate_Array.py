#Python version
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k steps in-place.
        """
        n = len(nums)
        if n == 0:
            return

        k %= n  # Normalize k when k is larger than n.

        def reverse(left, right):
            # Reverse nums[left:right + 1] in-place.
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire array.
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements.
        reverse(0, k - 1)

        # Step 3: Reverse the remaining n - k elements.
        reverse(k, n - 1)

'''
C++ version 
class Solution {
private:
    void reverse(vector<int>& nums, int left, int right) {
        while (left < right) {
            swap(nums[left], nums[right]); //built-in
            ++left;
            --right;
        }
    }

public:
    void rotate(vector<int>& nums, int k) {
        int n = static_cast<int>(nums.size());

        if (n == 0) {
            return;
        }

        k %= n;

        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }
};
'''