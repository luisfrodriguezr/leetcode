class Solution {
public:
  vector<int> largestSubarray(vector<int>& nums, int k) {
    vector<int> ans;
    int max = 0;
    bool flag = false;
    for (int i = 0; i <= nums.size() - k; i++) {
      if (nums[i] > max) max = nums[i];
    }
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == max) flag = true;
      if (flag) ans.push_back(nums[i]);
      if (ans.size() == k) break;
    }
    return ans;
  }
};