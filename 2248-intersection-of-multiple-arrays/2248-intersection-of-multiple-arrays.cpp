class Solution {
public:
  vector<int> intersection(vector<vector<int>>& nums) {
    int n = nums.size();
    map<int, int> hash_map; // Sorted hash_map using map (Balanced Binary search tree)
    vector<int> ans;
    
    
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < nums[i].size(); ++j) {
        ++hash_map[nums[i][j]];
      }
    }
    
    for (auto& [num, count]: hash_map) {
      if (count == n) ans.push_back(num);
    }
    
    return ans;
  }
};