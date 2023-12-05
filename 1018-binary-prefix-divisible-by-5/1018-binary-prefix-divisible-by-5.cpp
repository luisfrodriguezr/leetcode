class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
      int num = 0;
      vector<bool> ans;
      for (int i = 0; i < nums.size(); i++) {
        num = (num*2 + nums[i]) % 5;
        if (num) {
          ans.push_back(false);
        } else {
          ans.push_back(true);
        }
      }
      return ans;
    }
};