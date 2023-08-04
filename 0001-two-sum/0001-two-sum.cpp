class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i=0;
        for(auto num1: nums){
            int j=0;
            for(auto num2: nums){
                if(num1+num2==target && i!=j){
                    return {i, j};
                }
                j++;
            }
            i++;
        }
        return {0, 0};
    }
};