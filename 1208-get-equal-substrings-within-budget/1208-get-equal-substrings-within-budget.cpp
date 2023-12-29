class Solution {
public:
  int equalSubstring(string s, string t, int maxCost) {
    int ans = 0, curr = 0, left = 0;
    
    for (int right = 0; right < s.size(); right++) {
      curr += abs(s.at(right) - t.at(right));
      
      while (curr > maxCost) {
        curr -= abs(s.at(left) - t.at(left));
        left++;
      }
      
      ans = max(ans, right - left + 1);
    }
    
    return ans;
  }
};