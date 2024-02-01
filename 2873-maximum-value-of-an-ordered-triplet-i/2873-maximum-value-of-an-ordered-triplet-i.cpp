class Solution {
public:
  long long maximumTripletValue(vector<int>& nums) { 
    long long ans = 0;
    long long max_i = (long long)nums[0];
    long long max_ij = max_i - nums[1];
    
    for (int k = 2; k < nums.size(); ++k) {
      ans = max(ans, max_ij * nums[k]);
      max_i = max(max_i, (long long)nums[k - 1]);
      max_ij = max(max_ij, max_i - (long long)nums[k]);
    }
    
    return ans;
  }
};