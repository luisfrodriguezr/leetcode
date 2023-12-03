class Solution {
public:
  int maximumStrongPairXor(vector<int>& nums) {
    int max = 0;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i; j < nums.size(); j++) {
        if (std::abs(nums[j] - nums[i]) <= std::min(nums[i], nums[j])) {
            if ((nums[i] ^ nums[j]) > max) {
                max = nums[i] ^ nums[j];
            }
        }
      }
    }
    return max;
  }
};