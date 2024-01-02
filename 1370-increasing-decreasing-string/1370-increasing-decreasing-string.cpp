class Solution {
public:
  string sortString(string s) {
    int ht[26] = {};
    string ans = "";
 
    for (int i = 0; i < s.size(); i++) ht[s[i] - 'a']++;
    
    int step = 1, i = 0, n = s.size(), m = 0;
    while (m < n) {
      if (i == -1) {
        step = 1;
        i = 0;
      }
      if (i == 26) {
        step = -1;
        i = 25;
      }
      if (ht[i] > 0) {
        ans += char('a' + i);
        m++;
        ht[i]--;
      }
      i += step;
    }
    
    return ans;
  }
};