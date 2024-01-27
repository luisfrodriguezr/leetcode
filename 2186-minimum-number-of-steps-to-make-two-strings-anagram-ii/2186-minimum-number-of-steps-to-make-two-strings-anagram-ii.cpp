class Solution {
public:
  int minSteps(string s, string t) {
    int hash_table[26], ans = 0;
    
    for (int i = 0; i < max(s.size(), t.size()); i++) {
      if (i < s.size()) hash_table[s[i] - 'a']++;
      if (i < t.size()) hash_table[t[i] - 'a']--;
    }
    
    for (auto& num: hash_table) ans += abs(num);
    
    return ans;
  }
};