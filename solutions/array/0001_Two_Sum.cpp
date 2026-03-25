class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> com;
        for(int i = 0 ; i < nums.size() ; i++){
            int complement = target - nums[i];
            if(com.find(complement) != com.end()){
                return {com[complement], i};
            }
            com[nums[i]] = i;
        }
        return {};
    }
};