class Solution {
public:
  int pivotIndex(vector<int>& nums) {
    int left, right;
    vector<int> prefix;
    
    prefix.push_back(0);
    for (int i = 0; i < nums.size(); i++) {
      prefix.push_back(nums[i] + prefix[prefix.size() - 1]);
    }
    for (int i = 1; i < prefix.size(); i++) {
      left = prefix[i - 1];
      right = prefix[prefix.size() - 1] - prefix[i];
      if (left == right) return i - 1;
    }
    
    return -1;
  }
};