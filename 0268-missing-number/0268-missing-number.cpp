class Solution {
public:
  int missingNumber(vector<int>& nums) {
    int ans = 0, n = nums.size();
    
    for (auto& num: nums) ans += num;
    
    return n * (n + 1) / 2 - ans;
  }
};