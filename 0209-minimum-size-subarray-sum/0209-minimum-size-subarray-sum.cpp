class Solution {
public:
  int minSubArrayLen(int target, vector<int>& nums) {
    int left = 0, ans = 100001;
    long long curr = 0;
    
    for (int right = 0; right < nums.size(); ++right) {
      curr += nums[right];
      
      while (curr >= target) {
        ans = min(ans, right - left + 1);
        curr -= nums[left++];
      }
    }
    
    return left > 0 ? ans : 0;
  }
};