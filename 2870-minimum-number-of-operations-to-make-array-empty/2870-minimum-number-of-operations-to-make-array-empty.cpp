class Solution {
public:
  int minOperations(vector<int>& nums) {
    sort(begin(nums), end(nums));
    int ans = 0;
    float count = 1;
    
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] != nums[i - 1]) {
        if (count < 2) return -1;
        ans += ceil(count / 3);
        count = 1;
      } else count++;
    }
    if (count < 2) return -1;
    ans += ceil(count / 3);
    return ans;
  }
};