class Solution {
public:
  vector<int> getAverages(vector<int>& nums, int k) {
    vector<int> ans(nums.size(), -1);
    if (k >= nums.size() / 2 + 1) return ans;
    int r = k*2 + 1;
    long long curr = 0;
    for (int i = 0; i < 2*k; i++) {
      curr += nums[i];
    }
    for (int i = k; i < nums.size() - k; i++) {
      curr += nums[i + k];
      ans[i] = curr / r;
      curr -= nums[i - k];
    }
    return ans;
  }
};