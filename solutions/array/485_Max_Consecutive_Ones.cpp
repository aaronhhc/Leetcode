class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0;
        int current = 0;
        for(int num : nums){
            if(num == 1){
                current += 1;
                maxCount = max(current, maxCount);
            }
            else{
                current = 0;
            }
        }
        return maxCount;
    }
};
